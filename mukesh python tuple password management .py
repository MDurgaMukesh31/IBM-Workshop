import urllib
a=tuple(input("enter your username: "))
b=tuple(input("enter your password: "))
c=tuple(input("confirm your password: "))
def open():
    return urllib.urlopen('https://www.youtube.com/')
if b==c:
    print('password is correct')
    print('password succesful \n press 1 to open youtube ')
    d=int(input(''))
    
    if d==1:
        open
else:
    print('password is incorrect')
