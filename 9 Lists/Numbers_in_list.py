user_input = ""
number_list = []
while True:
    user_input = input('Enter a number: ')
    if user_input == "done":
        print(f"Maximum: {max(number_list)}")
        print(f"Minimum: {min(number_list)}")
        break
    try:
        user_input = int(user_input)
    except:
        print("Invalid input")
    else:
        number_list.append(user_input)