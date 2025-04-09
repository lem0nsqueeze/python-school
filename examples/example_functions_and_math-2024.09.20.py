# Function to add element in a list
def add_to_list(my_list, element):
    my_list.append(element)
    print(f"The element '{element}' was added to the list.")

# Function to write out all elements in the list
def print_list(my_list):
    print("Contents in the list:")
    for item in my_list:
        print(item)

# Function to remove elements in the list
def remove_from_list(my_list, element):
    if element in my_list:
        my_list.remove(element)
        print(f"The element '{element}' has been removed from the list.")
    else:
        print(f"The element '{element}' does not exist in the list.")

# Mainprogram with match-case
def main():
    my_list = []
    while True:
        action = input("Do you want to (1) add, (2) write, (3) remove, or (4) exit? ")

        match action:
            case '1':
                element = input("Choose an element to add: ")
                add_to_list(my_list, element)
            case '2':
                print_list(my_list)
            case '3':
                element = input("Choose an element to remove: ")
                remove_from_list(my_list, element)
            case '4':
                print("Closing the program.")
                break
            case _:
                print("Invalid option, try again.")

# Run program
if __name__ == "__main__":
    main()
