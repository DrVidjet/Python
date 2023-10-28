s = input("Enter the string: ")
s = s.lower()

if "ф" in s:
    a = s.count("ф")
    if a == 1:
        print(s.find("ф"))
    else:
            print(s.find("ф"))
            print(s.find("ф", -1))
