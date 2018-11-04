# person = ["Dat", "Ha Noi", "FTU", 23, 3, 257, False]

person = {
    "name"  : "Dat",
    "city"  : "Hanoi",
    "age"   :  23,
}

# person["friend_count"] = 257
# print(person)

del person["name"]
print(person)

# print("nhap 'stop' de dung chuong trinh")
# while True:
#     key = input("Nhap :")
#     if key in person:
#         print(key, person[key], sep=": ")
#     elif key == "stop":
#         break
#     else:
#         x = input("Ban co muon dong gop vao tu dien khong (Y/N)").upper()
#         if x == "Y":
#             k = input("Nhap nghia cua tu: ")
#             person[key] = k
#             for i in person:
#                 print(i)
#         else:
#             break
    