

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

mon_sales = int(mon_sales)
#mon_sales = type(mon_sales)
#print(mon_sales)

tues_sales = int(tues_sales)
wed_sales = int(wed_sales)
thurs_sales = int(thurs_sales)
fri_sales = int(fri_sales)

#to get the total sales simply add all sales of the week

total_sales = mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales

#using the string formatting
print( "This week's total sales: %s" %(total_sales))
    