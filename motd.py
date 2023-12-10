def check_password(password):
    if len(password) < 7:
        return False
    
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    
    special_characters = "!@#$%^&*()-_+=[]{}|:;,.?"
    
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    if not (has_lowercase and has_uppercase and has_digit and has_special):
        return False
    
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False
    
    return True
