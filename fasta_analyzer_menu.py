from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

def count_sequences():
    print("Total Sequences:", len(records))

def average_length():
    total = 0

    for record in records:
        total += len(record.seq)

    print("Average Length:", round(total / len(records), 2))


print("===== FASTA ANALYZER =====")
print("1. Count Sequences")
print("2. Average Length")

choice = input("Enter your choice: ")

if choice == "1":
    count_sequences()

elif choice == "2":
    average_length()

else:
    print("Invalid Choice")
