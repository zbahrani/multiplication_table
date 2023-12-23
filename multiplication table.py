#Getting Input from the User
while True:
    try:
        number = int(input("please enter your number: "))
        break  # If a number is entered, exit the loop.
    except ValueError:
        print("Invalid input. Please enter an integer.")

#Print the title
print(f"multiplication_table: {number}")

#Creat multiplication table
for i in range(1,11):
    result = number * i 
    print(f"{number} * {i} = {result}")
    
