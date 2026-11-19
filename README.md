# grocery_utility
Uses a .txt file where you enter info off of a receipt and automatically moves it to an excel sheet for tracking costs.

The .txt file needs to be formatted as follows, with commas separating attributes of each item, and new lines separating items:

NAME OF ITEM, AMOUNT OF ITEM, UNITS, COST, ADDITIONAL TAGS, ..., 

The additional tags will be additional costs such as tax and bottle deposit. The program will run all values after the first 4 mandatory columns through a dictionary to determine added costs.

PLANNED

  export to a growing .xlsx using openpyxl to keep a long term budget
  
  experimenting with OCR tools to update the sheet directly from a photo of a receipt and avoid entering data all together
