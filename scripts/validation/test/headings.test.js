import { validateDuplicatedOpeningHeading, validateHeadingsNesting, validateMaxLength, validateOpeningHeadingLevel, validateTitleCase } from '../validations/headings.js'
import { Article } from '../domain/article.js'

const content = 
`---
title: Incorrect Intro Level
---

### Incorrect Intro Level

If the intro is the first section it should be a H2 title.

## Conclusion

This is the conclusion.

#### This Is a Forbidden Nesting

# This Is Title Case
# This is not title case

# This Is a Very Very Very Long Title`;

const article = new Article();
article.rawData = content;

test('Test if forbidden H2 > H4 nesting is detected', () => {
    const errors = validateHeadingsNesting(article);
    // console.log(errors);
    expect(errors.length).toBe(1);
    expect(errors[0].lineNumber).toBe(13);
    expect(errors[0].column).toBe(1);
});

test('Test if forbidden opening heading level is detected', () => {
    const errors = validateOpeningHeadingLevel(article);
    // console.log(errors);
    expect(errors.length).toBe(1);
    expect(errors[0].lineNumber).toBe(5);
    expect(errors[0].column).toBe(1);
});

test('Test if missing title case is detected', () => {
    const errors = validateTitleCase(article);
    console.log(errors);
    expect(errors.length).toBe(1);
    expect(errors[0].lineNumber).toBe(16);
    expect(errors[0].column).toBe(1);
});

test('Test if too long titles are detected', () => {
    const errors = validateMaxLength(article, 30);
    console.log(errors);
    expect(errors.length).toBe(1);
    expect(errors[0].lineNumber).toBe(18);
    expect(errors[0].column).toBe(1);
});

test('Test if duplicated opening titles are detected', () => {
    const errors = validateDuplicatedOpeningHeading(article);
    console.log(errors);
    expect(errors.length).toBe(1);
    expect(errors[0].lineNumber).toBe(5);
    expect(errors[0].column).toBe(1);
});