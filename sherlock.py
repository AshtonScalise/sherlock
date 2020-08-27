import os
strToFind = "ftw"
yourpath = "E:/"
foundList = []


for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        # print(os.path.join(root, name))
        filename = (os.path.join(root, name))
        try:
            if filename.endswith(".txt"):
                f = open(filename, "r")
                whattoReturn = "None"
                if strToFind in f.read():
                    print("found in ---> " + filename)
                    foundList.append(filename)
                    whattoReturn = strToFind

        except:
            pass
            # print("couldn't open " + filename)

print(foundList)

    # for name in dirs:
    #     print(os.path.join(root, name))
