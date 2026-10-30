# Shipping as a function. Write shipping_charge(weight_kg, city) 
# that returns the charge as a number: Rs 200 for Karachi, Lahore and Islamabad, 
# Rs 350 for every other city, and double that when the weight is over 5 kg. 
# Clean the city inside the function, so " karachi " counts as Karachi. 
# Call it for at least four combinations, including exactly 5 kg, 
# and print each result with your format_rupees() function, 
# for example Shipping to Karachi: Rs 200. 
# If you solved Demo 4, problem 4, add its free-shipping rule as a third parameter, order_total.


def shipping_charge(weight_kg, city):
    city = city.title()
    if city == "Islamabad" or city == "Lahore" or city == "Karachi":
        charges = 200

    else:
        charges = 350
        if weight_kg > 5:
            charges *= 2
    return format_rupees(charges, city)

def format_rupees(amount, city):
    return print(f"Shipping to {city}: Rs {amount}")

shipping_charge(6,"islamaba")


    