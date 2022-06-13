import os

x = input("Enter your message :")
print(f"Your message is {x}")

path = input ("Provide a path :")

isdir = os.path.isdir(path) 
print(isdir)

if  isdir == False :
    os.mkdir(path)
    file = "message.txt"
    myfile = open(path +"/"+file, 'w')
    myfile.write(x)
    myfile.close()

else:
    file = "message.txt"
    myfile = open(path +"/"+file, 'w')
    myfile.write(x)
    myfile.close()
    
    



