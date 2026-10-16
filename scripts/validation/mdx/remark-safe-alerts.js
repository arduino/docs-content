// Copy of remark-safe-alerts.js in arduino/docs.arduino.cc, which the build runs on every page: keep the two in sync
/* eslint-env node */

// Wraps an <Alert> body in a string literal when it would not parse as JSX, so a `<model>` cannot fail the build
// The body still renders as markdown: string children land on the marked branch of Alert.tsx rather than being parsed by MDX

// Components whose body is authored as plain markdown text rather than JSX children
const TEXT_COMPONENTS = ['Alert'];

const OPENING_TAG = new RegExp(`^<(${TEXT_COMPONENTS.join('|')})((?:[^>"']|"[^"]*"|'[^']*')*)>`);

let parseExpression;
try {
  parseExpression = require('@babel/parser').parseExpression;
} catch (error) {
  // Without a parser we cannot tell broken alerts from valid ones, so we leave them alone
  parseExpression = null;
}

const parsesAsJsx = (source) => {
  try {
    parseExpression(source, { plugins: ['jsx'] });
    return true;
  } catch (error) {
    return false;
  }
};

// Returns a parseable version of a jsx node value, or null when there is nothing to fix
const safeValue = (value) => {
  const opening = value.match(OPENING_TAG);
  if (!opening) return null;

  const [tag, name] = opening;
  const closing = `</${name}>`;
  let body = value.slice(tag.length);

  // The closing tag can carry trailing whitespace, and is absent when the alert closes further down
  const suffix = body.match(new RegExp(`${closing}\\s*$`));
  if (suffix) body = body.slice(0, -suffix[0].length);

  // An alert opened on its own line already has its body parsed as markdown
  if (!body.trim()) return null;

  // More than one alert on the same line: leave the whole node alone rather than guess
  if (body.includes(closing) || new RegExp(`<${name}\\b`).test(body)) return null;

  // Alerts wrapping valid JSX keep the children they have today
  if (parsesAsJsx(`${tag}${body}${closing}`)) return null;

  const escaped = `${tag}{${JSON.stringify(body)}}`;
  return parsesAsJsx(`${escaped}${closing}`) ? `${escaped}${suffix ? suffix[0] : ''}` : null;
};

const visitJsx = (node) => {
  if (node.type === 'jsx' && typeof node.value === 'string') {
    const value = safeValue(node.value);
    if (value) node.value = value;
  }
  if (node.children) node.children.forEach(visitJsx);
};

module.exports = function remarkSafeAlerts() {
  return (tree) => {
    if (parseExpression) visitJsx(tree);
  };
};
