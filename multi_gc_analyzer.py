dna_sequences = [
    "ATGCGA",
    "GGGCCC",
    "ATATTT"
]

for dna in dna_sequences:

    gc_count = dna.count("G") + dna.count("C")

    gc_percentage = (gc_count / len(dna)) * 100

    print("DNA Sequence :", dna)

    print("GC Content :", round(gc_percentage, 2), "%")

    print("=" * 30)
