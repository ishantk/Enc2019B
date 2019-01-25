"""

John and Mark have to construct a wall
They have to put bricks to construct a wall
Start from John and after that Mark

Construct Wall of 15 Bricks

John	-		1 	Count 1
Mark 	-		2		  3
John	-		2		  5
Mark 	-		4		  9
John	-		3		  12
Mark 	-		6 		  18 -> 3 bricks

"""

N = int(input("Enter How Many Bricks? "))
brickCount = 0

def checkCount(count):
    if count >= N:
        return True
    else:
        return False

for i in range(1, N+1):

    brickCount = brickCount + i

    if checkCount(brickCount):
        brickCount = brickCount - i
        print((N - brickCount), "Brick(s) Planted by John Lastly")
        break

    brickCount = brickCount + (2*i)

    if checkCount(brickCount):
        brickCount = brickCount - (2*i)
        print((N-brickCount), "Brick(s) Planted by Mark Lastly")
        break

















