import operator

def main():
    moons = readfile()
    velocity = [[0 for i in range(3)] for j in range(4)]
    timestep = 1
    kinetic, potential, total = 0, 0, 0
    while timestep <= 1000:
        for focus_moon in range(len(moons)):
            moons_copy = moons[:]
            moons_copy.pop(focus_moon)
            for other_moon in range(len(moons_copy)):
                for axis in range(len(moons[focus_moon])):
                    if moons[focus_moon][axis] < moons_copy[other_moon][axis]:
                        velocity[focus_moon][axis] += 1
                    elif moons[focus_moon][axis] > moons_copy[other_moon][axis]:
                        velocity[focus_moon][axis] -= 1
        for i in range(len(moons)):
            moons[i] = list(map(lambda x, y : x + y, moons[i], velocity[i]))
        timestep += 1
    print(timestep)
    print(moons)
    print(velocity)
    for j in range(len(moons)):
        kinetic = sum(list(map(lambda x: abs(x), velocity[j])))
        potential = sum(list(map(lambda x: abs(x), moons[j])))
        total += kinetic * potential
    return total


def readfile():
    base_positions = []
    with open("input","r") as f:
        raw = f.read().split("\n")
    for moon in raw:
        base_positions.append(list(map(lambda x : int(x[2::]), moon[1:-1].split(", "))))
    return base_positions

print(main())