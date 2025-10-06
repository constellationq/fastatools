class Seq():
    def __init__ (self, head, seq):
        self.head = head.strip()
        self.seq = seq.upper().replace('\n', '').replace(' ','')
        self.header = head.strip() 
        self.sequence = seq.upper().replace('\n', '').replace(' ','')  
    
    def __str__(self):
        return f">{self.head}\n{self.seq}"
    
    def __len__(self):
        return len(self.seq)
    
    def len(self):
        return len(self.seq)
    
    def type(self):
        nuc = set("ACGTU")
        prot = set("ACDEFGHIKLMNPQRSTVWY")
        seqtype = set(self.seq)
        if seqtype.issubset(nuc):
            return "нуклеотидная последовательность"
        elif seqtype.issubset(prot):
            return "белковая последовательность" 
        else:
            return "неизвестный тип последовательности"
    
    def get_type(self):
        return self.type()

class FastaReader():
    def __init__(self, filename):
        self.filename = filename
    
    def reader(self):
        current_head = None
        current_seq = []
        with open(self.filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    if current_head is not None:
                        yield Seq(current_head, ''.join(current_seq))
                    current_head = line[1:]
                    current_seq = []
                else:
                    if line:  
                        current_seq.append(line) 
            if current_head is not None:
                yield Seq(current_head, ''.join(current_seq))
    
    def count_sequences(self):
        count = 0
        with open(self.filename, 'r') as file:
            for line in file:
                if line.startswith('>'):
                    count += 1
        return count                 