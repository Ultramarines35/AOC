j2 = open("j2.txt", "r").read().splitlines()
result = 0

for i in range(len(j2)):
    line = j2[i].split(": ")
    gameset = line[1].split("; ")
    red = 0
    green = 0
    blue = 0
    for set in gameset:
        number_ball_set = set.split(", ")
        print(gameset)
        for number_ball in number_ball_set:
            ball = number_ball.split(" ")
            numb = int(ball[0])
            if ball[1]=="green":
                green = max(numb,green)
            elif ball[1]=="blue":
                blue = max(numb,blue)
            elif ball[1]=="red":
                red = max(numb,red)
    result += blue*red*green

print(result)    