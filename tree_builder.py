from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo 
import matplotlib.pyplot as plt
import matplotlib
import csv
import os


def calculate_distance_matrix(alignment, output_dir="outputs"):
    print("\nCalculating distance matrix...")
    calculator = DistanceCalculator("identity")
    distance_matrix = calculator.get_distance(alignment)
    print("✓ Distance matrix calculated")
    
    csv_path = os.path.join(output_dir, "distance_matrix.csv")
    names = distance_matrix.names
    
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["species"] + names)
        for i, name in enumerate(names):
            row = [name] + [round(distance_matrix[name, n], 4) for n in names]
            writer.writerow(row)
    
    print(f"✓ Distance matrix saved to {csv_path}")
    return distance_matrix


def build_trees(distance_matrix, output_dir="outputs"):
    print("\nBuilding phylogenetic trees...")
    constructor = DistanceTreeConstructor()
    
    upgma_tree = constructor.upgma(distance_matrix)
    print("✓ UPGMA tree built")
    
    nj_tree = constructor.nj(distance_matrix)
    print("✓ Neighbor-Joining tree built")
    
    upgma_path = os.path.join(output_dir, "upgma_tree.nwk")
    nj_path = os.path.join(output_dir, "nj_tree.nwk")
    
    Phylo.write(upgma_tree, upgma_path, "newick")
    Phylo.write(nj_tree, nj_path, "newick")
    
    print(f"✓ Trees saved in Newick format")
    return upgma_tree, nj_tree


def visualize_trees(upgma_tree, nj_tree, output_dir="outputs", protein="cytochrome c"):
    print("\nVisualizing trees...")
    matplotlib.use("Agg")
    
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))
    
    axes[0].set_title("UPGMA Tree", fontsize=16, fontweight="bold")
    Phylo.draw(upgma_tree, axes=axes[0], do_show=False)
    
    axes[1].set_title("Neighbor-Joining Tree", fontsize=16, fontweight="bold")
    Phylo.draw(nj_tree, axes=axes[1], do_show=False)
    
    plt.suptitle("Cytochrome C Phylogenetic Trees", fontsize=20, fontweight="bold")
    plt.tight_layout()
    
    protein_clean = protein.replace(" ", "_").replace("/", "_")
    output_path = os.path.join(output_dir, f"phylogenetic_trees_{protein_clean}.png")
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    print(f"✓ Trees visualized and saved to {output_path}")


if __name__ == "__main__":
    from aligner import align_sequences, create_multiple_alignment
    
    records = align_sequences("outputs/sequences.fasta")
    alignment = create_multiple_alignment(records)
    
    distance_matrix = calculate_distance_matrix(alignment)
    upgma_tree, nj_tree = build_trees(distance_matrix)
    visualize_trees(upgma_tree, nj_tree)