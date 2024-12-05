import csv


def remove_duplicates(input_file, output_file):
    seen_ids = set()
    with open(input_file, mode="r", newline="") as infile, open(
        output_file, mode="w", newline=""
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row[0] not in seen_ids:
                writer.writerow(row)
                seen_ids.add(row[0])


input_file = "omaz.csv"  # Replace with your input file path
output_file = " omazNoDuplicates.csv"  # Replace with your output file path
remove_duplicates(input_file, output_file)
