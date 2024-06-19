n = 0
while n != 5:
    n = int(input("Enter your choice\n1: Check if the string is a substring of another string\n2: Count the occurrence of a character\n3: Replace a substring with another substring\n4: Convert to capital letters\n5: Exit\n"))
    
    if n == 1:
        # Check if the String is a Substring of Another String
        main_string = input("Enter the main string: ")
        sub_string = input("Enter the substring to check: ")
        if sub_string in main_string:
            print(f"'{sub_string}' is a substring of '{main_string}'.")
        else:
            print(f"'{sub_string}' is not a substring of '{main_string}'.")
    
    elif n == 2:
        # Count Occurrences of Character
        main_string = input("Enter the main string: ")
        char = input("Enter the character to count: ")
        count = main_string.count(char)
        print(f"Number of occurrences of '{char}' in '{main_string}': {count}")
    
    elif n == 3:
        # Replace a substring with another substring
        main_string = input("Enter the main string: ")
        old_substring = input("Enter the substring to replace: ")
        new_substring = input("Enter the new substring: ")
        modified_string = main_string.replace(old_substring, new_substring)
        print(f"Modified string: '{modified_string}'")
    
    elif n == 4:
        # Convert to Capital Letters
        main_string = input("Enter the string to convert to capital letters: ")
        capital_string = main_string.upper()
        print(f"String in capital letters: '{capital_string}'")
    
    elif n == 5:
        print("Exiting the program...")
    
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

print("Program ended.")
