from Bio.Seq import Seq

dna = Seq("ATGCGA")

print("DNA:", dna)

print("Length:", len(dna))

print("Count of G:", dna.count("G"))
print("Count of A:", dna.count("A"))
print("Count of T:", dna.count("T"))
print("Count of C:", dna.count("C"))
