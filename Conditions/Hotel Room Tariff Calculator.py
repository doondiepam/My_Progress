numbers_nights = int(input("Enter the NUmber of nights coustomer stayed: "))
room_type = input()
season = int(input("Enter which is  season it is "))


if room_type == "Standard":
    price = 2000
elif room_type == "Deluxe":
    price = 3500
elif room_type == "Suite":
    price = 6000

print("Original price is : ", price)
print("The room type is ", room_type)
Discount = 0
if numbers_nights > 5:
    Discount = price * 10/100
    print("Discount is:", Discount)

if season == "during peak season":
    price = price + 25/100

if price < 5000:
    price = price + 500


print("the total price after all is:", price)
