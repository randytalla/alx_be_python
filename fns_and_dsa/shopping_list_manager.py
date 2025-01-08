def display_menu():
    print("Shopping list Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Item")
    print("4. Exit")

def main():
    Shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            item = input ("Enter the item to add: ")
            Shopping_list.append(item)
            print("Item added to the list")
        elif choice == '2':
            item = input("Enter the item to remove: ")
            try:
                shopping_list.remove(item)
                print("Item removed from the list")
            except ValueError:
                print("Item not found in the list")
        elif choice == '3':
            print("Shopping list items:")
            for item in Shopping_list:
                print(item)
        elif choice == '4':
            print("Exiting the program")
            break
        else:
            print("invalid value")

if __name__ == "__main__":
    main()