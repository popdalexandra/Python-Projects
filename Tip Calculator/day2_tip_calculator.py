# Calculate how much everyone has to pay including the tip

bill = float(input("What is the total bill? "))
tip_per = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
ppl = int(input("How many people to split the bill?"))

tip = round( ((tip_per/100)*bill + bill) / ppl , 2)

print(f"Each person should pay: {tip}")