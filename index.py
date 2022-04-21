File_object = open(r"answers", "ro")

att = ['administration', 'apostleship', 'discernment', 'encouragement', 'evangelism', 'faith', 'giving', 'helps', 'hospitality', 'intercession', 'knowledge', 'leadership', 'mercy', 'prophecy', 'shepherding', 'teaching', 'wisdom']
answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

answers = File_object.read().splitlines()

for n in range(119):
    answerInd = n % 17
    answer[answerInd] += int(answers[n])

for i in range(17):
    print(att[i], answer[i])
