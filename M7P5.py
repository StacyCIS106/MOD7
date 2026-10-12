user_prompt = input("Do you want to do this program? (yes/no): ")
sum_discount1 = 0
while user_prompt == 'yes' or user_prompt == 'YES' or user_prompt == 'Yes':
    item_quantity = int(input("Enter the quantity of the item: "))
    item_price = int(input("Enter the price of the item: "))
    ext_price = item_quantity * item_price
    if ext_price > 1000.00:
        discount = ext_price * 0.25
    else:
        discount = ext_price * .10
    total_price = ext_price - discount
    sum_discount1 = discount + sum_discount1
    print("Total discount for all items: ", sum_discount1)
    print("ext_price, discount, total_price: ", ext_price, discount, total_price)
    user_prompt = input("Do you want to do this program? (yes/no): ")
    