# Простой FASTA инструмент

Минималистичная библиотека для работы с FASTA файлами.

## Использование

```python
from bioinftools import Seq, FastaReader

# Чтение файла
reader = FastaReader("sequences.fasta")
for sequence in reader.read_sequences():
    print(f"{sequence.header}: {len(sequence)} bp")