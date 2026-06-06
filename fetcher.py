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

def fetch_sequences(output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "sequences.fasta")
    records = []

    for species in SPECIES:
        print(f"Fetching sequence for: {species}")
        try:
            search_handle = Entrez.esearch(
                db="protein",
                term=f"{species}[Organism] AND cytochrome c[Protein Name]",
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

    SeqIO.write(records, output_file, "fasta")
    print(f"\n✓ All sequences saved to {output_file}")
    print(f"✓ Total sequences fetched: {len(records)}")
    return output_file

if __name__ == "__main__":
    fetch_sequences()