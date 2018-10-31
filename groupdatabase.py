import grp

print("ID: 4: " + str(grp.getgrgid(4)) + '\n') #Password detail using Group ID

print("cdrom group: " + str(grp.getgrnam('cdrom')) + '\n') #Password detail using Group name

for entry in grp.getgrall():
   print("Group Name: " + entry[0] + "\t\tMembers: " + str(entry.gr_mem))
