import { validate } from 'jsonschema';
import { readFileSync } from 'fs';
import { ValidationIssue } from '../domain/validation-issue.js';

function validateMetaData(article, schemaPath) {    
    let errorsOccurred = [];

    let metadata = article.metadata;
    if(!metadata) {
        const errorMessage = "No metadata found";
        errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath));            
        return errorsOccurred;
    }

    try {        
        let jsonSchema = JSON.parse(readFileSync(schemaPath));        
        let validationResult = validate(metadata, jsonSchema);
        for(let error of validationResult.errors){
            const errorMessage = `An error occurred while validating the metadata: ${error.property} - ${error.message}`;
            errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath));                
        }

    } catch (error) {
        const errorMessage = "An error occurred while parsing the metadata: " + error.toString();
        errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath));                       
    }
    
    return errorsOccurred;
}

export { validateMetaData }