f = open("girwhisky.csv", "r")
contents = f.readlines()
f.close()

whiskylist = []
for i in range(len(contents)):
    whiskylist.append([j.strip() for j in contents[i].split(",")])
    
for i in whiskylist:
    print(len(i))