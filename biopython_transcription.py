from Bio.Seq import Seq

dna = Seq("ATGCGA")

rna = dna.transcribe()

print("DNA:", dna)

print("RNA:", rna)
