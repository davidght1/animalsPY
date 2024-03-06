# Function to create dictionary
def populate_animal_dict():
    animal_dict = {}
    strings = ["Dog12, CAT3, LiOn7, DolphiN11, fish6", "PIG17, bear29, BiRd8", "SNAKE39, donkey14"]

    for txt in strings:
        animals = txt.split(', ')
        for animal in animals:

            last_non_digit_index = len(animal) - 1
            while last_non_digit_index >= 0 and animal[last_non_digit_index].isdigit():
                last_non_digit_index -= 1

            name, code_part = animal[:last_non_digit_index + 1].lower(), animal[last_non_digit_index + 1:]
            
            code = ''.join(char for char in code_part if char.isdigit())
            
            if code:
                animal_dict[name] = {"code": int(code), "name": name.capitalize(), "type": ""}
            else:
                print(f"Invalid format for animal: {animal}. Skipping.")

    return animal_dict

# Function for option 1
def search_by_code():
    code_to_search = int(input("Enter the animal code: "))
    for name, data in animal_dict.items():
        if data["code"] == code_to_search:
            print(f"Code: {data['code']},")
            print(f"Name: {data['name']}") 
            print(" --------------- ")
            return
    print("Animal not found.")

# Function for option 2
def search_by_name_partial(name_input):
    matching_animals = []
    name_input = name_input.lower()

    for name, data in animal_dict.items():
        if name_input in name:
            print(f"Code: {data['code']},")
            print(f"Name: {data['name']}") 
            print(" --------------- ")
            matching_animals.append(data)

    if not matching_animals:
        print("No matching animals found.")

# Function for option 3
def add_animal():
    new_animal_name = input("Enter the name of the new animal: ").lower()
    new_animal_code = input("Enter the code for the new animal: ")

    if not new_animal_code.isdigit():
        print("Invalid input. next time write a number and not a string.")
        return

    new_animal_code = int(new_animal_code)

    # Check if the code exists
    for name, data in animal_dict.items():
        if data["code"] == new_animal_code:
            print(f"Animal with code {new_animal_code} already exists. Cannot create the animal.")
            return

    animal_dict[new_animal_name] = {"code": new_animal_code, "name": new_animal_name.capitalize(), "type": ""}
    print(f"Animal {new_animal_name.capitalize()} added successfully!")


# Function for option 4
def delete_animal():

    code_to_delete_input = input("Enter the code of the animal to delete: ")

    if not code_to_delete_input.isdigit():
        print("Invalid input. next time write a number and not a string.")
        return 

    code_to_delete = int(code_to_delete_input)

    for name, data in animal_dict.items():
        if data["code"] == code_to_delete:
            del animal_dict[name]
            print(f"Animal with code {code_to_delete} deleted successfully!")
            return

    print("Animal not found. Deletion failed.")


# Initialize the animal dictionary
animal_dict = populate_animal_dict()

# Main loop
while True:
    print("\nOptions:")
    print("1. Search by code")
    print("2. Search by name")
    print("3. Add an animal")
    print("4. Delete an animal")
    print("5. Exit")

    option = input("Enter your choice (1-5): ")

    if option == "1":
        search_by_code()
    elif option == "2":
        name_input = input("Enter the partial name to search: ")
        search_by_name_partial(name_input)
    elif option == "3":
        add_animal()
    elif option == "4":
        delete_animal()
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
