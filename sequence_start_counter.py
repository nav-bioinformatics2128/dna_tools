dna_sequences = [
    "ATGC",
    "AGTT",
    "GGCC",
    "ATAA",
    "TTGC"
]

count = 0

for dna in dna_sequences:

    if dna.startswith("A"):

        count += 1

print("Sequences starting with A:", count)
