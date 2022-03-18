import { ValidationIssue } from '../domain/validation-issue.js';
import { getLineNumberFromIndex, getColumnFromIndex, isFile} from '../../lib/file-helper.cjs';
import { readFileSync, existsSync } from 'fs';
import { basename } from 'path';
import _ from 'node-html-parser';
const { parse } = _;

function validateImageDescriptions(article, imageCaptionMinWords){
    let errorsOccurred = [];
    const rawData = article.rawData;
    if(!rawData) return errorsOccurred;
    const regex = new RegExp(/!\[(?<caption>[^\]]*)\]\((?<filename>.*?)(?=\"|\))(?<optionalpart>\".*\")?\)/, "g");
    const matches = [...rawData.matchAll(regex)];

    for(let match of matches){
        const imageDescription = match.groups.caption;
        if(imageDescription.split(" ").length < imageCaptionMinWords){
            const lineNumber = getLineNumberFromIndex(match.index, rawData); 
            const column = getColumnFromIndex(match.index,rawData);
            const errorMessage = "Image doesn't have a (proper) description: " + match.groups.filename;
            errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath, ValidationIssue.Type.ERROR, lineNumber, column));  
        }
    }
    return errorsOccurred;
}

function validateImagePaths(article){
    let errorsOccurred = [];
    article.referencedAssetsPaths.forEach(imagePath => {
        if(imagePath.startsWith("/") || imagePath.startsWith("~")){
           const errorMessage = "Image uses an absolute path: " + imagePath;
           const content = article.rawData;
           const index = content.indexOf(imagePath);
           const lineNumber = getLineNumberFromIndex(index, content);
           const column = getColumnFromIndex(index, content);
           errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath, ValidationIssue.Type.ERROR, lineNumber, column));               
        } else if(!imagePath.startsWith("http") && (!existsSync(`${article.path}/${imagePath}`) || !isFile(`${article.path}/${imagePath}`))){
            const errorMessage = "Image doesn't exist: " + imagePath;
            const content = article.rawData;
            const index = content.indexOf(imagePath);
            const lineNumber = getLineNumberFromIndex(content.indexOf(imagePath), content);
            const column = getColumnFromIndex(index, content);
            errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath, ValidationIssue.Type.ERROR, lineNumber, column));
        }
    });
    return errorsOccurred;
}

function validateReferencedAssets(article){
    let errorsOccurred = [];
    let imageNames = article.referencedAssetsPaths.map(imagePath => basename(imagePath));    
    let assetNames = article.assets.map(asset => basename(asset));    
    let linkNames = article.links.map(link => basename(link));     
    let coverImagePath = article.metadata?.coverImage;   
    let coverImageName = coverImagePath ? basename(coverImagePath) : null;

    assetNames.forEach(asset => {        
        if(coverImageName == asset) return;
        if(!imageNames.includes(asset) && !linkNames.includes(asset)){ 
           const errorMessage = `Asset '${asset}' is not used.`;
           errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath));                       
        }
    });
    return errorsOccurred;
}

function validateSVGFiles(article){
    let errorsOccurred = [];
    let svgFiles = article.svgAssets;
    if(svgFiles === undefined || svgFiles.length == 0) return errorsOccurred;
    svgFiles.forEach(path => {     
       const rawData = readFileSync(path);
       if(rawData.includes("<image ")){
           const htmlDoc = parse(rawData);
           let image = htmlDoc.querySelector("image")
           // Detect if there are embedded images that are actually rendered
           if(image.attributes.width || image.attributes.height){
                const errorMessage = path + " contains embedded binary images.";
                errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath, ValidationIssue.Type.WARNING));                    
           }
       }
    });
    return errorsOccurred;
}

export { validateImageDescriptions, validateImagePaths, validateReferencedAssets, validateSVGFiles }