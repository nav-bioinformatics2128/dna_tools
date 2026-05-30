dna_sequences = [
    "ATGCGA",
    "GG",
    "ATATTTAAA",
    "ATGCGCTAGCTA"
]

sorted_sequences = sorted(dna_sequences, key=len)

print("Sequences Sorted by Length")

print("=" * 30)

for dna in sorted_sequences:

    print(dna, "Length :", len(dna))
