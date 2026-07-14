from Bio import SeqIO


class FASTAReader:
    """Read and analyze FASTA files."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.records = []

    def load(self):
        """Load sequences from a FASTA file."""
        self.records = list(SeqIO.parse(self.filepath, "fasta"))
        return self.records