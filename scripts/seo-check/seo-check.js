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
    const chatCompletion = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a helpful SEO and content writing assistant.' },
        { role: 'user', content: `Please review and improve this Markdown article for SEO:\n\n${content}` }
      ],
    });

    const result = chatCompletion.choices[0].message.content;
    console.log('\n💬 Response from OpenAI:\n');
    console.log(result);

    // Optional: write to file
    const outputPath = filePath.replace(/\.md$/, '.openai.md');
    fs.writeFileSync(outputPath, result, 'utf8');
    console.log(`\n✅ Response saved to: ${outputPath}`);
  } catch (err) {
    console.error('⚠️ Error communicating with OpenAI:', err);
  }
})();