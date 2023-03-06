import { fixMissingTitleCase } from 'content-lint';
import { ConfigManager } from 'content-lint';
import { ArticleManager } from 'content-lint';
import { fixUnusedAssets } from 'content-lint';
import { replaceItalicEmphasisWithBoldEmphasis } from 'content-lint';

const configManager = new ConfigManager();
configManager.addConfigFile("generic", "./config/config-generic.yml");
configManager.addConfigFile("tutorials", "./config/config-tutorials.yml");
configManager.addConfigFile("datasheets", "./config/config-datasheets.yml");

const articleManager = new ArticleManager(configManager.options.path, configManager.getConfig("generic").excludePatterns);
const tutorials = articleManager.getArticles(configManager.getConfig("tutorials").searchPatterns);
const datasheets = articleManager.getArticles(configManager.getConfig("datasheets").searchPatterns);
const allArticles = [...tutorials, ...datasheets];

if(!allArticles || allArticles.length == 0){
    console.log("❌ ERROR: No articles found.")
    process.exit(-1);
}

for(let article of allArticles){
    if(fixMissingTitleCase(article)){
        console.log(`✅ Fixed missing Title Case headings in '${article.contentFilePath}'.`);
    }

    if(fixUnusedAssets(article)){
        console.log(`✅ Fixed unused assets in '${article.contentFilePath}'.`);
    }
    
    if(replaceItalicEmphasisWithBoldEmphasis(article)){
        console.log(`✅ Fixed italic styling in '${article.contentFilePath}'.`);
    }

}