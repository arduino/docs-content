export class ValidationIssue {
    static Type = Object.freeze({
        ERROR:   Symbol("error"),
        WARNING:  Symbol("warning")
    });

    /**
     * 
     * @param {*} message the error message to be displayed
     * @param {*} file the file where the error occurred
     * @param {*} type Type.ERROR or Type.WARNING
     * @param {*} lineNumber the line number where the error occurred
     * @param {*} column the column / character position where the error occurred
     */
    constructor(message, file, type = ValidationIssue.Type.ERROR, lineNumber = 1, column = 1){
        this.message = message;
        this.file = file;
        this.type = type;
        this.lineNumber = lineNumber;
        this.column = column;
    }
}
