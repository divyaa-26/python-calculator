print("Welcome to my calculator")

while True:
    print("\nChoose operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    user_choice = input("Enter your choice (1/2/3/4): ")

    if user_choice not in ['1', '2', '3', '4']:
        print("Invalid choice, try again.")
        continue

    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
    except:
        print("Please enter valid numbers.")
        continue

    if user_choice == '1':
        answer = first_num + second_num
        print("Result:", answer)

    elif user_choice == '2':
        answer = first_num - second_num
        print("Result:", answer)

    elif user_choice == '3':
        answer = first_num * second_num
        print("Result:", answer)

    elif user_choice == '4':
        if second_num == 0:
            print("Cannot divide by zero")
        else:
            answer = first_num / second_num
            print("Result:", answer)

    again = input("\nDo you want to continue? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for using calculator!")
        break