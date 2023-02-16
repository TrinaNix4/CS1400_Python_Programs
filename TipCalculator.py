# Tip Calculator
# Allow the user to enter the cost of the meal
# allow the user to enter the service: Excellent, Good, Poor
# Calculate the total cost of the meal, including tip

print("Tip Calculator")
cost = float(input("Enter the cost of your meal: "))
service = input("How would you rate your service?: Excellent, Good, or Poor")

percentage = .10

if service == "Excellent" or service == "excellent":
    percentage += .10
elif service == "Good" or service == "good":
    percentage += .05


tip = cost * percentage
cost += tip
print("Tip: ", round(tip))
print("Cost: ", round(cost))
