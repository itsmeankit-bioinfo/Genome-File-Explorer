class GenomeFileExplorerError(Exception):
    """Base exception for Genome File Explorer."""
    pass


class InvalidDNASequenceError(GenomeFileExplorerError):
    """Raised when DNA contains invalid characters."""
    pass


class InvalidFASTAFileError(GenomeFileExplorerError):
    """Raised when a FASTA file cannot be parsed."""
    pass


class EmptyFASTAFileError(GenomeFileExplorerError):
    """Raised when a FASTA file contains no sequences."""
    pass