pets = [
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
id_counter = 3
while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti visus gyvūnus")
    print("2. Įtraukti naują gyvūną į sąrašą")
    print("3. Redaguoti gyvūnus")
    print("4. Šalinti gyvūnus iš sąrašo")
    print("5. Išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    ivestis = input()

    match ivestis:
        case "1":
            for pet in pets:
                print(f'{pet["id"]}. Gyvūnas: {pet["name"]}, {pet["species"]}, gimimo metai: {pet["birth_year"]}.')
        case "2":
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
        case "3":
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
        case "4":
            print("Gyvūno pašalinimas iš sąrašo")
            print("Įveskite ID gyvūno, kurį norite pašalinti iš sąrašo:")
            delete_id = input()
            for pet in pets:
                if delete_id == str(pet["id"]):
                    print(f'{pet["id"]}. PAŠALINAMA: gyvūnas: {pet["name"]}, {pet["species"]}, gimimo metai: {pet["birth_year"]}.')
                    pets.remove(pet)
        case "5":
            print("Išeiti iš programos")
            break