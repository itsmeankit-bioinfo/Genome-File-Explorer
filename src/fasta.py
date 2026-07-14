from Bio import SeqIO


class FASTAReader:

    def __init__(self, filepath):
        self.filepath = filepath
        self.records = []

    def load(self):
        self.records = list(SeqIO.parse(self.filepath, "fasta"))
        return self.records

    def sequence_length(self, sequence):
        return len(sequence)

    def gc_content(self, sequence):
        sequence = sequence.upper()

        g = sequence.count("G")
        c = sequence.count("C")

        return ((g + c) / len(sequence)) * 100

    def at_content(self, sequence):
        sequence = sequence.upper()

        a = sequence.count("A")
        t = sequence.count("T")

        return ((a + t) / len(sequence)) * 100

    def nucleotide_count(self, sequence):

        sequence = sequence.upper()

        return {
            "A": sequence.count("A"),
            "T": sequence.count("T"),
            "G": sequence.count("G"),
            "C": sequence.count("C"),
            "N": sequence.count("N")
        }