import csv
import os
import re
from collections import Counter

path = './'
lines = []

for file in os.listdir(path):
    if file.endswith('.tex'):
        filename = '%s%s' % (os.path.join(path), file)
        with open(filename, 'r') as f:
            lines.extend(f.readlines())

# Expressão regular
regex_expression = '\\\\cite(online)?\{(\w+)\}'

# Junta todos os itens da lista num único texto.
lines_joined = ''.join(lines)

# O findall retorna uma tupla das palavras encontradas
words_tuple = re.findall(regex_expression, lines_joined)

# Nova lista com as palavras separadas da tupla
words = [word for i, word in words_tuple]

# Contando e ordenando as palavras
result = Counter(words).most_common()

# Salvando result.tex
with open('result.tex', 'w') as f:
    f.write('\\begin{table}\n')
    f.write('\\begin{tabular}{ll}\n')
    for item in result:
        f.write('%s & %s \\\\\n' % item)
    f.write('\\end{tabular}\n')
    f.write('\\end{table}\n')

# Salvando result.csv
with open('result.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(('Autor', 'Quantidade'))
    for item in result:
        w.writerow(item)
