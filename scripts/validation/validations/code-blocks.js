import { ValidationIssue } from '../domain/validation-issue.js';
import { getLineNumberFromIndex, getColumnFromIndex} from '../../lib/file-helper.cjs';

function validateSyntaxSpecifiers(article, allowedSyntaxSpecifiers){
    let errorsOccurred = [];
    if(!article.codeBlockData) return errorsOccurred;
    
    for (let codeBlock of article.codeBlockData) {
        let syntax = codeBlock.language;
        if (syntax && !allowedSyntaxSpecifiers.includes(syntax)) {
            let rawContent = article.rawData;
            const lineNumber = getLineNumberFromIndex(codeBlock.beginIndex, rawContent);
            const column = getColumnFromIndex(codeBlock.beginIndex, rawContent);
            const errorMessage = `Code block uses unsupported syntax: '${syntax}'`;
            const issueType = ValidationIssue.Type.ERROR;
            errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath,issueType, lineNumber, column));
        }
    };
    return errorsOccurred;
}

export { validateSyntaxSpecifiers }