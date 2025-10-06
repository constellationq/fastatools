# Простой FASTA инструмент

Минималистичная библиотека для работы с FASTA файлами.

## Установка
'''bash
git clone https://github.com/constellationq/fastatools.git
cd fastatools

## Использование
'''python
from bioinftools import FastaReader

reader = FastaReader("dna.fasta")
for seq in reader.reader():
    print (f"{seq.header}:{len(seq)} символов, тип: {seq.type()})

## Запуск демо
''' bash
python test.py

