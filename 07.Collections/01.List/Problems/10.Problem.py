appliances = []
units_list = []
total_units = 0
total_amount = 0
rate_per_unit = 5

while True:
    appliance = input("Enter Appliance name (q to quit): ")

    if appliance.lower() == "q":
        break
    else:
        units = float(input(f"Enter units consumed by {appliance}: "))
        appliances.append(appliance)
        units_list.append(units)

print("\n------ Electricity Bill ------")

for appliance in appliances:
    print(appliance)

for units in units_list:
    total_units += units
    total_amount += units * rate_per_unit

print("\nTotal Units Consumed:", total_units)
print("Total Electricity Bill: ₹", total_amount)
