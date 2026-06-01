from Bio.Seq import Seq

dna = Seq("ATGCGA")

reverse_complement = dna.reverse_complement()

print("DNA:", dna)

print("Reverse Complement:", reverse_complement)
