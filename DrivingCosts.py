print("Welcome to the Driving Cost Calculator. I will calculate the cost of driving from Weber State University to 3 cities of your choice. Let's get started!")

carMilesPerGallon = input("How many miles per gallon does your car get?")
currCostOfGas = input("What is the current cost of gas per gallon?")

city1 = input(
    "Enter the first city you'd like to calculate the cost to drive to: ")
milesToCity1 = int(input(
    "How many miles is it from Weber State University to your first city?"))
costToCity1 = (int(milesToCity1) /
               int(carMilesPerGallon)) * float(currCostOfGas)

print('The cost for driving to', city1, 'is $', round(costToCity1, 2))

city2 = input(
    "Next, enter the second city you'd like to calculate the cost to drive to: ")
milesToCity2 = int(input(
    "How many miles is it from Weber State University to your second city?"))
costToCity2 = (int(milesToCity2) /
               int(carMilesPerGallon)) * float(currCostOfGas)

print('The cost for driving to', city2, 'is $', round(costToCity2, 2))

city3 = input(
    "Last, enter the third city you'd like to calculate the cost to drive to: ")
milesToCity3 = int(input(
    "How many miles is it from Weber State University to your third city?"))
costToCity3 = (int(milesToCity3) /
               int(carMilesPerGallon)) * float(currCostOfGas)

print('The cost for driving to', city3, 'is $', round(costToCity3, 2))
