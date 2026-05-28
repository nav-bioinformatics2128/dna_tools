dna = input("Enter DNA sequence: ")

stop_codons = ["TAA", "TAG", "TGA"]

print("DNA Sequence :", dna)

print("=" * 30)

for i in range(len(dna)):

    codon = dna[i:i+3]

    if codon in stop_codons:

        print("Stop codon", codon, "found at position:", i+1)
