monthly_sales = [42, 38, 33, 38, 40, 45]

sales_limit = 35

for sales_amount in monthly_sales:
    if sales_amount < sales_limit:
        print(f"Sales amount {sales_amount} is below the sales limit")
        break
    else:
        print(f"Sales amount {sales_amount} is above the sales limit")



monthly_sales = [42, 38, 33, 38, 40, 45]
months = ["Jan", "Feb", "March", "April", "May", "June"]

sales_limit = 35

for sales_amount, month in zip(monthly_sales, months):
    if sales_amount < sales_limit:
        print(f"Sales amount {sales_amount} is less than the sales limit in {month}")
        break
    else:
        print(f"Sales amount {sales_amount} is greater than the sales limit in {month}")

        