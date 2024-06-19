import { Validator } from 'content-lint';
import { ArticleManager } from 'content-lint';

import { validateDuplicatedOpeningHeading, validateHeadingsNesting, validateMaxLength, validateNumberedHeadings, validateOpeningHeadingLevel, validateSpacing, validateTitleCase } from 'content-lint'
import { validateMetaData } from 'content-lint';
import { validateRules } from 'content-lint';
import { validateImageDescriptions, validateImagePaths, validateReferencedAssets, validateSVGFiles } from 'content-lint';
import { validateSyntaxSpecifiers } from 'content-lint';
import { validateNestedLists } from 'content-lint';
import { validateBrokenLinks } from 'content-lint';
import { validateFolderName } from 'content-lint';
import { ConfigManager } from 'content-lint';

const configManager = new ConfigManager();
configManager.addConfigFile("generic", "./config/config-generic.yml");
configManager.addConfigFile("tutorials", "./config/config-tutorials.yml");
configManager.addConfigFile("datasheets", "./config/config-datasheets.yml");

const validator = new Validator();
const articleManager = new ArticleManager(configManager.options.path, configManager.getConfig("generic").excludePatterns);
const tutorials = articleManager.getArticles(configManager.getConfig("tutorials").searchPatterns);
const datasheets = articleManager.getArticles(configManager.getConfig("datasheets").searchPatterns);
const allArticles = [...tutorials, ...datasheets];

if(!allArticles || allArticles.length == 0){
    console.error("❌ ERROR: No articles found.")
    process.exit(-1);
}

// Verify that all meta data is valid JSON and contains the correct attributes
if(configManager.getConfig("generic").validateMetadata){
    validator.addValidation(tutorials, validateMetaData, configManager.getConfig("tutorials").metadataSchema);
    validator.addValidation(datasheets, validateMetaData, configManager.getConfig("datasheets").metadataSchema);
}

// Verifies that the titles are in the correct format
validator.addValidation(datasheets, validateNumberedHeadings);
validator.addValidation(allArticles, validateTitleCase);
validator.addValidation(allArticles, validateSpacing);
validator.addValidation(allArticles, validateMaxLength, configManager.getConfig("generic").headingMaxLength);

// Verifies that the article titles are not duplicated
validator.addValidation(tutorials, validateDuplicatedOpeningHeading);

// Validates the nesting of the headings
validator.addValidation(allArticles, validateHeadingsNesting);

// Verifies if the tutorials start with H2
validator.addValidation(tutorials, validateOpeningHeadingLevel, configManager.getConfig("tutorials").openingHeadingLevel);

// Verify that SVG images don't contain embedded images
validator.addValidation(allArticles, validateSVGFiles);

// Verify that there are no broken links
if(configManager.options.checkBrokenLinks){
    validator.addValidation(allArticles, validateBrokenLinks, configManager.getConfig("generic").brokenLinkExcludePatterns, configManager.getConfig("generic").baseURL, configManager.options.verbose);
};

// Verify if articles contain discouraged foldernames (which translate into URLs)
validator.addValidation(allArticles, validateFolderName, configManager.getConfig("generic").folderNameIgnoreList);

// Verify that all files in the assets folder are referenced
validator.addValidation(allArticles, validateReferencedAssets);

// Verify that the images exist and don't have an absolute path
validator.addValidation(allArticles, validateImagePaths);

// Ensures no nested lists are used
if(!configManager.getConfig("tutorials").allowNestedLists){
    validator.addValidation(tutorials, validateNestedLists);
};

// Verify that the images contain a description
validator.addValidation(tutorials, validateImageDescriptions, configManager.getConfig("generic").imageCaptionMinWords);

// Verify that only allowed syntax specifiers are used
if (configManager.getConfig("tutorials").validateSyntaxSpecifiers){
    validator.addValidation(tutorials, validateSyntaxSpecifiers, configManager.getConfig("generic").allowedSyntaxSpecifiers);        
}

// Verifies that the content rules are met
for(let validationRuleFile of configManager.getConfig("tutorials").validationRuleFiles){
     validator.addValidation(tutorials, validateRules, validationRuleFile, configManager.options.debug);
}

// Check if an error occurred and exit with the corresponding status code
validator.run();
