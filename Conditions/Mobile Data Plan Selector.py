"""
Docstring for Conditions.Mobile Data Plan Selector
🔹 2. Mobile Data Plan Selector
Scenario:
A telecom company recommends a plan based on usage.
Rules:
If data_usage > 50 GB → Premium Plan
Else if data_usage > 20 GB → Standard Plan
Else if data_usage > 5 GB → Basic Plan
Else → Mini Plan
Task:
Write a program to print the suggested plan.
"""
data_usage  = int(input("Enter the data you want to use in Gb: "))

if data_usage > 50:
    print(" Premium Plan")
elif data_usage > 20:
    print("Standard Plan")
elif data_usage > 5:
    print("Basic plan")
else:
    print("Mini plan")
