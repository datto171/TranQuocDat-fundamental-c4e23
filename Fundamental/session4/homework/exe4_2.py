print("Answer the following algebra question:" )
question1 = {
    "question"  : "If x = 8, then what is the value of 4(x+3) ? ",
    "answer1"   : "35",
    "answer2"   : "36",
    "answer3"   : "40",
    "answer4"   : "44",
    "positions" : 4
}
question2 = {
    "question"  : "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? ",
    "answer1"   : "About 55",
    "answer2"   : "About 65",
    "answer3"   : "About 75",
    "answer4"   : "About 85",
    "positions" : 2
}
list_question = [question1, question2]
point = 0

for i in range(len(list_question)):
    for k,v in (list_question[i].items()):
        if k == 'positions':
            break
        print(k, v, sep=": ")
    x = int(input("Your choice: "))
    if x == list_question[i]['positions']:
        point += 1
        print("Bingo")
    else:
        print(":(")

print("You correctly answer",point ,"out of", len(list_question), "question")

