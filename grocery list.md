A Grocery List for supermarket shopping with name, price and quantity. 
If the list already contains an item then it only updates the price and quantity it do not append the item name again. 
The user puts his/her budget initially and the amount is subtracted from the budget after adding a new item in the list. If budget go zero/0 then no more items could be bought and if some money left and users add items greater than the budget left then it informs “over price”.
After the list is made, from money left in the budget the code suggests items which you can buy(within the budget) from the list made.

Example input and output:
Enter Your budget : 500
1.Add an item
2.Exit

Enter your choice : 1

Enter product : corn flour
Enter quantity : 1.5 kg
Enter Price : 100

Amount left : 400

1.Add an item
2.Exit

Enter your choice : 1

Enter product : wheat
Enter quantity : 2 kg
Enter Price : 100

Amount left : 300

1.Add an item
2.Exit

Enter your choice : 1

Enter product : corn flour
Enter quantity : 2 kg
Enter Price : 250

Amount left : 150

1.Add an item
2.Exit

Enter your choice : 1

Enter product : rice
Enter quantity : 5 kg
Enter Price : 300

Can't Buy the product ###(because budget left is 150)

1.Add an item
2.Exit

Enter your choice : 1

Enter product : xyz
Enter quantity : 1 kg
Enter Price : 50

Amount left : 100

1.Add an item
2.Exit

Enter your choice : 2

Amount left can buy you wheat

GROCERY LIST is:
Product name    Quantity    Price
corn flour       2 kg         250
wheat            2 kg         100
xyz              1 kg          50
