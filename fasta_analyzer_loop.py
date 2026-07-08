from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

def count_sequences():
    print("Total Sequences:", len(records))

def average_length():
    total = 0

    for record in records:
        total += len(record.seq)

    print("Average Length:", round(total / len(records), 2))

while True:

    print("\n===== FASTA ANALYZER =====")
    print("1. Count Sequences")
    print("2. Average Length")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        count_sequences()

    elif choice == "2":
        average_length()

    elif choice == "3":
        print("Thank you for using FASTA Analyzer!")
        break

    else:
        print("Invalid Choice")
