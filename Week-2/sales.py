sales_list=[]
with open("sales.txt", "w") as file:
    file.write("200\n450\nabc\n700")
with open("sales.txt","r") as file:
    for i in file:
        try:
            number=int(i)
            sales_list.append(number)
        except:
            continue
total_sales=0
for i in sales_list:
    total_sales+=i
print("Total sales:", total_sales)
print("valid sales:", sales_list)


