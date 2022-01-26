import { titleCase } from 'title-case';

function fixMissingTitleCase(article){
    let content = article.rawData;
    const articleTitle = article.metadata.title;

    if(articleTitle && articleTitle != titleCase(articleTitle)){
        content = content.replace(articleTitle, titleCase(articleTitle));
    }

    if(article.headingsData){
        for(let headingData of article.headingsData){
            const heading = headingData.content;
            const titleCaseHeading = titleCase(heading);
    
            if(heading != titleCaseHeading){
                const hashes = "#".repeat(headingData.level);
                const fixedHeading = `${hashes} ${titleCaseHeading}`
                content = content.replace(headingData.rawData, fixedHeading);
            }        
        }
    }
    const hasChanged = article.rawData != content;
    article.rawData = content;
    return hasChanged && article.writeContentToFile();
}

export { fixMissingTitleCase };