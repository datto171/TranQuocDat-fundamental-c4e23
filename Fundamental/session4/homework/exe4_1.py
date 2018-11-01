print("Answer the following algebra question:" )
question1 = {
    "question"  : "If x = 8, then what is the value of 4(x+3) ? ",
    "answer1"   : "35",
    "answer2"   : "36",
    "answer3"   : "40",
    "answer4"   : "44",
    "positions" : 4
}
for k,v in question1.items():
    if k == 'positions':
        break
    print(k, v, sep=": ")
x = int(input("Your choice: "))
if x == question1['positions']:
    print("Bingo")
else:
    print(":(")
