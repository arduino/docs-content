function replaceRange(indexFrom, indexTo, haystack, replacement) {
    let start = haystack.substring(0, indexFrom);
    let end = haystack.substring(indexTo);
    return start + replacement + end;
};

function replaceItalicEmphasisWithBoldEmphasis(article){
    let contentBackup = article.rawData;

    while(article.emphasizedTextData.some((element) => element.type == "italic")){
        for(let data of article.emphasizedTextData){
            if(data.type == "italic"){
                let newData = replaceRange(data.beginIndex, data.endIndex, article.rawData, `**${data.text}**`)
                console.log(`🔧 Replacing italic styling of '${data.text}' in ${article.contentFilePath}`);
                article.rawData = newData;
                break;
            }
        }
    }    
    const hasChanged = article.rawData != contentBackup;    
    return hasChanged && article.writeContentToFile();
}

export { replaceItalicEmphasisWithBoldEmphasis }