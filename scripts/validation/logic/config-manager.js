import { readFileSync } from 'fs';
import { load } from 'js-yaml';
import commandLineArgs from 'command-line-args';

export class ConfigManager {
    constructor() {
        this.options = {};
        this.config = { "generic" : {} };

        const optionDefinitions = [
            { name: 'check-broken-links', alias: 'c', type: Boolean },
            { name: 'debug', alias: 'd', type: Boolean, defaultOption: false },
            { name: 'verbose', alias: 'v', type: Boolean },
            { name: 'path', alias: 'p', type: String },
        ]

        this.cliOptions = commandLineArgs(optionDefinitions);
        this.updateOptions();
    }

    updateOptions() {
        this.options.checkBrokenLinks = this.cliOptions["check-broken-links"] ?? this.getConfig("generic").checkForBrokenLinks;
        this.options.debug = this.cliOptions["debug"] ?? this.getConfig("generic").debug;
        this.options.verbose = this.cliOptions["verbose"] ?? this.getConfig("generic").verbose;
        this.options.path = this.cliOptions["path"] ?? this.getConfig("generic").path;
    }

    addConfigFile(identifier, configFilePath) {
        const newConfig = load(readFileSync(configFilePath, 'utf8'));
        this.config[identifier] = newConfig;
        this.updateOptions();
    }

    getConfig(identifier){
        return this.config[identifier];
    }
}