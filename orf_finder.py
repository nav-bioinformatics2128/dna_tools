dna = input("Enter DNA sequence: ")

stop_codons = ["TAA", "TAG", "TGA"]

for i in range(len(dna)):

    start_codon = dna[i:i+3]

    if start_codon == "ATG":

        for j in range(i+3, len(dna), 3):

            stop_codon = dna[j:j+3]

            if stop_codon in stop_codons:

                print("ORF found:")

                print(dna[i:j+3])

                break
