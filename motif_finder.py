dna = "ACGTTGCATGTCGCATGATGCATGAGCT"
motif = "CAT"

print("DNA Sequence:", dna)
print("Motif:", motif)
print("=" * 40)

for i in range(len(dna)):

    piece = dna[i:i+len(motif)]

    if piece == motif:
        print(f"Motif found at position: {i+1}")
