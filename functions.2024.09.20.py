# Funktion för att lägga till element i en lista
def add_to_list(my_list, element):
    my_list.append(element)
    print(f"Element '{element}' har lagts till listan.")

# Funktion för att skriva ut alla element i listan
def print_list(my_list):
    print("Innehållet i listan:")
    for item in my_list:
        print(item)

# Funktion för att ta bort element från listan
def remove_from_list(my_list, element):
    if element in my_list:
        my_list.remove(element)
        print(f"Element '{element}' har tagits bort från listan.")
    else:
        print(f"Element '{element}' finns inte i listan.")

# Huvudprogram med match-case
def main():
    my_list = []
    while True:
        action = input("Vill du (1) lägga till, (2) skriva ut, (3) ta bort, eller (4) avsluta? ")

        match action:
            case '1':
                element = input("Ange ett element att lägga till: ")
                add_to_list(my_list, element)
            case '2':
                print_list(my_list)
            case '3':
                element = input("Ange ett element att ta bort: ")
                remove_from_list(my_list, element)
            case '4':
                print("Avslutar programmet.")
                break
            case _:
                print("Ogiltigt val, försök igen.")

# Kör programmet
if __name__ == "__main__":
    main()
