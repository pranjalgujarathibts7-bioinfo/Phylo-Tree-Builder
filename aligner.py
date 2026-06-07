from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Align import MultipleSeqAlignment, PairwiseAligner


def align_sequences(fasta_file):
    print("\nReading sequences...")
    records = list(SeqIO.parse(fasta_file, "fasta"))
    print(f"✓ Found {len(records)} sequences")
    return records


def create_multiple_alignment(records):
    print("\nPerforming Multiple Sequence Alignment...")
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5

    reference = records[0]
    aligned_records = []

    for record in records:
        alignments = aligner.align(reference.seq, record.seq)
        best = alignments[0]
        aligned_seq = str(best).split("\n")[2]
        new_record = SeqRecord(
            Seq(aligned_seq),
            id=record.id,
            description=""
        )
        aligned_records.append(new_record)
        print(f"  ✓ Aligned {record.id}")

    alignment = MultipleSeqAlignment(aligned_records)
    print(f"✓ MSA complete")
    print(f"✓ Alignment: {len(alignment)} rows x {alignment.get_alignment_length()} columns")
    return alignment


if __name__ == "__main__":
    records = align_sequences("outputs/sequences.fasta")
    alignment = create_multiple_alignment(records)
    print(alignment)