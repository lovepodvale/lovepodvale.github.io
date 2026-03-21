#!/usr/bin/python3.12
# -*- coding: utf-8 -*-

import os


with open('template.html', 'r') as f:
    init_html = f.read()
    f.close()

with open('otkaz.txt', 'r') as f:
    text = f.read()
    f.close()

lines = text.strip().split('\n\n')
lines = ['\t\t<p>' + line.replace('\n', '<br />') + '</p>\n' for line in lines]
lines[0] = lines[0].replace('* * *', '* * * <a href="media.html">картинки</a>')

html = init_html.replace('CONTENT', ''.join(lines))
html = html.replace('<main>	\t', '<main>\n\t\t')

with open('index.html', 'w') as f:
    f.write(html)
    f.close()

fnames = ['<a target="_blank" href="/media/{0}">{0}</a>'.format(fname) for fname in sorted(os.listdir('media'))]
fnames = '<p>* * * <a href="index.html">текст</a></p><p>' + '<br />'.join(fnames) + '</p>'

html = init_html.replace('CONTENT', fnames)
with open('media.html', 'w') as f:
    f.write(html)
    f.close()
