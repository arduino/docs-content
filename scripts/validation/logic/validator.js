export class Validator {
    validations = [];

    addValidation(articles, func, ...args) {
        this.validations.push({articles: articles, callback: func, args: args});
    }

    get articleCount(){
        return this.validations.map(validation => {
            return validation.articles;
        }).flat(1).filter((articleB, index, self) =>
        index === self.findIndex((articleA) => (
          articleA.contentFilePath === articleB.contentFilePath
        ))
      ).length;
    }

    async validate(){
        return new Promise(resolve => {

            let promises = [];
            
            for(const validation of this.validations){
                for(let article of validation.articles){
                    let callbackArgs = [...validation.args];
                    callbackArgs.unshift(article);
                    promises.push(validation.callback.apply(null, callbackArgs));
                }
            }
            Promise.all(promises).then(results => {                                
                const flattenedResults = results.flat(1);
                resolve(flattenedResults);
            });

        });        
    }
}
