def load_default_data():
    return [
            {
                "id": 1,
                "name": "Luna",
                "species": "katė",
                "birth_year": 2020
            },
            {
                "id": 2,
                "name": "Rex",
                "species": "šuo",
                "birth_year": 2018
            },
            {
                "id": 3,
                "name": "Bela",
                "species": "voverė",
                "birth_year": 2024
            }
        ]

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
    id_counter += 1
    pet = {
        "id": id_counter,
        "name": vardas,
        "species": rusis,
        "birth_year": gim_metai,
    }
    pets.append(pet)
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

def remove_pets(pets):
    print("Gyvūno pašalinimas iš sąrašo")
    print("Įveskite ID gyvūno, kurį norite pašalinti iš sąrašo:")
    delete_id = input()
    for pet in pets:
        if delete_id == str(pet["id"]):
            print(
                f'{pet["id"]}. PAŠALINAMA: gyvūnas: {pet["name"]}, {pet["species"]}, gimimo metai: {pet["birth_year"]}.')
            pets.remove(pet)