# Written by: Micah Anderson
# Date Started: 11/17/2026
# Takes a .txt file of a receipt and converts it to a .csv file

import sys

TAX_RATE = .07
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
# Inputs: item - list[str] - the item eligible for tax
# Outputs: float - the amount of tax on the taxable item
def tax(item):
    # item[3] is the base cost of the item
    return float(item[3]) * TAX_RATE

# Function: Returns the bottle deposit for an eligible item
# Inputs: item - list[str] - the item eligible for bottle deposit
# Outputs: float - the bottle deposit cost
def bottleDeposit(item):
    # item[1] is the amount of the item
    return float(item[1]) * BOTTLE_DEPOSIT

# Dictionary that maps additional tags onto their functions
tags = {"tax": tax, "bottle deposit": bottleDeposit}

def main():
    receipt = readReceipt("receipt.txt")
    for item in receipt:
        # sets totalCost to the listed price
        totalCost = float(item[3])
        # checks to see if there are more attributes to the item than the base 4, then applies additional fees
        if (len(item) > 4):
            # creates an iterator to go from the 4th attribute to the end of the items attributes
            iterator = 4
            while(iterator < len(item)):
                totalCost += tags[item[iterator]](item)
                iterator += 1
        print(f"{item[1]} {item[2]} of {item[0]}, costing ${totalCost:.2f}")



if __name__ == "__main__":
    main()