# user input
stock = int(input('Please enter an initial stock level: '))
month = int(input('Please enter the number of month to plan: '))
stock_in_hand = stock
no_months_plan = []  # months list
for i in range(month):
    month_p = i + 1
    print('for month: ', month_p)
    value = int(input('Please enter the planned sales quantity for month: '))
    no_months_plan.append(value)  # months list creation
print('The resulting production quantities are:')  # result printing
for j in range(month):
    month_ = j + 1  # for displaying proper month in output
    if stock_in_hand > no_months_plan[j]:
        production = 0
        stock_in_hand = stock_in_hand - no_months_plan[j]
    else:
        production = no_months_plan[j] - stock_in_hand
        stock_in_hand = 0
    print('Production quantity for  month', month_, '-', production)
