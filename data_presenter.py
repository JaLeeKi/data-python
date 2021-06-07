# Create a new file called data_presenter.py.
# Open the CupcakeInvoices.csv.

open_file = open('CupcakeInvoices.csv')

# Loop through all the data and print each row.

for line in open_file:
  print(line)

# Loop through all the data and print the type of cupcakes purchased.

for line in open_file:
  values = line.split(',')
  print(values[2])

# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

for line in open_file:
  values = line.split(',')
  quantity = int(values[3])
  price = float(values[4])
  total = quantity * price
  print(total)

# Loop through all the data, and print out the total for all invoices combined.

total = 0

for line in open_file:
  values = line.split(',')
  quantity = int(values[3])
  price = float(values[4])
  total = total + (quantity * price)
  
print(total)

# Close your open file.

open_file.close()