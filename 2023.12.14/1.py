def strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    elif password.isupper() or password.islower():
        return False
    elif len(set(password) & set(str(i) for i in range(10))) < 2:
        return False
    elif len(set(password) & set(' .,:;!@#$%^&*-_+=')) < 1:
        return False
    else:
        return True

# >>> strong_password('Password-1234')
# True

# >>> strong_password('pasword1')
# False