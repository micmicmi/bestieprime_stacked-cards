const fs = require('fs');
const html = fs.readFileSync('1.html', 'utf8');
const matches = [...html.matchAll(/<img[^>]+src=\"(data:image[^>]+)\"[^>]*>/g)];
matches.forEach((m, i) => {
    console.log('Image ' + i + ': length ' + m[1].length);
    fs.writeFileSync('img/embedded_' + i + '.png', m[1].replace(/^data:image\/\w+;base64,/, ''), 'base64');
});
console.log('Done extracting ' + matches.length + ' images.');
