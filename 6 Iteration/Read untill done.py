print("Welcome!")
user_input = ""
total = 0
count = 0
average = 0
while True:
    user_input = input("Please input a number: ")
    if user_input == "done":
        average = total/count
        print(total, count, average)
        break
    try: user_input = int(user_input)
    except: print("Bad input")
    else:
        total = total + user_input
        count = count + 1
        print(user_input)
