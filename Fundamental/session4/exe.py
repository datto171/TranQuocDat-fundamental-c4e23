p1 = {
    "stt"   : "1",
    "name"  : "Huy",
    "Hours" : 30,
    "VND"   : 50,
}
p2 = {
    "stt"   : "2",
    "name"  : "Quan",
    "Hours" : 20,
    "VND"   : 40,
}
p3 = {
    "stt"   : "3",
    "name"  : "Duc",
    "Hours" : 15,
    "VND"   : 35,
}
#Cau 1
list = [p1, p2, p3]
# print(list)

#Cau 2
# for i in list:
#     print(i['Hours'])

#Cau 3 + #Cau 4
x = 0
s = 0
for i in list:
    x = i['Hours'] * i['VND']
    print(i['name'], x, sep=": ")
    s = s + x
    
print("Tong luong: ", s)