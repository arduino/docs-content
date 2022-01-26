import { ValidationIssue } from '../domain/validation-issue.js';

function validateNestedLists(article) {
    let errorsOccurred = [];
    
    let nodes = article.html.querySelectorAll("li ul");
    if (nodes && nodes.length > 0) {
        const errorMessage = "Content uses nested lists";
        errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath));
    }
    return errorsOccurred;
}

export { validateNestedLists }