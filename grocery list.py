l1=[]
l2=[]
l3=[]
l4=[]
oldprice=0
oldquantity=0
budget=int(input("Enter your budget:"))
while True:
    flag=0
    flag2=0
    print("1. Add an item")
    print("2. Exit")
    option=int(input("Enter your choice:"))
    if option==1:
        product=input("Enter product:")
        quantity=input("Enter quantity:")
        price=int(input("Enter price:"))
        for i,j in enumerate(l1):
            if j==product:
                flag=1
                oldquantity=l2[i]
                oldprice=l3[i]
                l2[i]=quantity
                l3[i]=price
                budget=budget-price+oldprice
                print("Amount left = {}".format(budget))
        if (budget-price)>0:
            flag2=1
            if flag!=1:
                l1.append(product)
            l2.append(quantity)
            l3.append(price)
        if flag==0 and flag2==1:
            budget=budget-price
            print("Amount left = {}".format(budget))
        if flag2==0 and flag!=1:
            print("Can't Buy the product ###(because budget left is {})".format(budget))
    else:
        for j in range(0,len(l3)):
            if l3[j]<=budget:
                l4.append(l1[j])
        if len(l4)!=0:
            print("Amount left can buy you ")
            for k in range(0,len(l4)):
                print(l4[k],sep=", ")
        print("Grocery list is:")
        print("Product name     Quantity     Price")
        for i in range(0,len(l1)):
            print("{0:12}     {1:^8}     {2:5}".format(l1[i],l2[i],l3[i]))
        exit()
