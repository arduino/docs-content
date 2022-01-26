import markdownLinkCheck from 'markdown-link-check';
import { ValidationIssue } from '../domain/validation-issue.js';

async function validateBrokenLinks(article, brokenLinkExcludePatterns, baseURL, verbose = false){
    return new Promise(function(resolve){
        const markdownContent = article.markdown;
        if(!markdownContent) return;
        const ignorePatterns = brokenLinkExcludePatterns?.map((ignorePattern) => {
            return {pattern : ignorePattern}
        });
        const linkCheckOptions = { 
            ignorePatterns: ignorePatterns,
            baseUrl: baseURL,
            projectBaseUrl: baseURL,
            replacementPatterns:[
            {
                "pattern": "^/",
                "replacement": "{{BASEURL}}/"
            }
        ]};
        try {
            markdownLinkCheck(markdownContent, linkCheckOptions, function (err, results) {                
                if (err) {
                    console.error('Error', err);
                    return;
                }
                let errorsOccurred = [];
                results.forEach(function (result) {    
                    if(result.status == "alive" && verbose){
                        console.log(`👍 ${result.link} is alive`);
                    } else if(result.status == "dead" && result.statusCode !== 0){
                        const errorMessage = `${result.link} is dead 💀 HTTP ${result.statusCode}`;
                        errorsOccurred.push(new ValidationIssue(errorMessage, article.contentFilePath));                        
                    }
                });
                resolve(errorsOccurred);
            });
        } catch (error) {
            console.log(`❌ ERROR: Error occurred while checking the links in ${article.contentFilePath}`, error.message);
        }
    });
}

export { validateBrokenLinks }