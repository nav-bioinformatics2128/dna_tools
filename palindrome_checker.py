dna = input("Enter DNA sequence: ")

complement = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

reverse_complement = ""

for base in dna:

    reverse_complement += complement[base]

reverse_complement = reverse_complement[::-1]

print("Reverse Complement :", reverse_complement)

if dna == reverse_complement:

    print("DNA is palindrome")

else:

    print("DNA is not palindrome")
