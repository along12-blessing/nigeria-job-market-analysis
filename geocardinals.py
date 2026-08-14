import json as js

with open("houses.json", "r") as file:
    houses = js.load(file)
# open(...)- opens the file
# "r" means read
# json.load(..)- converts JSON - Python(list of dict)
"""for house in houses:
    print(
        f"state: {house['State']}, city: {house['Location']}, price:{house['Price']}")
"""
# for loop- iterates through the list of dictionaries


# 🔹 STEP 1 — FILTER ONLY


def filter_houses(state, ptype, budget):
    filtered_houses = []
    # this is a list to filter the houses whether it is land or house

    for house in houses:
        if (
            house['Price'] <= budget and
            house['State'].strip().lower() == state
            and house['Propaty_Type'].strip().lower() == ptype
        ):
            filtered_houses.append(house)
    return filtered_houses

# This is to display the information of the prpperty_type


def display_houses(filtered_houses):
    if not filtered_houses:
        print("No houses found matching the criteria.")
    else:
        for i, house in enumerate(filtered_houses, start=1):
            states = house['State'].strip().lower()
            location = house['Location']
            price = house['Price']
            estate_name = house['Estate_Name']
            property_type = house['Propaty_Type'].strip().lower()
         # Check if the property type is land or house and print the details accordingl
            if property_type == "land":
                print(
                    f"{i}.state: {states.title()}, city: {location}, price:₦{price},  Estate: {estate_name}")
            elif property_type == "house":
                bedroom = house['Bedroom']
                bathroom = house['Bathroom']
                print(
                    f"{i}.state: {states.title()}, city: {location}, price:₦{price}")
                print(
                    f"Estate: {estate_name}, Bedroom: {bedroom}, Bathroom: {bathroom}")


# enumerate() is a built-in function in Python that allows you to loop through an iterable (like a list) and have an automatic counter. It returns both the index and the value of each item in the iterable. In this case, it is used to print the index (starting from 1) along with the details of each house that matches the criteria.
# enumerate() gives index start=1 allows the index to start from 1 instead of the default 0. This is useful for user-friendly output, especially when listing items.

# this is to show the fill details ot
def house_choice(filtered_houses, choice):
    if choice < 1 or choice > len(filtered_houses):
        print("Invalid selection.")
    else:
        selected = filtered_houses[choice - 1]

        print("\n--- FULL DETAILS ---")

        ptype = selected['Propaty_Type'].strip().lower()

        if ptype == "land":
            print(f"Estate: {selected.get('Estate_Name', 'N/A')}")
            print(f"Location: {selected.get('Location', 'N/A')}")
            print(f"Price: ₦{selected.get('Price', 'N/A')}")
            print(f"Plot Size: {selected.get('Plot_Size_sqm', 'N/A')} sqm")
            print(
                f"Total_Area_sqm: {selected.get('Total_Area_sqm', 'N/A')} sqm")
            # print(f"Estate: {selected.get('Estate_Name', 'N/A')}") this ia a more efficient way for in case the key is not available
            # if it is not available it shows N/A if it's available it shows the value

        elif ptype == "house":
            print(f"Estate: {selected.get('Estate_Name', 'N/A')}")
            print(f"Location: {selected.get('Location', 'N/A')}")
            print(f"Price: ₦{selected.get('Price', 'N/A')}")
            print(f"Bedrooms: {selected.get('Bedroom', 'N/A')}")
            print(f"Bathrooms: {selected.get('Bathroom', 'N/A')}")
            print(f"Toilets: {selected.get('Toilet', 'N/A')}")


state = input("Enter state: ").strip().lower()
ptype = input("Enter Property type (Land/House): ").strip().lower()
budget = int(input("Enter required Budget: "))

filtered = filter_houses(state, ptype, budget)

display_houses(filtered)

if filtered:
    choice = int(input("\nSelect a property number: "))
    house_choice(filtered, choice)
