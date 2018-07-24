import os

clear = lambda: os.system('cls')

names = []
namesPoints = []

game_points = int(input("KUINKA MONEEN PELATAAN?: "))
numer = int(input("KUINKA MONTA PELAJAA: "))

point = 1

for x in range(numer):
        names.append(input(str(x+1)+". pelaajan nimi: "))
        namesPoints.append([game_points])
clear()
while True :
    if point != 0 :
        for x in range(numer):
            g = "PISTEET |"
            for y in range(numer):
                g += " "+(names[y] + ": " + str( namesPoints[y][len(namesPoints[y])-1] )+" |")
            print(g)
            points = int(namesPoints[x][len(namesPoints[x])-1])
            point = points - int(input("PELAAJAN " + names[x] + " VUORO | PISTEITÄ NYT: " + str(points) + " | TEHDYT PISTEET: "))
            if point == 0:
                namesPoints[x] = namesPoints[x] + [point]
                clear()
                break
            if point == 1 or point < 0:
                #print("Ei mahdolinen!")
                namesPoints[x] = namesPoints[x] + [points]
                clear()
                #print(names[x] + ": " + str(points))
            else:
                clear()
                namesPoints[x] = namesPoints[x] + [point]
                #print(names[x] + ": " + str(point))
    if point == 0:
        print("PELAAJA " + names[x] + " VOITTI!")
        for u in range(numer):
            print("-"+names[u] + " " + str( namesPoints[u]))
        com = input("UUSIPELI = (y) | LOPETA = (n) | KOMENTO: ")
        clear()
        if com == "y":
            point = 1
            for t in range(numer):
                namesPoints[t].clear()
                namesPoints[t].append(game_points)
        if com == "n" :
            break