# Written by: Micah Anderson
# Date Started: 11/17/2026
# Takes a .txt file of a receipt and converts it to a .xlsx file

import sys

# Function: Reads the receipt file you want to add to your spreadsheet
# Inputs: receipt_file - string - the name of the file you are reading from
# Outputs: text - string - the contents of the file
def readReceipt(receipt_file):
    try:
        with open(receipt_file, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    return text

def main():
    print(readReceipt("receipt.txt"))

if __name__ == "__main__":
    main()