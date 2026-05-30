dna_sequences = [
    "ATGA",
    "AGTT",
    "GGCA",
    "ATAA",
    "TTGC"
]

count = 0

for dna in dna_sequences:

    if dna.endswith("A"):

        count += 1

print("Sequences ending with A:", count)
