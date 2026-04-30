import urllib.request
import re
from pypdf import PdfReader

reader = PdfReader('/Users/ncai/dev/HechangPu/红河谷简谱.pdf')
text_lines = []
for page in reader.pages:
    text_lines.extend(page.extract_text().split('\n'))

with open('score_text.txt', 'w') as f:
    f.write('\n'.join(text_lines))

print("Saved score_text.txt")
