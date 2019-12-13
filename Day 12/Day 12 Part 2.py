def main():
    moons = readfile()
    count_tracker = [0, 0, 0]
    for axis in range(3):
        axises = [moons[x][axis] for x in range(4)]
        base_axises = axises[:]
        axis_velocity = [0, 0, 0, 0]
        done = False
        timestep = 0
        while not done:
            if timestep != 0 and axises == base_axises:
                done = True
            for i in range(len(axises)):
                other_axises = axises[:]
                other_axises.pop(i)
                for j in range(len(other_axises)):
                    if axises[i] < other_axises[j]:
                        axis_velocity[i] += 1
                    elif axises[i] > other_axises[j]:
                        axis_velocity[i] -= 1
            axises = list(map(lambda x, y: x + y, axises, axis_velocity))
            timestep += 1
        count_tracker[axis] = timestep
    return int(lcm(count_tracker))

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i / gcd(lcm, i)
    return lcm

def readfile():
    base_positions = []
    with open("input","r") as f:
        raw = f.read().split("\n")
    for moon in raw:
        base_positions.append(list(map(lambda x : int(x[2::]), moon[1:-1].split(", "))))
    return base_positions

print(main())