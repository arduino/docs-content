const path = require('path');
const fs = require('fs');
const matcher = require('./matcher.cjs');

function isFile(path, followSymlinks = true){
    const stat = fs.lstatSync(path);
    if(stat.isFile()) return true;
    if(followSymlinks && stat.isSymbolicLink()){
        return fs.lstatSync(fs.realpathSync(path)).isFile();
    }
    return false;
}

function isDirectory(path, followSymlinks = true){
    const stat = fs.lstatSync(path);
    if(stat.isDirectory()) return true;
    if(followSymlinks && stat.isSymbolicLink()){
        try {
            const resolvedPath = fs.realpathSync(path);
            return fs.lstatSync(resolvedPath).isDirectory();            
        } catch (error) {
            console.error(error);
            return false;
        }
    }
    return false;
}

/**
 * Returns all subdirectories (non-recursive) of a given path
 * which don't match an exclude pattern
 * @param {String} startPath 
 * @param {String[]} excludePatterns
 * @param {boolean} followSymlinks Defines if symlinks should be considered
 * @returns a string array containing the full paths of the subdirectories
 */
function getSubdirectories(startPath, excludePatterns = [], followSymlinks = true){
    if (!fs.existsSync(startPath)) {        
        console.log("💣 Directory doesn't exist:", startPath);
        return;
    }

    var files = fs.readdirSync(startPath);
    let directories = [];
    files.forEach(file => {
        var fullPath = path.join(startPath, file);

        if (matcher.matchAny(fullPath, excludePatterns)) {            
            return;
        }

        if (isDirectory(fullPath, followSymlinks)) {
            directories.push(fullPath);
        }
    })
    return directories;    
}

/**
 * Returns all file names in a path (non-recursive) with a given file extension.
 * This function only returns the file names without path info.
 * @param {*} path 
 * @param {*} extension 
 * @returns a string array containing the file names
 */
function getFilesWithExtension(path, extension){
    return fs.readdirSync(path).filter(aFile => aFile.endsWith('.' + extension));
}


/**
 * Returns a list of file paths based on the start path
 * @param {*} startPath 
 * @param {*} searchPattern 
 * @param {*} excludePatterns
 * @param {boolean} followSymlinks Defines if symlinks should be considered
 * @param {*} matchingFiles 
 * @returns 
 */
function findAllFilesAndFolders(startPath, searchPattern = null, excludePatterns = [], followSymlinks = true, matchingFiles = []) {
    if(matcher.matchAny(startPath, excludePatterns)){
        // console.log("Excluding directory " + startPath);
        return matchingFiles;
    }
    
    // console.log('Starting from dir ' + startPath + '/');

    if (!fs.existsSync(startPath)) {
        console.log("💣 Directory doesn't exist:", startPath, " search pattern: ", searchPattern);
        return null;
    }

    var files = fs.readdirSync(startPath);
    for (let file of files) {
        var filePath = path.join(startPath, file);
        
        if (!matcher.matchAny(filePath, excludePatterns)) {
            if(!searchPattern) {
                matchingFiles.push(filePath);
                continue;
            }
            let patterns = Array.isArray(searchPattern) ? searchPattern : [searchPattern];            
            patterns.forEach(pattern => {
                if(filePath.indexOf(pattern) >= 0){
                    // console.log('-- found: ', filename);
                    matchingFiles.push(filePath);
                }
            });
       
            if (isDirectory(filePath, followSymlinks)) {
                findAllFiles(filePath, searchPattern, excludePatterns, followSymlinks, matchingFiles);
            }
        };

    };

    return matchingFiles;
}

function findAllFolders(startPath, searchPattern, excludePatterns = [], followSymlinks = true, matchingFiles = []) {
    return findAllFilesAndFolders(startPath, searchPattern, excludePatterns, followSymlinks, matchingFiles)?.filter(file => {
        if(!isDirectory(file, followSymlinks)) return false;
        const lastPathComponent = file.substring(file.lastIndexOf('/') + 1);
        return matcher.matchAny(lastPathComponent, [searchPattern]);
    });
}

/**
 * 
 * @param {String} startPath The directory from which to start a recursive search
 * @param {String} searchPattern The file name that should be looked for
 * @param {String[]} excludePatterns An array of paths that should be excluded from the search
 * @param {boolean} followSymlinks Defines if symlinks should be considered
 * @param {String[]} matchingFiles The matching files as recursion parameter
 */
function findAllFiles(startPath, searchPattern, excludePatterns = [], followSymlinks = true, matchingFiles = []) {    
    return findAllFilesAndFolders(startPath, searchPattern, excludePatterns, followSymlinks, matchingFiles)?.filter(file => {
        return isFile(file, followSymlinks);
    });
};

function createDirectoryIfNecessary(path){
    if(!fs.existsSync(path)){
        fs.mkdirSync(path, { recursive: true });
    }
}

function getLineNumberFromIndex(index, haystack){
    const tempString = haystack.substring(0, index);
    const lineNumber = tempString.split('\n').length;
    return lineNumber;
}

function getColumnFromIndex(index, haystack){
    const tempString = haystack.substring(0, index);
    const lines = tempString.split('\n');
    lines.pop();
    const indexOfLastLine = lines.length > 0 ? lines.join('\n').length + 1 : 0;
    const column = (index - indexOfLastLine) + 1;
    return column;
}

module.exports = { isFile, isDirectory, findAllFiles, findAllFolders, getFilesWithExtension, getSubdirectories, createDirectoryIfNecessary, getLineNumberFromIndex, getColumnFromIndex};
