import csv
from datetime import datetime

# Define the data to be written to the CSV file
data = [
    ["INSERTED", "Placement", 12, "null", "2018-04-10 12:34:56.789"],
    ["INSERTED", "Placement", 13, "null", "2018-04-10 12:43:10.123"],
    ["UPDATED", "Company", 123, "[status, companyURL]", "2018-04-10 12:44:00.123"],
    [
        "UPDATED",
        "Placement",
        13,
        "[status, hoursPerDay, overtimeRate]",
        "2018-04-10 14:52:43.699",
    ],
]

# Validate event type and timestamp format
for row in data:
    # Validate event type
    if row[0] not in ["INSERTED", "UPDATED", "DELETED"]:
        raise ValueError("Invalid event type:", row[0])

    # Validate timestamp format
    try:
        datetime.strptime(row[-1], "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        raise ValueError("Invalid timestamp format:", row[-1])

# Open the CSV file in write mode
with open("events.csv", "w", newline="") as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(
        ["event type", "entity name", "entity id", "[fields updated]", "timestamp"]
    )
    # Write the data rows
    writer.writerows(data)


def print_all_data(csv_file):
    """
    Print all data from CSV file to the terminal.

    Args:
        csv_file (str): Path to the CSV file.
    """
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))  # Join elements of each row with a comma and print


def filter_by_event_type(csv_file, event_type):
    """
    Filter data by event type and print to the terminal.

    Args:
        csv_file (str): Path to the CSV file.
        event_type (str): Event type to filter by.
    """
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == event_type:
                print(
                    ", ".join(row)
                )  # Join elements of each row with a comma and print


def filter_by_field(csv_file, field_name):
    """
    Filter data where event affects a particular field and print to the terminal.

    Args:
        csv_file (str): Path to the CSV file.
        field_name (str): Field name to filter by.
    """
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            fields_updated = row[3][1:-1].split(
                ", "
            )  # Extract fields updated from the row
            if field_name in fields_updated:
                print(
                    ", ".join(row)
                )  # Join elements of each row with a comma and print


def filter_by_timestamp_range(csv_file, start_timestamp, end_timestamp):
    """
    Filter data by timestamp range and print to the terminal.

    Args:
        csv_file (str): Path to the CSV file.
        start_timestamp (str): Start timestamp in '%Y-%m-%d %H:%M:%S.%f' format.
        end_timestamp (str): End timestamp in '%Y-%m-%d %H:%M:%S.%f' format.
    """
    try:
        # Parse start and end timestamps
        start_datetime = datetime.strptime(start_timestamp, "%Y-%m-%d %H:%M:%S.%f")
        end_datetime = datetime.strptime(end_timestamp, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        raise ValueError("Invalid timestamp format")

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            timestamp = datetime.strptime(row[-1], "%Y-%m-%d %H:%M:%S.%f")
            if start_datetime <= timestamp <= end_datetime:
                print(
                    ", ".join(row)
                )  # Join elements of each row with a comma and print


def filter_combination(csv_file, start_timestamp, end_timestamp):
    """
    Filter data for a combination of different factors: filter all UPDATED events where status changed within the specified timestamp range and print to the terminal.

    Args:
        csv_file (str): Path to the CSV file.
        start_timestamp (str): Start timestamp in '%Y-%m-%d %H:%M:%S.%f' format.
        end_timestamp (str): End timestamp in '%Y-%m-%d %H:%M:%S.%f' format.
    """
    try:
        # Parse start and end timestamps
        start_datetime = datetime.strptime(start_timestamp, "%Y-%m-%d %H:%M:%S.%f")
        end_datetime = datetime.strptime(end_timestamp, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        raise ValueError("Invalid timestamp format")

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row[0] == "UPDATED":  # Check if event type is UPDATED
                timestamp = datetime.strptime(row[-1], "%Y-%m-%d %H:%M:%S.%f")
                # Check if the timestamp falls within the specified range
                if start_datetime <= timestamp <= end_datetime:
                    fields_updated = row[3][1:-1].split(", ")
                    # Check if 'status' field is among the fields updated
                    if "status" in fields_updated:
                        print(
                            ", ".join(row)
                        )  # Join elements of each row with a comma and print


# System usage (printed to terminal):

# Get all event data
print("All event data:")
print_all_data("events.csv")

print("\n")  # Add a newline for separation

# Get all events of a specific event type
print("All events where event type is 'INSERTED':")
filter_by_event_type("events.csv", "INSERTED")

print("\n")

# Get all events affecting a particular field
print("All events where status field is updated:")
filter_by_field("events.csv", "status")

print("\n")

# Get all events between two timestamps (inclusive)
print(
    "All events between 2018-04-10 12:40:00.000 and 2018-04-10 14:00:00.000 (inclusive):"
)
filter_by_timestamp_range(
    "events.csv", "2018-04-10 12:40:00.000", "2018-04-10 14:00:00.000"
)

print("\n")

# Get all UPDATED events where status changed between 2018-04-10 12:00:00.000 and 2018-04-10 12:50:00.000
print(
    "UPDATED events where status changed between 2018-04-10 12:00:00.000 and 2018-04-10 12:50:00.000:"
)
filter_combination("events.csv", "2018-04-10 12:00:00.000", "2018-04-10 12:50:00.000")
