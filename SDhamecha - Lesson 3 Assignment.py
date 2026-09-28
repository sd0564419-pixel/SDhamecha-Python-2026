#!/usr/bin/env python3

print("======================")

# get investment amount
investment = int(input("Please Enter monthly investment: "))
while investment <= 0 or investment >= 50000:
    investment = int(input("Please Enter monthly investment: "))

# get rate
rate = float(input("Please Enter interest rate: "))
while rate <= 0 or rate >= 15:
    rate = float(input("Please Enter interest rate: "))

# get years
years = int(input("Please Enter years: "))
while years <= 0:
    years = int(input("Please Enter years: "))

print("======================")

# convert values
months = years * 12
monthly_rate = rate / 12 / 100
total = 0

# calculate monthly interest
for month in range(1, months + 1):
    total += investment
    interest = total * monthly_rate
    total += interest
    
    # print yearly total
    if month % 12 == 0:
        current_year = month // 12
        print(f"Year {current_year}: ${round(total, 2)}")

print("======================")

# print final results
print(f"Investment Duration: {years} years")
print(f"Yearly Interest Rate: {rate}%")
print(f"Monthly Investment Amount: ${investment}")
print(f"Total Amount of Investment After Compounding: ${round(total, 2)}")

print("======================")

# completion message
print("Completed by, Shivang")