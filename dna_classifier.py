dna_sequences = [
    "ATATTT",
    "GGGCCC",
    "ATGCGA",
    "ATATGC"
]

for dna in dna_sequences:

    gc_count = dna.count("G") + dna.count("C")

    gc_percentage = (gc_count / len(dna)) * 100

    print("DNA Sequence :", dna)

    print("GC Content :", round(gc_percentage, 2), "%")

    if gc_percentage >= 50:

        print("Classification : GC-rich")

    else:

        print("Classification : AT-rich")

    print("=" * 30)
