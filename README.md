# List_to_FiveCast

## Overview
This tool allows users to generate a CSV file containing Twitter usernames. It takes a text file containing a list of usernames and creates a CSV file with two columns: the first column containing the text "TWITTER" for each row, and the second column containing the usernames.

## Usage
1. Prepare a text file named `usernames.txt` containing the usernames, with each username on a separate line.
2. Run the script using the following command:

    ```bash
    python create_twitter_csv.py
    ```

3. After running the script, a CSV file named `twitter_accounts.csv` will be generated in the same directory.
## Example
Suppose you have a text file named `usernames.txt` with the following content:
- user1
- user2
- user3

After running the script, the `twitter_accounts.csv` file will contain the following content:
- TWITTER,user1
- TWITTER,user2
- TWITTER,user3

## Requirements
- Python 3.x

## Notes
- Ensure that the text file `usernames.txt` is properly formatted with each username on a separate line.
- The output CSV file will always have "TWITTER" in the first column for each row.
- This tool is intended for generating CSV files compatible with certain applications or data processing tasks.


