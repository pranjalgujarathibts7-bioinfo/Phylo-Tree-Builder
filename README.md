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