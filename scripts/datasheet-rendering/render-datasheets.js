import { DatasheetRenderer} from '@arduino/datasheet-renderer'

(async function main() {
    let args = process.argv.slice(2)
    let datasheetsSourcePath = args[0];
    let renderer = new DatasheetRenderer("./config.json", datasheetsSourcePath);
    
    const generatedDatasheets = (await renderer.generatePDFsFromMarkdownFiles()).length;
    const allDatasheetsGenerated = generatedDatasheets == renderer.datasheets.length;
    const failedDatasheets = renderer.datasheets.length - generatedDatasheets;
    
    if(generatedDatasheets > 0)
        console.log("✅ %s Datasheets generated.", generatedDatasheets);
    if(failedDatasheets > 0)
        console.log("❌ %s Datasheets couldn't be generated.", failedDatasheets);
    process.exit(allDatasheetsGenerated ? 0 : -1);
})()