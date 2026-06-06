from fetcher import fetch_sequences
from aligner import align_sequences, create_multiple_alignment
from tree_builder import calculate_distance_matrix, build_trees, visualize_trees
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Phylogenetic Tree Builder using Cytochrome C protein sequences"
    )
    parser.add_argument(
        "--output",
        default="outputs",
        help="Output directory for results (default: outputs)"
    )
    args = parser.parse_args()

    print("*** Phylogenetic Tree Builder ***")
    print("=" * 40)

    fasta_file = fetch_sequences(args.output)
    records = align_sequences(fasta_file)
    alignment = create_multiple_alignment(records)
    distance_matrix = calculate_distance_matrix(alignment, args.output)
    upgma_tree, nj_tree = build_trees(distance_matrix, args.output)
    visualize_trees(upgma_tree, nj_tree, args.output)
    
    print("=" * 40)
    print("Pipeline complete!")
    print(f"All results saved to: {args.output}/")


if __name__ == "__main__":
    main()