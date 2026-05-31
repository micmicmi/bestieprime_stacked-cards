const fs = require('fs');
const html = fs.readFileSync('1.html', 'utf8');
const clean = html.replace(/<svg[\s\S]*?<\/svg>/g, '[SVG]\n')
                  .replace(/<img[^>]+src=\"data:image[^>]+>/g, '[IMG]\n')
                  .replace(/style=\"[^\"]*\"/g, '');
fs.writeFileSync('clean.html', clean);
console.log('Cleaned file saved as clean.html');
