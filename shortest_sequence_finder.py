dna_sequences = [
    "ATGCGA",
    "GG",
    "ATATTTAAA",
    "ATGCGCTAGCTA"
]

shortest_sequence = dna_sequences[0]

for dna in dna_sequences:

    if len(dna) < len(shortest_sequence):

        shortest_sequence = dna

print("Shortest DNA Sequence :")

print(shortest_sequence)

print("Length :", len(shortest_sequence))
