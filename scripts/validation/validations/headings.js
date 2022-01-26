import { ValidationIssue } from '../domain/validation-issue.js';
import { getLineNumberFromIndex, getColumnFromIndex} from '../../lib/file-helper.cjs';
import { titleCase } from 'title-case';

/**
 * Checks if the article starts with the expected heading.
 * @param {*} article An object of type Article
 * @param {*} expectedLevel The expected opening heading level.
 * The default is 2 assuming H1 is defined in the frontmatter of an article.
 * @returns an array containing the validation errors
 */
function validateOpeningHeadingLevel(article, expectedLevel = 2){
    let errorsOccurred = [];
    if(!article.headingsData) return errorsOccurred;
    const firstHeading = article.headingsData[0];

    if(firstHeading.level != expectedLevel){
        const content = article.rawData;
        const path = article.contentFilePath;

        const message = `Using forbidden level in opening heading '${firstHeading.content}': H${firstHeading.level} instead of H${expectedLevel}`;
        const lineNumber = getLineNumberFromIndex(firstHeading.location, content);
        const column = getColumnFromIndex(firstHeading.location, content);
        const issueType = ValidationIssue.Type.WARNING;
        errorsOccurred.push(new ValidationIssue(message, path, issueType, lineNumber, column));
    }
    return errorsOccurred;
}

/**
 * Checks if the article has the same title in the metadata
 * and the opening heading.
 * @param {*} article An object of type Article
 * @returns an array containing the validation errors
 */
function validateDuplicatedOpeningHeading(article){
    let errorsOccurred = [];
    if(!article.headingsData) return errorsOccurred;
    const firstHeading = article.headingsData[0];
    const firstHeadingContent = firstHeading.content.trim();
    const headingFromFrontmatter = article.metadata?.title?.trim();
    if(!headingFromFrontmatter) return errorsOccurred;

    if(firstHeadingContent == headingFromFrontmatter){
        const content = article.rawData;
        const path = article.contentFilePath;
        const message = `Using duplicated heading in metadata and content '${firstHeading.content}'`;
        const lineNumber = getLineNumberFromIndex(firstHeading.location, content);
        const column = getColumnFromIndex(firstHeading.location, content);
        const issueType = ValidationIssue.Type.ERROR;
        errorsOccurred.push(new ValidationIssue(message, path, issueType, lineNumber, column));
    }
    return errorsOccurred;
}

/**
 * Validates if the headings are nested correctly.
 * Heading levels cannot be skipped e.g. H2 > H4 is forbidden
 * @param {*} article An object of type Article
 * @returns an array containing the validation errors
 */
function validateHeadingsNesting(article){
    let errorsOccurred = [];
    if(!article.headingsData) return errorsOccurred;
    let previousHeading = null;

    for(let heading of article.headingsData){
        // Same level or shallower are allowed
        if(previousHeading && heading.level > previousHeading.level){
            // Report error if nesting levels are skipped
            if(heading.level != previousHeading.level + 1){
                const content = article.rawData;
                const path = article.contentFilePath;

                const message = `Incorrect nesting of heading ${previousHeading.level} ${previousHeading.content} H${heading.level} '${heading.content}'`;
                const lineNumber = getLineNumberFromIndex(heading.location, content);
                const column = getColumnFromIndex(heading.location, content);
                const issueType = ValidationIssue.Type.ERROR;
                errorsOccurred.push(new ValidationIssue(message, path, issueType, lineNumber, column));
            }
        }
        previousHeading = heading;
    }
    return errorsOccurred;
}

/**
 * Validates if headings are in title case
 * @param {*} article An object of type Article
 * @returns an array containing the validation errors
 */
function validateTitleCase(article){
    let errorsOccurred = [];
    if(!article.headingsData) return errorsOccurred;
    const content = article.rawData;
    const path = article.contentFilePath;
    const articleTitle = article.metadata.title;

    if(articleTitle && articleTitle != titleCase(articleTitle)){
        const message = `'${articleTitle}' is not title case.`;
        errorsOccurred.push(new ValidationIssue(message, path));
    }

    for(let headingData of article.headingsData){
        const heading = headingData.content;

        if(heading != titleCase(heading)){
            const message = `'${heading}' is not title case.`;
            const lineNumber = getLineNumberFromIndex(headingData.location, content);
            const column = getColumnFromIndex(headingData.location, content);
            const issueType = ValidationIssue.Type.ERROR;
            errorsOccurred.push(new ValidationIssue(message, path, issueType, lineNumber, column));
        }        
    }
    return errorsOccurred;
}

/**
 * Validates if a heading exceeds the allowed length limit.
 * @param {*} article An object of type Article
 * @param {*} maxLength the maximum allowed length of a heading
 * @returns 
 */
function validateMaxLength(article, maxLength){
    let errorsOccurred = [];
    if(!article.headingsData) return errorsOccurred;

    for(let headingData of article.headingsData){
        const heading = headingData.content;

        if(heading.length > maxLength){
            const content = article.rawData;
            const path = article.contentFilePath;
            const message = `${heading}' (${heading.length}) exceeds the max length (${maxLength})`;
            const lineNumber = getLineNumberFromIndex(headingData.location, content);
            const column = getColumnFromIndex(headingData.location, content);
            const issueType = ValidationIssue.Type.WARNING;
            errorsOccurred.push(new ValidationIssue(message, path, issueType, lineNumber, column));              
        }
    }
    return errorsOccurred;
}

/**
 * Validates if the headings contain any spurious (doubles/tabs) spacings.
 * @param {Article} article 
 * @returns 
 */
function validateSpacing(article){
    let errorsOccurred = [];
    if(!article.headingsData) return errorsOccurred;

    for(let headingData of article.headingsData){
        const headingRaw = headingData.rawData;
        const content = article.rawData;
        const path = article.contentFilePath;
        const issueType = ValidationIssue.Type.ERROR;
        
        const doubleSpaceIndex = headingRaw.indexOf("  ");
        if(doubleSpaceIndex != -1){
            const message = `${headingRaw}' contains spurious spaces. Only single spaces are allowed.`;
            const lineNumber = getLineNumberFromIndex(headingData.location, content);
            const column = doubleSpaceIndex + 1;
            errorsOccurred.push(new ValidationIssue(message, path, issueType, lineNumber, column));              
        }

        const tabIndex = headingRaw.indexOf("\t");
        if(tabIndex != -1){
            const message = `${headingRaw}' contains spurious spaces. No tabulator indents are allowed.`;
            const lineNumber = getLineNumberFromIndex(headingData.location, content);
            const column = tabIndex + 1;
            errorsOccurred.push(new ValidationIssue(message, path, issueType, lineNumber, column));              
        }
    }
    return errorsOccurred;
}


function validateNumberedHeadings(article){
    let errorsOccurred = [];
    if(!article.headingsData) return errorsOccurred;

    for(let headingData of article.headingsData){
        const headingContent = headingData.content;
        const content = article.rawData;
        const path = article.contentFilePath;
        const issueType = ValidationIssue.Type.ERROR;

        const regex = new RegExp(/^((\d\.?)+) /);
        const match = headingContent.match(regex);

        if(match){
            const message = `Manual numbering is forbidden: ${headingContent}`;
            const lineNumber = getLineNumberFromIndex(headingData.location, content);
            const column = 1;
            errorsOccurred.push(new ValidationIssue(message, path, issueType, lineNumber, column));              
        }
        
    }
    return errorsOccurred;
}

export { validateHeadingsNesting, validateOpeningHeadingLevel, validateTitleCase, validateMaxLength, validateSpacing, validateDuplicatedOpeningHeading, validateNumberedHeadings };