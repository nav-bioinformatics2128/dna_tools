dna = input("Enter DNA sequence: ")

start_codon = "ATG"

print("DNA Sequence :", dna)

print("=" * 30)

for i in range(len(dna)):

    codon = dna[i:i+3]

    if codon == start_codon:

        print("Start codon found at position:", i+1)
