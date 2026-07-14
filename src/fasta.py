from Bio import SeqIO
from src.exceptions import EmptyFASTAFileError
from src.utils import average

class FASTAReader:

    def __init__(self, filepath):
        self.filepath = filepath
        self.records = []

    def load(self):
        self.records = list(SeqIO.parse(self.filepath, "fasta"))

        if len(self.records) == 0:
            raise EmptyFASTAFileError(
                "The FASTA file contains no sequences."
            )

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
    
    def validate_sequence(self, sequence):
        """
        Validate DNA sequence.
        Returns True if valid.
        """

        valid_bases = {"A", "T", "G", "C", "N"}

        sequence = sequence.upper()

        invalid = []

        for index, base in enumerate(sequence, start=1):
            if base not in valid_bases:
                invalid.append((index, base))

        return invalid


    def is_valid(self, sequence):
        return len(self.validate_sequence(sequence)) == 0
    
    def summary(self):
        """
        Generate summary statistics for all sequences.
        """

        lengths = []
        gc_values = []

        longest = None
        shortest = None

        for record in self.records:

            seq = str(record.seq)

            length = self.sequence_length(seq)
            gc = self.gc_content(seq)

            lengths.append(length)
            gc_values.append(gc)

            if longest is None or length > longest[1]:
                longest = (record.id, length)

            if shortest is None or length < shortest[1]:
                shortest = (record.id, length)

        return {
            "total": len(self.records),
            "average_length": average(lengths),
            "overall_gc": average(gc_values),
            "longest": longest,
            "shortest": shortest
        }