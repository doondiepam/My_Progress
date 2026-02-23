"""Problem: Smart Electricity Bill Calculator 
You are working for an electricity board. Write a Python program
that calculates the monthly electricity bill based on the number of units consumed.

📌 Rules:
Input the number of units used.
Billing slabs:
Units Range	Rate per Unit
0 - 100	₹1.5
101 - 200	₹2.5
201 - 300	₹4.0
Above 300	₹6.0
Additional Conditions:
If total bill > ₹1000 → give 10% discount
If total bill < ₹200 → add ₹50 fixed charge
"""


units = int(input())

if 0 <= units <=100:
    bill = units * 1.5
elif 101 <= units <=200:
    bill = units * 2.5
elif 201 <= units <=300:
    bill = units * 4.0
elif units > 300:
    bill = units * 6.0

print(units)
print("Original Bill", bill)

Discount = 0


if bill > 1000:
    Discount = bill * 10/100
    bill = bill - Discount
elif bill < 200:
    bill = bill + 50

print("Discount :", Discount)
print("final bill:", bill)
