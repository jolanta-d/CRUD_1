import csv

headers = ["id", "name", "species", "birth_year"]

def load_pets():
    with open("pets.csv", mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def save_pets(pets):
    with open("pets.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(pets)

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti visus gyvūnus")
    print("2. Įtraukti naują gyvūną į sąrašą")
    print("3. Redaguoti gyvūnus")
    print("4. Šalinti gyvūnus iš sąrašo")
    print("5. Išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")

def print_pets(pets):
    for pet in pets:
        print(f'{pet["id"]}. Gyvūnas: {pet["name"]}, {pet["species"]}, gimimo metai: {pet["birth_year"]}.')

def create_pets(pets, id_counter):
    print("Naujo gyvūno įvedimas")
    print("Įveskite naujo gyvūno vardą:")
    vardas = input()
    print("Įveskite naujo gyvūno rūšį:")
    rusis = input()
    print("Įveskite naujo gyvūno gimimo metus:")
    gim_metai = int(input())
    id_counter = int(pets[-1]["id"]) + 1 if len(pets) > 0 else 1
    pet = {
        "id": id_counter,
        "name": vardas,
        "species": rusis,
        "birth_year": gim_metai,
    }
    pets.append(pet)
    save_pets(pets)
    return id_counter

def edit_pets(pets):
    print("Gyvūno redagavimas")
    print("Įveskite ID gyvūno, kurį norite redaguoti:")
    edit_id = input()
    for pet in pets:
        if edit_id == str(pet["id"]):
            print(
                f'{pet["id"]}. Gyvūnas: {pet["name"]}, {pet["species"]}, gimimo metai: {pet["birth_year"]}.')
            print("Įveskite gyvūno vardą:")
            pet["name"] = input()
            print("Įveskite gyvūno rūšį:")
            pet["species"] = input()
            print("Įveskite gyvūno gimimo metus:")
            pet["birth_year"] = input()
    save_pets(pets)

def remove_pets(pets):
    print("Gyvūno pašalinimas iš sąrašo")
    print("Įveskite ID gyvūno, kurį norite pašalinti iš sąrašo:")
    delete_id = input()
    for pet in pets:
        if delete_id == str(pet["id"]):
            print(
                f'{pet["id"]}. PAŠALINAMA: gyvūnas: {pet["name"]}, {pet["species"]}, gimimo metai: {pet["birth_year"]}.')
            pets.remove(pet)
    save_pets(pets)