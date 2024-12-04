price = .99

pounds = float(input('How many pounds do you want to order?'))

gross_sales = pounds * price

print('Gross sales:',gross_sales)

discount = 0
if (pounds>=10) and (pounds<99.99):
    discounts = 0.1
    print('discount' , discount)
if (pounds>=100) and (pounds<999.99):
    discount = 0.2
    print('discount' , discount)
if (pounds>=1000) and (pounds<9999.99):
    discount = 0.3
    print('discount' , discount)
if (pounds>=10000):
    discount = 0.4
    print('discount' , discount)

discountamount = gross_sales*discount
finalamount = gross_sales-discountamount
print('discount:',discountamount)
print('final amount:',finalamount)
