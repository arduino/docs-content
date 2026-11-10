// Translated tutorials as docs.arduino.cc builds them: <name>-<lang>.md next to its English <name>.md or <name>-en.md
import { existsSync, readdirSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// The languages of src/utils/languages.json in docs.arduino.cc, except en
const TRANSLATION_FILE = /^(.*)-(?:de|es|fr|hi|it|ja|nl|pt|zh)\.md$/;

// Without its English file next to it, a name ending in -it.md is an English page and stays checked
export const isTranslatedTutorial = (filePath) => {
  const match = filePath.match(TRANSLATION_FILE);
  return !!match && (existsSync(`${match[1]}.md`) || existsSync(`${match[1]}-en.md`));
};

const findTranslatedTutorials = (dir) =>
  readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) return findTranslatedTutorials(fullPath);
    return isTranslatedTutorial(fullPath) ? [fullPath] : [];
  });

// `node translations.js content` prints them as codespell walks ./content/, comma separated for its --skip
if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  console.log(findTranslatedTutorials(process.argv[2]).map((file) => `./${file}`).join(','));
}
