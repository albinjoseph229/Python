def is_substring(main_str, sub_str):
    return sub_str in main_str

def count_occurrences(main_str, char):
    return main_str.count(char)

def replace_substring(main_str, old_sub, new_sub):
    return main_str.replace(old_sub, new_sub)

def to_capital_letters(main_str):
    return main_str.upper()

def main():
    while True:
        print("\nMenu:")
        print("1. Check if the String is a Substring of Another String")
        print("2. Count Occurrences of Character")
        print("3. Replace a Substring with Another Substring")
        print("4. Convert to Capital Letters")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            main_str = input("Enter the main string: ")
            sub_str = input("Enter the substring: ")
            if is_substring(main_str, sub_str):
                print(f"'{sub_str}' is a substring of '{main_str}'")
            else:
                print(f"'{sub_str}' is not a substring of '{main_str}'")
        
        elif choice == '2':
            main_str = input("Enter the string: ")
            char = input("Enter the character: ")
            count = count_occurrences(main_str, char)
            print(f"The character '{char}' occurs {count} times in '{main_str}'")
        
        elif choice == '3':
            main_str = input("Enter the main string: ")
            old_sub = input("Enter the substring to be replaced: ")
            new_sub = input("Enter the new substring: ")
            result = replace_substring(main_str, old_sub, new_sub)
            print(f"The new string is: {result}")
        
        elif choice == '4':
            main_str = input("Enter the string: ")
            result = to_capital_letters(main_str)
            print(f"The string in capital letters is: {result}")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()