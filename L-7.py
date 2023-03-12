
n = int(input("qaxaqneri qanak - "))
city = set()

for i in range(n):
    c = True
    while c:
        anna = input("Anna asa qaxaqi anun - ")
        if anna in city:
            print("TRY ANOTHER")
            
        else:
            city.add(anna)
            print("OK")
            c = False
    c = True       
    while c:
        natasha = input("Natasha asa qaxaqi anun - ")

        if natasha in city:
            print("TRY ANOTHER")
            
        else:
            city.add(natasha)
            print("OK")
            c = False
print(city)

autopep8 --in-place --aggressive L-7.py


    