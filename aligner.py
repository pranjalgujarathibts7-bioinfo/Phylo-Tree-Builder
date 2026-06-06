from Bio import SeqIO
from Bio.Align import PairwiseAligner
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Align import MultipleSeqAlignment


def align_sequences(fasta_file):
    print("\nReading sequences...")
    records = list(SeqIO.parse(fasta_file, "fasta"))
    print(f"✓ Found {len(records)} sequences")
    return records


def create_multiple_alignment(records):
    print("\nAligning sequences...")
    aligner = PairwiseAligner()
    aligner.mode = "global"
    
    reference = records[0]
    aligned_records = []
    
    for record in records:
        alignments = aligner.align(reference.seq, record.seq)
        best = alignments[0]
        aligned_seq = str(best).split("\n")[2]
        new_record = SeqRecord(Seq(aligned_seq), id=record.id, description="")
        aligned_records.append(new_record)
        print(f"  ✓ Aligned {record.id}")
    
    alignment = MultipleSeqAlignment(aligned_records)
    print(f"✓ Alignment complete")
    return alignment


if __name__ == "__main__":
    records = align_sequences("outputs/sequences.fasta")
    alignment = create_multiple_alignment(records)
    print(alignment)