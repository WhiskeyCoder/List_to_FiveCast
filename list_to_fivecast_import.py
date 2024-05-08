import csv

def create_twitter_csv(username_file, output_file):
    # Open the text file containing usernames
    with open(username_file, 'r') as file:
        usernames = [line.strip() for line in file.readlines()]

    # Write usernames to CSV
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(['TWITTER', 'Username'])
        # Write rows
        for username in usernames:
            writer.writerow(['TWITTER', username])

# Usage
username_file = "usernames.txt"  # Path to the text file containing usernames
output_file = "twitter_accounts.csv"  # Output CSV file

create_twitter_csv(username_file, output_file)
