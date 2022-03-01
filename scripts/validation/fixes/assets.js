import fs from 'fs';

function fixUnusedAssets(article){
    const assets = article.unreferencedAssetsPaths;
    if(assets.length == 0) return false;

    for(let filePath of assets){
        try {
            console.log(`🔧 Deleting unused asset ${filePath}`);
            fs.unlinkSync(filePath)
        } catch (error) {
            console.error(`❌ Couldn't delete unused asset ${filePath}`);
            return false;
        }
    }    
    return true;
}

export { fixUnusedAssets };