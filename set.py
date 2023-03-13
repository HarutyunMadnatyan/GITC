import random

b = set()
d = set()
for i in range(20):
    c = random.randint(1, 10)
    e = random.randint(5, 15)
    b.add(c)
    d. add(e)

print("b", "-", b)
print("d", "-", d)
print(f"miacum- {b|d}")
print(f"tarberutyun - {b&d}")
print(f"iraric hanel- {d-b}")

num = int(input("qani mard avelacnel?- "))
a = set()
for i in range(num):
    name = input("Azganun- ")
    a.add(name)
print(a)
