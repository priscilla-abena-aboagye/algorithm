'''
distance_mi = 6
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False

if not distance_mi:
    print("False")

elif distance_mi <= 1:
    if not is_raining:
        print("True")
    else:
        print("False")

elif (distance_mi > 1 and distance_mi <= 6):
    if has_bike and not is_raining:
        print("True")
    else:
        print("False")

elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print("True")
    else:
        print("False")
else:
    print("False")

# discount calculator

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number" 
    
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    if price <= 0:
        return "The price should be greater than 0"
    
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discount = (discount / 100) * price

    final_price = price - discount



    return final_price
print(apply_discount(50, 20))

# An example of enumerate 
names_of_friends = ["Ama", "Ceydes", "Baaba", "Veve", "Azuu", "Florain"]

for name in names_of_friends:
    print(name)

for index, name in enumerate(names_of_friends):
    print(f"Index Number: {index} Name: {name}")

# enumerate also takes start
# when you don't bring it it default is 0

for index, name in enumerate(names_of_friends, 4):
    print(f"Index Number: {index} Name: {name}")

# An example of zip
# the zip returns a tuple
items = ["bottle", "socks", "laptop", "inhaler", "bag", "piano"]
owners = ["Priscilla", "Frank", "Ben", "Grace", "Godwin", "Belinder"]

print(list(zip(items, owners)))

for item, owner in zip(items, owners):
    print(f"Items: {items}")
    print(f"Owners: {owners}")

'''
# list comprehension

for num in range(11):
    if num % 2 == 0:
        print(num)

even_numbers = [num for num in range(11) if num % 2 ==0]
print(even_numbers)

for num in range(11):
    if num % 2 == 0:
        print(f"Even: {num}")
    else:
        print(f"Odd: {num}")

numbers = ["even" if num % 2 == 0 else "Odd" for num in range(11)]
print(numbers)

