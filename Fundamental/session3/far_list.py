list = ["am nhac", "kem", "dien tu"]
new_item = input("ten ban muon them ? :")
list.append(new_item)
print(*list,sep=", ")