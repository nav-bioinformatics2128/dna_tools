dna = "ATGTTT"

codon_table = {
    "ATG": "methionine",
    "TTT": "phenylalanine"
}

protein_chain = []

for i in range(0, len(dna), 3):

    codon = dna[i:i+3]

    protein = codon_table[codon]

    protein_chain.append(protein)

final_protein = "-".join(protein_chain)

print("Protein Chain:", final_protein)
