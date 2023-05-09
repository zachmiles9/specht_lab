import csv
# Define the number of rows to consolidate
ROWS_PER_GROUP = 8

# Open the input CSV file
with open('input_file.csv', 'r') as infile:
    # Create a CSV reader object
    reader = csv.reader(infile)

    # Open the output CSV file
    with open('output_file.csv', 'w', newline='') as outfile:
        # Create a CSV writer object
        writer = csv.writer(outfile)

        # Initialize the list of rows to consolidate
        rows_to_consolidate = []

        # Iterate over each row in the input CSV file
        for i, row in enumerate(reader):
            # Add the current row to the list of rows to consolidate
            rows_to_consolidate.append(row)

            # If we've accumulated enough rows, consolidate them
            if len(rows_to_consolidate) == ROWS_PER_GROUP:
                # Initialize the consolidated row
                consolidated_row = []

                # Iterate over each cell in the row
                for j in range(len(rows_to_consolidate[0])):
                    # Get the set of values for this cell in each row to be consolidated
                    values = set(row[j] for row in rows_to_consolidate)

                    # If there's only one value, add it to the consolidated row
                    if len(values) == 1:
                        consolidated_row.append(values.pop())
                    # Otherwise, add a comma-separated list of the values to the consolidated row
                    else:
                        consolidated_row.append(','.join(sorted(values)))

                # Write the consolidated row to the output CSV file
                writer.writerow(consolidated_row)

                # Reset the list of rows to consolidate
                rows_to_consolidate = []

        # If there are any remaining rows to consolidate, do so now
        if len(rows_to_consolidate) > 0:
            # Initialize the consolidated row
            consolidated_row = []

            # Iterate over each cell in the row
            for j in range(len(rows_to_consolidate[0])):
                # Get the set of values for this cell in each row to be consolidated
                values = set(row[j] for row in rows_to_consolidate)

                # If there's only one value, add it to the consolidated row
                if len(values) == 1:
                    consolidated_row.append(values.pop())
                # Otherwise, add a comma-separated list of the values to the consolidated row
                else:
                    consolidated_row.append(','.join(sorted(values)))

            # Write the consolidated row to the output CSV file
            writer.writerow(consolidated_row)

