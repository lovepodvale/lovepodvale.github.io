#!/usr/bin/python3.12
# -*- coding: utf-8 -*-

with open('template.html', 'r') as f:
    html = f.read()
    f.close()

with open('otkaz.txt', 'r') as f:
    text = f.read()
    f.close()

lines = text.strip().split('\n\n')
lines = ['\t\t<p>' + line.replace('\n', '<br />') + '</p>\n' for line in lines]

html = html.replace('CONTENT', ''.join(lines))
html = html.replace('<main>	\t', '<main>\n\t\t')

with open('index.html', 'w') as f:
    f.write(html)
    f.close()
