# # Shipping rules. Given weight_kg, order_total and city, work out the shipping charge:

# # Orders over Rs 10,000 ship free anywhere.
# # Karachi, Lahore and Islamabad: Rs 200 up to 5 kg, Rs 400 above that.
# # Every other city: Rs 350 up to 5 kg, Rs 700 above that.
# Customers type the city themselves, so clean city first: " karachi " must count as Karachi.
# Print Shipping to Karachi: Rs 200. Test at least five combinations, including exactly 5 kg.

givenWeight = 6
orderTotal = 3000
city = input("")

city = city.title()
if orderTotal >= 10000:
    print("Ship free anywhere")

elif city == "Karachi" or city == "Islamabad" or city == "Lahore":
    if(givenWeight > 5):
        print(f"Shipping to {city} 400 rupees")
    else:
        print(f"Shipping to {city} 200 rupees")

else: 
    if(givenWeight > 5):
        print(f"Shipping to {city} 700 rupees")

    else:
        print(f"Shipping to {city} 350 rupees")
