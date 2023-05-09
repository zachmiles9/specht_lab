import csv

# Define the number of columns to keep
COLUMNS_PER_GROUP = 8

# Open the input CSV file
with open('output_file.csv', 'r') as infile:
    # Create a CSV reader object
    reader = csv.reader(infile)

    # Open the output CSV file
    with open('output_file_2.csv', 'w', newline='') as outfile:
        # Create a CSV writer object
        writer = csv.writer(outfile)

        # Iterate over each row in the input CSV file
        for row in reader:
            # Initialize the new row
            new_row = []

            # Iterate over each column in the row
            for i, value in enumerate(row):
                # Check if the column index is divisible by the number of columns to keep
                if (i + 1) % COLUMNS_PER_GROUP == 0:
                    # If it is, add the value to the new row
                    new_row.append(value)

            # Write the new row to the output CSV file
            writer.writerow(new_row)
