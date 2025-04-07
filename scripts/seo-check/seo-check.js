require('dotenv').config({ path: __dirname + '/.env' });
const fs = require('fs');
const path = require('path');
const OpenAI = require('openai');

// 1. Get file path from arguments
const filePath = process.argv[2];
if (!filePath) {
  console.error('❌ No file path provided.');
  process.exit(1);
}

// 2. Read file content
const content = fs.readFileSync(filePath, 'utf8');

// 3. Set up OpenAI client (v4 style)
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// 4. Send to OpenAI
(async () => {
  try {
    const prompt = `Please review the following markdown content, and recommend SEO improvements.
    The SEO improvements should be made in coordination with the following guidelines:
    - https://developers.google.com/search/docs/fundamentals/creating-helpful-content
    - https://developers.google.com/search/docs/crawling-indexing/url-structure

    Please extract non-generic focus points from the content and suggest specific improvements.
    You can extract specific sections from the content, place it in markdown code block, and then below, 
    make a markdown codeblock containing a new suggestion for the section.
    
    :\n\n${content}`;

    const chatCompletion = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a helpful SEO and content writing assistant.' },
        { role: 'user', content: prompt }
      ],
    });

    const result = chatCompletion.choices[0].message.content;

    // Optional: write to file
    const outputPath = filePath.replace(/\.md$/, '.openai.md');
    fs.writeFileSync(outputPath, result, 'utf8');
    console.log(`\n✅ Response saved to: ${outputPath}`);
  } catch (err) {
    console.error('⚠️ Error communicating with OpenAI:', err);
  }
})();