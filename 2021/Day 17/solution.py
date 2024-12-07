TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(data: str) -> tuple:
    target: str = data.strip('target area: ').split(', ')
    target_x = target[0].strip('x=').split('..')
    target_y = target[1].strip('y=').split('..')
    return int(target_x[0]), int(target_x[1]), int(target_y[0]), int(target_y[1])

def projectile(vx, vy, target, currX=0, currY=0):
    currX += vx
    currY += vy
    
    if target[0] <= currX <= target[1] and target[2] <= currY <= target[3]:
        return currX, currY
    if currX > target[1] or currY < target[2]:
        return False

    if vx == 0: vx = 0
    elif vx > 0: vx -= 1
    elif vx < 0: vx += 1
    vy -= 1

    return projectile(vx, vy, target, currX=currX, currY=currY)

def maxHeight(vx):
    if vx % 2 == 0:
        height = ((vx // 2) * vx) + vx // 2
    else:
        height = (((vx+1) // 2) * vx) + vx // 2
    return height

def partOne(target: tuple) -> int:
    height: list = []
    for vx in range(target[2], target[3]*-1):
        height.append(maxHeight(vx))
    return max(height)

def partTwo(target: tuple) -> int:
    number: list = []
    for x in range(0, target[1]+1):
        for y in range(target[2], target[2]*-1 + 1):
            if projectile(x, y, target) != False:
                number.append(projectile(x, y, target))
    return len(number)

def main() -> None:
    data = getData(DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()