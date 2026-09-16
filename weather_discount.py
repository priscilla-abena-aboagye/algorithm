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