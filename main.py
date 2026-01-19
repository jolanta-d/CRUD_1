from file_CRUD_1 import *

pets = load_pets()
id_counter = 3

while True:
    print_info()
    ivestis = input()
    match ivestis:
        case "1":
            print_pets(pets)
        case "2":
            id_counter = create_pets(pets, id_counter)
        case "3":
            edit_pets(pets)
        case "4":
            remove_pets(pets)
        case "5":
            print("Išeiti iš programos")
            break