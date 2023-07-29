#!/usr/bin/python3
def validate_password(password):
    
    if len(password) < 8:
        return False
    
    for c in password:
        if c.isupper():
            return True
        elif c.islower():
            return True
        elif c.isdigit():
            return True
        elif char.isspace():
            return False
        else:
            return False
