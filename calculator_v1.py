print("""
    + - / x
""")
calculate = input("How do you want to calculate: ")
calculate_num1 = int(input("enter your first number "))
calculate_num2 = int(input("enter the secound number "))
plus = calculate_num1+calculate_num2
substraction = calculate_num1-calculate_num2
divison = calculate_num1/calculate_num2
multiply = calculate_num1*calculate_num2
data = [plus,substraction,divison,multiply]
if calculate == "+":
    print(f"Result : {plus}")
elif calculate == "-":
    print(f"Result : {substraction}")
elif calculate == "/":
    print(f"Result : {divison}")
elif calculate == "x":
    print(f"Result : {multiply}")
else:
    print("Failed process ,try again later!!")
Numbers = {
    1 :"one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
    }
output=""
for count in data:
    output += str(Numbers.get(count," "))
print(output)
