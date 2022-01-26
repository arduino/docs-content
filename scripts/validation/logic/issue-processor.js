import { ValidationIssue } from '../domain/validation-issue.js';

export class IssueProcessor {
    processIssues(validationIssues) {

        if (validationIssues.length == 0) {
            console.log("✅ No issues found.")
            process.exit(0);
        }

        let validationIssueErrors = 0;
        let validationWarnings = 0;

        for (let issue of validationIssues) {
            if (issue.type == ValidationIssue.Type.ERROR) {
                ++validationIssueErrors;
            } else {
                ++validationWarnings;
            }
            const symbol = issue.type == ValidationIssue.Type.ERROR ? "❌ ERROR" : "😬 WARNING";
            const lineNumber = issue.lineNumber ? ":" + issue.lineNumber : ":1"; //Default line number is 1
            const column = issue.column ? ":" + issue.column : "";
            console.log(`${symbol}: ${issue.message} Location: ${issue.file}${lineNumber}${column}`);
        }

        if (validationWarnings > 0)
            console.log("😬 " + validationWarnings + " warnings found.")
        if (validationIssueErrors > 0)
            console.log("🚫 " + validationIssueErrors + " errors found.")
        process.exit(validationIssueErrors > 0 ? 2 : 0);
    }

}