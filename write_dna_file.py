dna_sequences = [
    "ATGCGA",
    "GGGCCC",
    "ATATTTAAA"
]

file = open("dna_sequences.txt", "w")

for dna in dna_sequences:

    file.write(dna + "\n")

file.close()

print("Sequences saved successfully")
