import csv

transactions = []

def finance_manager(file):
   sum = 0

   with open(file, mode="r") as csv_file:
      csv_header = csv.reader(csv_file)
      header = next(csv_header)
      for row in csv_header:
        # get name, amout, currency
        name = row[4]
        amount = float(row[7])
        date = row[1]

        transaction = (date, name, amount)
        sum += amount
        transactions.append(transaction)
   print(f"The sum of your transactions this month is ${sum}")
   print('')
   return transactions

user_input = input("Enter filename properly: ")
print(finance_manager(user_input))

