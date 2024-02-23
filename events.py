import csv
from datetime import datetime

# Define the data to be written to the CSV file
data = [
    ["INSERTED", "Placement", 12, "null", "2018-04-10 12:34:56.789"],
    ["INSERTED", "Placement", 13, "null", "2018-04-10 12:43:10.123"],
    ["UPDATED", "Company", 123, "[status, companyURL]", "2018-04-10 12:44:00.123"],
    ["UPDATED", "Placement", 13, "[status, hoursPerDay, overtimeRate]", "2018-04-10 14:52:43.699"]
]

# Validate event type and timestamp format
for row in data:
    # Validate event type
    if row[0] not in ["INSERTED", "UPDATED", "DELETED"]:
        raise ValueError("Invalid event type:", row[0])
    
    # Validate timestamp format
    try:
        datetime.strptime(row[-1], '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        raise ValueError("Invalid timestamp format:", row[-1])

# Open the CSV file in write mode
with open('events.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["event type", "entity name", "entity id", "[fields updated]", "timestamp"])
    # Write the data rows
    writer.writerows(data)

# Open the CSV file for reading
with open('events.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Print each row to the terminal
        print(', '.join(row))  # Join elements of each row with a comma and print

# Open the CSV file for reading
with open('events.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Specify the event type to filter by
    event_type_to_filter = "INSERTED"
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the current row has the desired event type
        if row[0] == event_type_to_filter:
            # Print the row to the terminal
            print(', '.join(row))  # Join elements of each row with a comma and print