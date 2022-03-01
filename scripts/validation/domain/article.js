import fileHelper from '../../lib/file-helper.cjs';
import { existsSync, readFileSync, writeFileSync } from 'fs';
import fm from 'front-matter';
import marked from 'marked';
import _ from 'node-html-parser';
const { parse } = _;
import { decode } from 'html-entities';
import * as path from 'path';

export class Article {
    constructor(contentFilePath){
        this.contentFilePath = contentFilePath;
    }

    clearData(){
        this._html = null;
        this._markdown = null;
        this._metaData = null;
        this._codeBlockData = null;
        this._referencedAssetsPaths = null;
    }

    get path(){
        if(this._basePath) return this._basePath;
        this._basePath = this._contentFilePath ? path.dirname(this._contentFilePath) : null;
        return this._basePath;
    }

    set path(basePath){
        this._basePath = basePath;
        this._assetsPath = null; // Reset cached value
    }

    get contentFilePath(){
        if(this._contentFilePath) return this._contentFilePath;
        if(!this.path) return null;

        const files = fileHelper.getFilesWithExtension(this.path, "md");
        if(files.length > 1){
            console.log("😬 WARNING: More than one markdown file in directory. Location:", this.path);
        }
        if(files.length == 0) {
            console.log("😬 WARNING: No markdown file in directory. Location:", this.path);
            return null;
        }
        this._contentFilePath = `${this.path}/${files[0]}`;
        return this._contentFilePath;
    }

    set contentFilePath(path){
        this._contentFilePath = path;
    }

    set rawData(data){
        this._rawData = data;
        this.clearData();
    }

    get rawData(){
        if(this._rawData) return this._rawData;

        if(!this.contentFilePath || !existsSync(this.contentFilePath)){
            return null;
        }
        this._rawData = readFileSync(this.contentFilePath).toString();
        return this._rawData;
    }

    get markdown(){
        if(this._markdown) return this._markdown;
        if(!this.rawData){
            return null;
        }        
        const content = fm(this.rawData);
        this._markdown = content.body;
        return this._markdown;
    }

    get rawHTML(){
        const markdown = this.markdown
        return markdown ? marked(markdown) : null;
    }

    get html(){
        if(this._html) return this._html;
        this._html = parse(this.rawHTML, {
			blockTextElements: {
				script: true,
				noscript: true,
				style: true,                
                code: false
            }
        });
        return this._html;
    }

    get imageNodes(){
        return this.html.querySelectorAll("img"); 
    }

    get codeNodes(){
        return this.html.querySelectorAll("pre code");
    }

    get headings(){
        const maxHeadingLevel = 6;
        let headings = [];
        for(let i = 1; i <= maxHeadingLevel; ++i) {
            let currentHeadings = this.html.querySelectorAll("h" + i);
            headings = headings.concat(currentHeadings.map(heading => decode(heading.innerText)));            
        }
        return headings;
    }

    /**
     * Checks if the character at the given index is inside a code block
     * of the markdown file.
     * @param {*} characterIndex 
     * @returns a boolean indicating if the index is withing a code block.
     */
    isInsideCodeBlock(characterIndex){
        const codeBlocks = this.codeBlockData;
        for(let codeBlock of codeBlocks){
            if(characterIndex >= codeBlock.beginIndex && characterIndex <= codeBlock.endIndex)
                return true;
        }
        return false;
    }

    /**
     * Returns an array containing code blocks data objects in the format:
     * {language : 'cpp', code: 'void main(){}', beginIndex: 82, endIndex: 102 }
     */
    get codeBlockData(){
        if(this._codeBlockData) return this._codeBlockData;
        if(!this.rawData) return null;
        const regex = new RegExp(/`{3}(?<lang>[\w]*)(?:\s*)\r?\n(?<code>[\S\s]+?)\r?\n`{3}/, "gm");
        const matches = [...this.rawData.matchAll(regex)];
        let data = new Array();

        for(let match of matches){            
            const language = match.groups.lang;
            const code = match.groups.code;
            data.push({language : language, code: code, beginIndex: match.index, endIndex: match.index + match[0].length - 1 })
        }
        this._codeBlockData = data;
        return this._codeBlockData;
    }

    /**
     * Returns an array containing headings data objects in the format:
     * { content: 'Conclusion', level: 2, location: 89 }
     */
    get headingsData(){
        if(!this.rawData) return null;
        const regex = new RegExp(/^(?<level>#{1,6})\s+(?<content>.*)$/, "gm");
        const matches = [...this.rawData.matchAll(regex)];
        let data = new Array();

        // Filter out false positives such as python comments with a leading hash tag
        // FIXME: Instead use 'remark' to get the headings along with their token index
        const headingsFromParser = this.headings;
        const filteredMatches = matches.filter((match) => {
            // Parser transforms tabs to four spaces so we need to replicate this here.
            let matchedHeading = match.groups.content.replace(/\t/g, '    ');
            // Parser trims title so we need to replicate this here
            matchedHeading = matchedHeading.trim();
            return headingsFromParser.includes(matchedHeading);
        });

        for(let match of filteredMatches){            
            const level = match.groups.level.length;
            const rawData = match[0];
            data.push({content : match.groups.content, level: level, location: match.index, rawData: rawData })
        }
        return data.length == 0 ? null : data;
    }       

    /**
     * Returns a list of all asset file paths that are not referenced in an article
     */
    get unreferencedAssetsPaths(){
        const referencedAssetNames = this.referencedAssetsPaths.map(assetPath => path.basename(assetPath));    
        return this.assets.filter((filePath) => { return !referencedAssetNames.includes(path.basename(filePath)); });
    }

    /**
     * Returns an array of all images and video files referenced
     * in the article including its meta data.
     */
    get referencedAssetsPaths(){
        if(this._referencedAssetsPaths) return this._referencedAssetsPaths;
        const images = this.html.querySelectorAll("img");
        const imagePaths = images.map(image => image.attributes.src);

        const pathRegex = new RegExp(`^(?!http).*(${this.assetsFolder})\/.*(?:\..{1,4})$`);
        const filteredFilePaths = this.links.filter((link) => link.match(pathRegex));      

        const videos = this.html.querySelectorAll("video source");
        const videoPaths = videos.map(video => video.attributes.src);
        
        const allPaths = imagePaths.concat(videoPaths).concat(filteredFilePaths);
        let coverImagePath = this.metadata?.coverImage;   
        if(coverImagePath) allPaths.push(coverImagePath);
        this._referencedAssetsPaths = allPaths;
        return this._referencedAssetsPaths;
    }

    /**
     * Returns all hyperlinks in the document
     */
    get links(){
        let links = this.html.querySelectorAll("a");
        return links.map(link => link.attributes.href);
    }


    get assetsFolder(){
        if(this._assetFolder) return this._assetFolder;
        const validDirectories = ["assets", "images"];

        if (existsSync(`${this.path}/${validDirectories[0]}/`)){
            this._assetFolder = validDirectories[0];
            return this._assetFolder;
        }
        if (existsSync(`${this.path}/${validDirectories[1]}/`)){
            console.log("😬 WARNING: Using deprecated 'images' directory to store assets. Location:", path);
            this._assetFolder = validDirectories[1];
            return this._assetFolder;
        }
        console.log(`😬 WARNING: No standard assets directory (${validDirectories.join(" | ")}) found in: ${this.path}`);
        return null;
    }

    /**
     * Returns the assets path if it's one of the standard ones 'assets' or 'images', null otherwise.
     */
    get assetsPath(){
        if(this._assetsPath) return this._assetsPath;
        if(!this.assetsFolder) return null;
        this._assetsPath = `${this.path}/${this.assetsFolder}/`;
        return this._assetsPath;
    }

    /**
     * Returns a list of file paths in the assets folder based on the basePath property
     */
    get assets(){
        if(!this.assetsPath) return [];
        let files = fileHelper.findAllFiles(this.assetsPath, null, [".DS_Store"]);
        return files ? files.map(file => file.split("?")[0]) : [];
    }

    get metadata(){
        if(this._metaData) return this._metaData;
        if(!this.rawData) return null;
        try {            
            const content = fm(this.rawData);
            this._metaData = content.attributes;
            return this._metaData;
        } catch (error) {
            console.log("💣 Error occurred while parsing", this.contentFilePath);
            console.log(error);
            return null;
        }
    }

    get svgAssets(){
        if(!this.assetsPath) return [];
        return fileHelper.findAllFiles(this.assetsPath, '.svg');
    }

    /**
     * Writes the content contained in the rawData property to the specified file.
     * @param {*} filename the filename to which the data should be written.
     * Defaults to the `contentFilePath` property.
     */
    writeContentToFile(filename = null){
        let targetPath;
        
        if(filename){
            const maybeSlash = this.basePath.endsWith("/") ? "" : "/";
            targetPath = `${this.basePath}${maybeSlash}${filename}`;
        } else {
            targetPath = this.contentFilePath;
        }

        try {
            writeFileSync(targetPath, this.rawData);
            return true;
        } catch (error) {
            return false;
        }
    }
}