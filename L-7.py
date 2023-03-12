
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
    c=True
    while c:
        natasha = input("Natasha asa qaxaqi anun - ")

        if natasha in city:
            print("TRY ANOTHER")

        else:
            city.add(natasha)
            print("OK")
            c = False
print(city)


# Books for summer

m = int(input("Qani girq ka gradaranum? - "))
n = int(input("Qani girq e handznararvac? - "))

gradaran = set()
for i in range(m):
    gradaran_list = input("Mutqagrel gradarani grqeri anunner@ - ")
    gradaran.add(gradaran_list)
print(gradaran)
for i in range(n):
    amaran_grqer = input("Mutqagrel amran@ handznararvac greri anunner@ - ")
    if amaran_grqer in gradaran:
        print("YES",)
    else:
        print("NO")
