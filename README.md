# Phylo-Tree-Builder

A Python pipeline that fetches real protein sequences from NCBI, aligns them, and builds phylogenetic trees showing evolutionary relationships between species.

## What it does

- Fetches real cytochrome c protein sequences from NCBI for 8 species
- Aligns sequences using Biopython's PairwiseAligner
- Calculates evolutionary distance matrix
- Builds UPGMA and Neighbor-Joining phylogenetic trees
- Saves results as FASTA, CSV, Newick, and PNG files

## Species analyzed

Human, Chimpanzee, Horse, Cow, Chicken, Frog, Tuna, Wheat

## Background

**Why cytochrome c?**
Cytochrome c is a highly conserved protein found in almost every living organism.
It performs the same function across all life, but small sequence differences
reflect millions of years of evolution, making it ideal for phylogenetic analysis.

**Why UPGMA and Neighbor-Joining?**
UPGMA assumes all species evolve at a constant rate and produces a rooted tree.
Neighbor-Joining does not make this assumption and is generally considered more
accurate for real biological data. Building both allows comparison of results.

**Why protein sequences instead of DNA?**
Proteins are more conserved than DNA. Silent mutations at the DNA level do not
affect the protein sequence, creating noise in DNA-based phylogenetics. Protein
sequences give a cleaner evolutionary signal.

**Why wheat as an outgroup?**
Triticum aestivum (wheat) is a plant — distantly related to all animals in this
analysis. It serves as an outgroup to root the tree and provide evolutionary context.

## Requirements

- Python 3.x
- Biopython
- Matplotlib

## Installation

pip install biopython matplotlib

## Usage

python main.py

## Output

All results are saved in the outputs/ folder:
- sequences.fasta — downloaded protein sequences
- distance_matrix.csv — evolutionary distances between species
- upgma_tree.nwk — UPGMA tree in Newick format
- nj_tree.nwk — Neighbor-Joining tree in Newick format
- phylogenetic_trees.png — visualization of both trees

## Author

Pranjal Gujarathi