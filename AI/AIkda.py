#IMPORT
import math
import seaborn as sns
import pygame

#pygame initialize


#CLASSES
class Gaming():

    kill = None
    death = None
    assist = None
    length = None
    player = None

    def __init__(self, K,D,A,L, P):
        self.kill = K
        self.death = D
        self.assist = A
        self.length = L
        self.player = P

    def toKDA(self):
        return (self.kill + self.assist)/max(1, self.death)

#DATASET
dataset = []
dataset.append(Gaming(17, 3, 11, 24, "kr"))
dataset.append(Gaming(10, 7, 14, 35, "kr"))
dataset.append(Gaming(6, 1, 8, 27, "kr"))
dataset.append(Gaming(9, 0, 6, 29, "kr"))
dataset.append(Gaming(13, 10, 11, 36, "kr"))
dataset.append(Gaming(5, 5, 9, 31, "kr"))
dataset.append(Gaming(3, 3, 4, 24, "kr"))
dataset.append(Gaming(4, 2, 7, 22, "kr"))
dataset.append(Gaming(4, 11, 4, 32, "a"))
dataset.append(Gaming(6, 5, 0, 27, "a"))
dataset.append(Gaming(8, 4, 7, 21, "a"))
dataset.append(Gaming(3, 5, 23, 34, "a"))
dataset.append(Gaming(5, 14, 6, 34, "a"))
dataset.append(Gaming(8, 6, 10,28, "a"))
dataset.append(Gaming(11, 12, 4,38, "a"))
dataset.append(Gaming(8, 5, 22, 28, "a"))
dataset.append(Gaming(7, 14, 7, 41, "a"))
dataset.append(Gaming(1, 10, 4, 23, "a"))
dataset.append(Gaming(4, 3, 21, 25, "kr"))
dataset.append(Gaming(10, 12, 12, 33, "a"))
dataset.append(Gaming(9, 8, 22, 49, "a"))
dataset.append(Gaming(8, 5, 13, 27, "a"))
dataset.append(Gaming(11, 7, 10, 36, "kr"))
dataset.append(Gaming(18,8,9,31, "a"))
dataset.append(Gaming(8,4,10,33, "a"))
dataset.append(Gaming(2,6,8,19, "a"))
dataset.append(Gaming(8,10,28, 37, "a"))
dataset.append(Gaming(2,1, 12, 24, "kr"))
dataset.append(15, 8, 12, 31)

print("\n")
k = input("type kills: ")
d = input("type deaths: ")
a = input("type assists: ")
m = input("type game length (min): ")

kda = (int(k)+int(a))/max(1, int(d))

datasetMask = []
#knn
for point in dataset:
    datasetMask.append(math.sqrt((kda*15-point.toKDA()*15)**2 + (int(m)*5-int(point.length)*5)**2)) #func to calculate the distance beetween the 2 data

dtMmin = min(datasetMask)
i = datasetMask.index(dtMmin) #find the closest one
print(i)

assumption = Gaming(int(k), int(d), int(a), int(m), dataset[i].player)
dataset.append(assumption)
print("la partita è stata giocata da: "+ assumption.player)	

pygame.init()
clock = pygame.time.Clock()
negro = pygame.display.set_mode((500,500))

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
blue = (0,0, 255)
green = (0, 255, 0)
lup = True
negro.fill(white)
pygame.draw.line(negro, black, (0, 250), (500, 250))
1
pygame.draw.line(negro, black, (250, 0), (250, 500))
while lup:
   
   
   for cont in dataset:
       color = red
       if cont.player == "kr":
           color = blue
       if cont == dataset[len(dataset)-1]:
           color = green
       pygame.draw.circle(negro, color, (250 + cont.length*5, 250 - cont.toKDA()*15 ), 3, 3)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         lup = False
   pygame.display.flip()