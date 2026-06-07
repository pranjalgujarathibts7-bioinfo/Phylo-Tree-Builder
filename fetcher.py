from Bio import Entrez, SeqIO
import time
import os

Entrez.email = "pranjalgujarathibts7@gmail.com"

SPECIES = [
    "Homo sapiens",
    "Pan troglodytes",
    "Equus caballus",
    "Bos taurus",
    "Gallus gallus",
    "Rana pipiens",
    "Thunnus albacares",
    "Triticum aestivum"
]

def fetch_sequences(output_dir="outputs", species_list=None, protein="cytochrome c"):
    os.makedirs(output_dir, exist_ok=True)
    if species_list is None:
        species_list = SPECIES
    output_file = os.path.join(output_dir, "sequences.fasta")
    records = []

    for species in species_list:
        print(f"Fetching sequence for: {species}")
        try:
            search_handle = Entrez.esearch(
                db="protein",
                term=f"{species}[Organism] AND {protein}[Protein Name]",
                retmax=1
            )
            search_results = Entrez.read(search_handle)
            search_handle.close()

            if search_results["IdList"]:
                seq_id = search_results["IdList"][0]
                fetch_handle = Entrez.efetch(
                    db="protein",
                    id=seq_id,
                    rettype="fasta",
                    retmode="text"
                )
                record = SeqIO.read(fetch_handle, "fasta")
                fetch_handle.close()
                record.id = species.replace(" ", "_")
                record.description = ""
                records.append(record)
                print(f"  ✓ Got sequence for {species}")
                time.sleep(0.4)

        except Exception as e:
            print(f"  ✗ Failed for {species}: {e}")

    if len(records) < 3:
        print(f"\n✗ Only {len(records)} sequences fetched.")
        print("Need at least 3 sequences to build a tree.")
        print("Try different species names or a different protein name.")
        return None

    SeqIO.write(records, output_file, "fasta")
    print(f"\n✓ All sequences saved to {output_file}")
    print(f"✓ Total sequences fetched: {len(records)}")
    return output_file