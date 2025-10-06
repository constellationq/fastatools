from bioinftools import Seq, FastaReader


def demo_read_files():
    try:       
        reader = FastaReader("test_files/dna.fasta")
        
        for i, seq in enumerate(reader.reader(), 1):
            print(f"{i}. {seq.header}")
            print(f"   Длина: {len(seq)}, Тип: {seq.get_type()}")
            print(f"   Начало: {seq.sequence[:20]}...")
        print()
    except FileNotFoundError:
        print("Файл test_files/dna.fasta не найден")
    
    
    try:   
        reader = FastaReader("test_files/protein.fasta")
        
        print(f"Всего последовательностей: {reader.count_sequences()}")
        for i, seq in enumerate(reader.reader(), 1):
            print(f"{i}. {seq.header}")
            print(f"   Длина: {len(seq)}, Тип: {seq.type()}")
        print()
    except FileNotFoundError:
        print("Файл test_files/protein.fasta не найден")

def demo_large_file():  
    with open("large_test.fasta", "w") as f:
        for i in range(100):
            f.write(f">sequence_{i}\n")
            f.write("ATCG" * 10 + "\n")  
    
    
    reader = FastaReader("large_test.fasta")
    total_length = 0
    
    for seq in reader.reader():
        total_length += len(seq)
    
    print(f"Обработано {reader.count_sequences()} последовательностей")
    print(f"Общая длина: {total_length} символов")
    
    import os
    os.remove("large_test.fasta")

if __name__ == "__main__":
    demo_read_files()
    demo_large_file()