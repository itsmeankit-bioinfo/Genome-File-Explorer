from src.fasta import FASTAReader


def main():

    reader = FASTAReader("sample_data/sample.fasta")

    sequences = reader.load()

    print("=" * 55)
    print("Genome File Explorer")
    print("=" * 55)

    for record in sequences:

        seq = str(record.seq)

        print(f"\nSequence ID : {record.id}")
        print(f"Description : {record.description}")

        print(f"\nLength       : {reader.sequence_length(seq)} bp")
        print(f"GC Content   : {reader.gc_content(seq):.2f}%")
        print(f"AT Content   : {reader.at_content(seq):.2f}%")

        counts = reader.nucleotide_count(seq)

        print(f"A Count      : {counts['A']}")
        print(f"T Count      : {counts['T']}")
        print(f"G Count      : {counts['G']}")
        print(f"C Count      : {counts['C']}")
        print(f"N Count      : {counts['N']}")

        print("-" * 55)


if __name__ == "__main__":
    main()

invalid = reader.validate_sequence(seq)

if len(invalid) == 0:
    print("Validation   : ✅ Valid DNA Sequence")
else:
    print("Validation   : ❌ Invalid DNA Sequence")

    for pos, char in invalid:
        print(f"Invalid Base : {char} at position {pos}")