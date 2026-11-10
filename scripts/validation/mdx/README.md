# MDX Check

Compiles every page in `content/` with the same compiler that builds docs.arduino.cc: `@mdx-js/mdx` 1.6.22 followed by the Babel parser. A page that fails here would fail the deploy too.

It catches what the other checks let through, for example:

- Void tags that are never closed: `<br>` and `<img src="...">` instead of `<br/>` and `<img src="..."/>`.
- Tags closed in the wrong order, or never closed: `<b>text</strong>`, a `<td>` without `</td>`.
- HTML comments inside an HTML block, and `{ }` inside HTML, which MDX reads as JavaScript.

## Running it locally

From the repository root, with Node.js installed:

```bash
npm ci --prefix scripts/validation/mdx
node scripts/validation/mdx/mdx-check.js content
```

Pass a folder or a single file instead of `content` to check only that part.

## Output

For each page that does not compile, it prints the compiler error and the lines to fix:

```text
✖ content/hardware/pro/carriers/portenta-mid-carrier/datasheet/datasheet.md
  Unterminated JSX contents.
  line 91: <br> is never closed: write <br/>
```

The build reports the same error at the end of the generated code, which is why this check looks for the line in the page instead. In GitHub Actions each line also becomes an annotation on the pull request.

## Notes

- `.lintignore` is not honoured on purpose: the build compiles every page, ignored or not.
- `remark-safe-alerts.js` is a copy of the plugin with the same name in `arduino/docs.arduino.cc`, which the build runs on every page. Keep the two in sync.
- It checks that pages compile, not that they render. An error that only shows up at render time, like an undefined variable inside `{ }`, still needs a preview build.
