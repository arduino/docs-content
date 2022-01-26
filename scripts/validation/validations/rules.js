import { load } from 'js-yaml';
import { readFileSync } from 'fs';
import { ValidationIssue } from '../domain/validation-issue.js';
import { getLineNumberFromIndex, getColumnFromIndex} from '../../lib/file-helper.cjs';

/**
 * Validates rules in an article based on regex patterns defined in a rule file.
 * @param {*} article An Article object that shall be validated.
 * @param {*} rulesFilePath The path to the yml file containing the rules.
 * @param {*} debug A boolean indicating if debug messages shoudl be printed.
 * @returns An array of ValidationIssue objects.
 */
function validateRules(article, rulesFilePath, debug) {
    const debugPrint = (message) => {
        if(debug) console.log(message)
    }

    let errorsOccurred = [];
    if(!article.contentFilePath) return errorsOccurred;
    let htmlContent = article.rawHTML;
    let rawContent = article.rawData;
    let rules = [];

    try {
        rules = load(readFileSync(rulesFilePath, 'utf8'));
    } catch (e) {
        console.log(e);
        return errorsOccurred;
    }
    
    for(let rule of rules) {
        debugPrint(`🕵️ Validating rule ${rule.regex} for ${article.contentFilePath}`)
        const content = rule.format == "html" ? htmlContent : rawContent;
        if(!content || content.length == 0){
            console.log("💣 File content couldn't be read:", article.contentFilePath);
            continue;
        }
        const modifiers = rules.regexModifiers ?? "gm"
        const regex = new RegExp(rule.regex, modifiers);
        const matches = [...content.matchAll(regex)];
        const ruleType = rule.type == "warning" ? ValidationIssue.Type.WARNING : ValidationIssue.Type.ERROR;

        if(matches.length == 0 && rule.shouldMatch){
            const errorMessage = rule.errorMessage;
            errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath, ruleType));
        } else {
            debugPrint(`👍 Passed rule ${rule.regex} for ${article.contentFilePath}`)
        }

        for(let currentMatch of matches){
            const index = currentMatch.index;
            if(!rule.includeCodeBlocks && article.isInsideCodeBlock(index))
                continue;
            // Line number only makes sense for rules that operate on the source markdown file
            const lineNumber = rule.format == "markdown" ? getLineNumberFromIndex(index,content) : undefined;
            const column = rule.format == "markdown" ? getColumnFromIndex(index,content) : undefined;

            if(!rule.shouldMatch) {
                const errorMessage = rule.errorMessage;
                errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath, ruleType, lineNumber, column));
            } else {
                debugPrint(`👍 Passed rule ${rule.regex} for ${article.contentFilePath}`)
            }
        }

    };
    return errorsOccurred;
}

export { validateRules }