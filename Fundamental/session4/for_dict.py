p1 = {
    "name"  : "Dat",
    "city"  : "Hanoi",
    "age"   :  23,
}

p2 = {
    "name"  : "Quan",
    "city"  : "Hanoi",
    "age"   :  24,
}

# for k in person.keys(): #tuple ~ list
#     print(k, person[k], sep=": ")

# for v in person.values():
#     print(v)

# for k,v in person.items():
#     print(k, v)

p_list = [
    {
        "name"  : "Dat",
        "city"  : "Hanoi",
        "age"   :  23,
    },
    {
        "name"  : "Quan",
        "city"  : "Hanoi",
        "age"   :  24,
    }
]
for p in p_list:
    print(p['name'])
    print("----------")