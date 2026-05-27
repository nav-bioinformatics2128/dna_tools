dna = input("Enter DNA sequence: ")

complement = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

new_dna = ""

for base in dna:

    new_dna += complement[base]

print("Original DNA :", dna)

print("Complement DNA :", new_dna)
