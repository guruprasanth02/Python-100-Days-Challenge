# 🌟 Day 54: Shop Earnings Tracker Program 💰

### 🎊 Today’s Highlights:

* **CSV File Handling:** We read and processed a CSV file containing daily sales data, including the cost and quantity of items sold.
* **Data Calculation:** For each item, we calculated the total earnings by multiplying the cost by the quantity, summing it up to get the total earnings for the day.
* **File Reading and Processing:** We used Python's built-in ```csv``` library to read and process the CSV file, treating the data in a structured way.

### 🔍 Key Concepts:

* **CSV File Parsing:** We focused on reading and parsing data from a CSV file, which is structured with rows and columns. We used Python's ```csv.DictReader()``` for handling the data as a dictionary.
* **Data Type Conversion:** Since values like the cost and quantity are strings in the CSV file, we needed to convert them to numbers (e.g., ```float()``` for cost) to perform calculations.
* **Looping and Summing:** We looped through each row in the CSV file, calculated the earnings for each item, and kept a running total using simple arithmetic.

### 👉 Day 54 Challenge:

**Task Overview:**

Your task was to read a CSV file, calculate the daily earnings of a shop by multiplying the cost of an item by its quantity, and then sum up all the earnings for the day. The final output should show how much money the shop made in a day.

Example Output:

**🌟 Shop $$ Tracker🌟**
Your shop took £592 pounds today.

### 🛠️ Common Errors Encountered:

* **Missing Total Calculation:** If the calculation for the total earnings is skipped or done incorrectly, the program will fail to output the correct earnings.

  **Fix:** Ensure the multiplication and summing operations are correctly implemented, and check the data types of the inputs.

* **Incorrect Data Types:** If the data from the CSV file is not converted properly (e.g., treating the cost and quantity as strings), calculations will fail.

  **Fix:** Cast the values to appropriate data types (e.g., ```float()``` for the cost and ```int()``` for the quantity).

* **File Read/Write Issues:** Sometimes the file might not be read properly, or the format of the CSV might not match the expected structure.

  **Fix:** Double-check the CSV file format and ensure the data is structured as expected.

### My Code:
```python
import csv

total = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row["Quantity"]) * float(row["Cost"])

print(f"Total: ${round(total,2)}")
