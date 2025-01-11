def display_menu():
    print(f"Shopping list Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Item")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input ("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list")
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list")
            else:
                print(f"{item} is not in the shopping list")
        elif choice == "3":
            print("Shopping list items:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("invalid value")

if __name__ == "__main__":
    main()