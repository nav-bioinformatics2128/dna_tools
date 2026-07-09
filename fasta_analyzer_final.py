from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

def count_sequences():
    print("Total Sequences:", len(records))


def average_length():
    total = 0

    for record in records:
        total += len(record.seq)

    print("Average Length:", round(total / len(records), 2))


def average_gc():
    total_gc = 0

    for record in records:
        sequence = str(record.seq)

        gc_count = sequence.count("G") + sequence.count("C")

        gc_percent = (gc_count / len(sequence)) * 100

        total_gc += gc_percent

    print("Average GC:", round(total_gc / len(records), 2))


def longest_sequence():
    longest = 0
    longest_id = ""

    for record in records:

        if len(record.seq) > longest:
            longest = len(record.seq)
            longest_id = record.id

    print("Longest Sequence:", longest_id)
    print("Length:", longest)


def shortest_sequence():
    shortest = float("inf")
    shortest_id = ""

    for record in records:

        if len(record.seq) < shortest:
            shortest = len(record.seq)
            shortest_id = record.id

    print("Shortest Sequence:", shortest_id)
    print("Length:", shortest)


def dataset_summary():

    total_length = 0
    total_gc = 0

    longest = 0
    shortest = float("inf")

    for record in records:

        sequence = str(record.seq)

        length = len(sequence)

        gc_count = sequence.count("G") + sequence.count("C")

        gc_percent = (gc_count / length) * 100

        total_length += length
        total_gc += gc_percent

        if length > longest:
            longest = length

        if length < shortest:
            shortest = length

    print("\n===== DATASET SUMMARY =====")

    print("Total Sequences:", len(records))

    print("Average Length:", round(total_length / len(records), 2))

    print("Average GC:", round(total_gc / len(records), 2))

    print("Longest Sequence:", longest)

    print("Shortest Sequence:", shortest)


def search_sequence():

    sequence_id = input("Enter Sequence ID: ")

    found = False

    for record in records:

        if record.id == sequence_id:

            print("\nSequence Found!")

            print("ID:", record.id)

            print("Length:", len(record.seq))

            print("Sequence:")

            print(record.seq)

            gc_count = record.seq.count("G") + record.seq.count("C")

            gc_percent = (gc_count / len(record.seq)) * 100

            print("GC Content:", round(gc_percent, 2))

            found = True

            break

    if not found:
        print("Sequence Not Found!")


def sequence_information():

    sequence_id = input("Enter Sequence ID: ")

   
