import { findAllFiles } from '../../lib/file-helper.cjs';
import { Article } from '../domain/article.js';
import fs from 'fs';
import slash from 'slash';

export class ArticleManager {
    constructor(basePath, excludePatterns) {
        this.basePath = basePath;        
        var fileStat = fs.lstatSync(basePath);

        if(fileStat.isDirectory()){
            this.allMarkdownFiles = findAllFiles(basePath, ".md", excludePatterns, false);
        } else{
            this.allMarkdownFiles = [basePath];
        }
    }

    getFilteredPaths(searchPattern) {
        return this.allMarkdownFiles.filter(markdownFilePath => {
            return slash(markdownFilePath).includes(searchPattern)
        });
    }

    getArticles(searchPatterns){
        let articlePaths = [];
        for(let pattern of searchPatterns){
            articlePaths = articlePaths.concat(this.getFilteredPaths(pattern));
        }
        return articlePaths.map(articlePath => new Article(articlePath));
    }    
}