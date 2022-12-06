username = input('enter the name')
password = input('enter the password')
passwordlength = len(password)
hiddenpassword = '*'*passwordlength
# hidden the password is send the value of hidden password
print(f'your {username},and your {hiddenpassword} length of {passwordlength}')