option = "yes"
while option.lower() != "no": 
    total_amount = int(input("Enter the total purchase amount: "))
    initial_amount = float(f"{total_amount:.2f}")
    print(f"Initial Purchase Amount: {initial_amount}")

    if total_amount > 5000:
        discount = total_amount * 0.10
        total_amount = total_amount - discount
        print(f"Discount: {discount:.2f}")
        print(f"Final Price: {total_amount:.2f}")
    else:
        discount = total_amount * 0.05
        total_amount = total_amount - discount
        print(f"Discount: {discount:.2f}")
        print(f"Final Price: {total_amount:.2f}")

    option = input("Do you want to try again? (yes/no): ")
    if option != "yes":
        print("Thank you!")


