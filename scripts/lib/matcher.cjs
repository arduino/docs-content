/**
 * Checks if a text matches any of the supplied patterns.
 * @param {*} text 
 * @param {*} patterns 
 * @param {*} callback if specified the callback will be called with the pattern that was matched
 * @returns a boolean indicating whether a pattern was matched.
 */
function matchAny(text, patterns, callback = null){
    let result = false;

    for(let pattern of patterns){
        if(text.indexOf(pattern) != -1){
            if(callback) callback(pattern);            
            result = true;
        }
    }
    return result;
}

/**
 * Checks if the text matches all of the supplied patterns.
 * @param {*} text 
 * @param {*} patterns 
 * @param {*} callback if specified the callback will be called with the pattern that was matched
 * @returns a boolean indicating if all patterns were matched.
 */
function matchAll(text, patterns, callback = null){
    let result = true;

    for(let pattern of patterns){
        if(text.indexOf(pattern) == -1){   
            if(callback) callback(pattern);         
            result = false;
        }
    }
    return result;
}

module.exports = { matchAll, matchAny};