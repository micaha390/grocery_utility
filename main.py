# Written by: Micah Anderson
# Date Started: 11/17/2026
# Takes a .txt file of a receipt and converts it to a .csv file

import sys

TAX_RATE = .06
BOTTLE_DEPOSIT = .05

# Function: Reads the receipt file you want to add to your spreadsheet
# Inputs: receipt_file - string - the name of the file you are reading from
# Outputs: text - list[str] - the contents of the file
def readReceipt(receipt_file):
    try:
        with open(receipt_file, "r", encoding="utf-8") as file:
            text = file.read().splitlines()
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    for i in range(len(text)):
        text[i] = text[i].split(", ")
    return text

# Function: Returns the tax for a taxable item
# Inputs: cost - string - a taxable item's cost
# Outputs: float - the amount of tax on the taxable item
def tax(cost):
    return float(cost) * TAX_RATE

# Function: Returns the bottle deposit for an eligible item
# Inputs: amount - string - the number of bottles/cans purchased
# Outputs: float - the bottle deposit cost
def bottleDeposit(amount):
    return float(amount) * BOTTLE_DEPOSIT

# Dictionary that maps additional tags onto their functions
tags = {"tax": tax, "bottle deposit": bottleDeposit}

def main():
    receipt = readReceipt("receipt.txt")
    for item in receipt:
        print(f"{item[1]} {item[2]} of {item[0]}, costing ${item[3]}")

if __name__ == "__main__":
    main()