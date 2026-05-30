dna_sequences = [
    "ATGCGA",
    "GG",
    "ATATTTAAA",
    "ATGCGCTAGCTA"
]

total_length = 0

for dna in dna_sequences:

    total_length += len(dna)

average_length = total_length / len(dna_sequences)

print("Total Length :", total_length)

print("Number of Sequences :", len(dna_sequences))

print("Average Length :", round(average_length, 2))
