def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

total = sum_all(1, 2, 3, 4, 5)

print(f"Sum of all numbers: {total}")






def company_info(**details):
    if 'company_code' in details:
        print("Company Code:", details['company_code'])
        
    if 'ceo' in details:
        print("CEO:", details['ceo'])
        
    if 'revenue' in details:
        print("Revenue:", details['revenue'])


company_info(company_code='GOOGL', ceo='Sundar Pichai', revenue='307 billion')
