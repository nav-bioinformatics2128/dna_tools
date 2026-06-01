from Bio.Seq import Seq

dna = Seq("ATGGCC")

protein = dna.translate()

print("DNA:", dna)

print("Protein:", protein)
