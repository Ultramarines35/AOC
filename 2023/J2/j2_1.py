j2 = open("j2.txt", "r").read().splitlines()
result = 0
red = 12
green = 13
blue = 14

for i in range(len(j2)):
    line = j2[i].split(": ")
    gameset = line[1].split("; ")
    etat = True
    for set in gameset:
        number_ball_set = set.split(", ")
        for number_ball in number_ball_set:
            ball = number_ball.split(" ")
            numb = int(ball[0])
            if ball[1]=="green" and numb > green and etat:
                etat = False
            elif ball[1]=="blue" and numb > blue and etat:
                etat = False
            elif ball[1]=="red" and numb > red and etat:
                etat = False
    if etat:
        result += i+1

print(result)    