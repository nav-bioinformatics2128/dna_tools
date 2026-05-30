dna_sequences = [
    "ATGC",
    "GGCC",
    "TTAA",
    "ATGCGA"
]

search_sequence = input("Enter DNA sequence to search: ")

if search_sequence in dna_sequences:

    print("Sequence Found")

else:

    print("Sequence Not Found")
position = dna_sequences.index(search_sequence)

print("Found at position:", position + 1)
