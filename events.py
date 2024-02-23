import csv

# Define the data to be written to the CSV file
data = [
    ["INSERTED", "Placement", 12, "null", "2018-04-10 12:34:56.789"],
    ["INSERTED", "Placement", 13, "null", "2018-04-10 12:43:10.123"],
    ["UPDATED", "Company", 123, "[status, companyURL]", "2018-04-10 12:44:00.123"],
    ["UPDATED", "Placement", 13, "[status, hoursPerDay, overtimeRate]", "2018-04-10 14:52:43.699"]
]

# Open the CSV file in write mode
with open('events.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["event type", "entity name", "entity id", "[fields updated]", "timestamp"])
    # Write the data rows
    writer.writerows(data)