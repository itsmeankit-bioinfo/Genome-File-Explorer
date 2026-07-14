from src.fasta import FASTAReader


def main():

    try:
        reader = FASTAReader("sample_data/sample.fasta")

        sequences = reader.load()

        # Your existing analysis code here

    except FileNotFoundError:
        print("❌ FASTA file not found.")

    except Exception as e:
        print("❌ Error: {e}")

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

        invalid = reader.validate_sequence(seq)

        if len(invalid) == 0:
            print("Validation   : ✅ Valid DNA Sequence")
        else:
            print("Validation   : ❌ Invalid DNA Sequence")

            for pos, char in invalid:
                print(f"Invalid Base : {char} at position {pos}")

        print("-" * 55)

        summary = reader.summary()

        print("\n" + "=" * 55)
        print("Genome Summary")
        print("=" * 55)

        print(f"Total Sequences : {summary['total']}")
        print(f"Longest Sequence : {summary['longest'][0]} ({summary['longest'][1]} bp)")
        print(f"Shortest Sequence : {summary['shortest'][0]} ({summary['shortest'][1]} bp)")
        print(f"Average Length : {summary['average_length']:.2f} bp")
        print(f"Overall GC : {summary['overall_gc']:.2f}%")