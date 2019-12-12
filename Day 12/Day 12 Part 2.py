def main():
    moons = readfile()
    for i in range(3):

    # velocity = [[0 for i in range(3)] for j in range(4)]
    # individual_moon_base_pos = moons[:]
    # individual_moon_cycle = [1, 1, 1, 1]
    # timestep = 1
    # #moon_pos_set = set()
    # done = False
    # while not done:
    #     print(individual_moon_cycle, timestep)
    #     #print(timestep, moons[1], velocity[1])
    #     #moon_set = tuple(tuple(moons[i]) for i in range(len(moons)))
    #     #if moon_set in moon_pos_set:
    #     #    done = True
    #     #else:
    #         #moon_pos_set.add(moon_set)
    #     for focus_moon in range(len(moons)):
    #         moons_copy = moons[:]
    #         moons_copy.pop(focus_moon)
    #         for other_moon in range(len(moons_copy)):
    #             for axis in range(len(moons[focus_moon])):
    #                 if moons[focus_moon][axis] < moons_copy[other_moon][axis]:
    #                     velocity[focus_moon][axis] += 1
    #                 if moons[focus_moon][axis] > moons_copy[other_moon][axis]:
    #                     velocity[focus_moon][axis] -= 1
    #         if moons[focus_moon] == individual_moon_base_pos[focus_moon]:
    #             if individual_moon_cycle[focus_moon] == 1:
    #                 individual_moon_cycle[focus_moon] = timestep
    #             if 1 not in individual_moon_cycle:
    #                 done = True
    #     #print(moons, "---", velocity)
    #     for i in range(len(moons)):
    #         moons[i] = list(map(lambda x, y : x + y, moons[i], velocity[i]))
        if not done:
            timestep += 1
    print(individual_moon_cycle, int(lcm(individual_moon_cycle)))
    return timestep


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