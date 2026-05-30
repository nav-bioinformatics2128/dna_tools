dna_sequences = [
    "AT",
    "ATGCGA",
    "GG",
    "ATATTTAAA",
    "ATGCGCTAGCTA"
]

for dna in dna_sequences:

    if len(dna) > 5:

        print("Sequence :", dna)

        print("Length :", len(dna))

        print("=" * 30)
