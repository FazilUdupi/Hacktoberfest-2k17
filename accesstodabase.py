import pwd

print("Root: " + str(pwd.getpwnam('root')) + '\n') #Password detail for root

for entry in pwd.getpwall():
   print("Name: " + entry[0] + "\t\tShell: " + entry.pw_shell)
