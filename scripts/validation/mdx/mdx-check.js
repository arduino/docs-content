#!/usr/bin/env node
// Compiles pages with the MDX 1 that builds docs.arduino.cc, so broken HTML fails here instead of in the deploy
const fs = require('fs');
const path = require('path');
const mdx = require('@mdx-js/mdx');
const { parse } = require('@babel/parser');
const remarkSafeAlerts = require('./remark-safe-alerts');

const MDX_OPTIONS = { remarkPlugins: [remarkSafeAlerts] };
const VOID_TAGS = new Set(['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr']);
const TAG = /<(\/?)([A-Za-z][\w.:-]*)((?:[^<>"'{]|"[^"]*"|'[^']*'|\{[^}]*\})*?)(\/?)>/g;
// remark-safe-alerts turns an alert body into a string expression, whose `<model>` placeholders are not tags
const STRING_EXPRESSION = /\{"(?:[^"\\]|\\.)*"\}/g;

// Babel only says where the document ends, so find the tags that leave it unbalanced, with their source line
function unbalancedTags(src) {
  const compiler = mdx.createMdxAstCompiler(MDX_OPTIONS);
  const tags = [];
  const visit = (node) => {
    if (node.type === 'jsx' && node.position) {
      const value = node.value.replace(STRING_EXPRESSION, (s) => s.replace(/[^\n]/g, ' '));
      for (const m of value.matchAll(TAG)) {
        const line = node.position.start.line + (value.slice(0, m.index).match(/\n/g) || []).length;
        tags.push({ closing: !!m[1], name: m[2], selfClosing: !!m[4], line, text: m[0] });
      }
    }
    (node.children || []).forEach(visit);
  };
  visit(compiler.runSync(compiler.parse(src)));

  const problems = [];
  const open = [];
  for (const tag of tags) {
    if (tag.selfClosing) continue;
    if (!tag.closing) {
      open.push(tag);
      continue;
    }
    // Like an HTML parser, a closing tag also closes whatever was left open inside it
    const match = open.map(({ name }) => name).lastIndexOf(tag.name);
    if (match === -1) problems.push({ ...tag, stray: true });
    else problems.push(...open.splice(match).slice(1));
  }
  return problems.concat(open).sort((a, b) => a.line - b.line);
}

// MDX keeps raw HTML verbatim, so the line Babel points at can be found in the source
function sourceLine(src, message) {
  const marked = message.replace(/\x1b\[[0-9;]*m/g, '').match(/^>\s*\d+ \| (.*)$/m);
  const snippet = marked && marked[1].trim();
  if (!snippet || snippet.startsWith('</MDXLayout')) return null;
  const index = src.split('\n').findIndex((line) => line.includes(snippet.slice(0, 60)));
  return index === -1 ? null : { line: index + 1, text: snippet, error: true };
}

function describe(problem, reason) {
  if (problem.error) return `${reason} in ${problem.text}`;
  if (problem.stray) return `${problem.text} closes a tag that is not open`;
  if (VOID_TAGS.has(problem.name)) return `${problem.text} is never closed: write <${problem.name}${problem.text.slice(problem.name.length + 1, -1)}/>`;
  return `${problem.text} is never closed`;
}

function check(file) {
  const src = fs.readFileSync(file, 'utf8');
  try {
    parse(mdx.sync(src, MDX_OPTIONS), { sourceType: 'module', plugins: ['jsx'] });
    return null;
  } catch (error) {
    // Positions in the message refer to the generated code, not to the page
    const reason = error.message.split('\n')[0].replace(/^unknown: /, '').replace(/ \(\d+:\d+\)$/, '');
    let problems = [];
    try {
      problems = unbalancedTags(src);
    } catch {
      // The hint is best effort: the compile error above is the verdict
    }
    if (!problems.length) {
      const at = sourceLine(src, error.message);
      if (at) problems = [at];
    }
    return { reason, problems };
  }
}

function collect(target) {
  if (fs.statSync(target).isFile()) return [target];
  return fs.readdirSync(target, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(target, entry.name);
    if (entry.isDirectory()) return collect(full);
    return /\.mdx?$/.test(entry.name) ? [full] : [];
  });
}

const escapeData = (text) => text.replace(/%/g, '%25').replace(/\r/g, '%0D').replace(/\n/g, '%0A');
const escapeProperty = (text) => escapeData(text).replace(/:/g, '%3A').replace(/,/g, '%2C');

function annotate(file, message, line) {
  if (!process.env.GITHUB_ACTIONS) return;
  console.log(`::error file=${escapeProperty(file)}${line ? `,line=${line}` : ''}::${escapeData(message)}`);
}

const targets = process.argv.slice(2);
if (!targets.length) {
  console.error('Usage: node mdx-check.js <file or folder>...');
  process.exit(2);
}

const started = Date.now();
const files = targets.flatMap(collect);
let failed = 0;
for (const file of files) {
  const result = check(file);
  if (!result) continue;
  failed++;
  console.log(`\n✖ ${file}\n  ${result.reason}`);
  if (!result.problems.length) annotate(file, result.reason);
  for (const problem of result.problems) {
    console.log(`  line ${problem.line}: ${describe(problem, result.reason)}`);
    annotate(file, describe(problem, result.reason), problem.line);
  }
}
console.log(`\n${files.length} files checked in ${((Date.now() - started) / 1000).toFixed(1)}s, ${failed} with errors`);
process.exit(failed ? 1 : 0);
