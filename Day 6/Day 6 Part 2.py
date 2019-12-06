class Orbit:
    def __init__(self, name):
        self.name = name
        self.orbits = [] #A list of objects, these objects ORBIT AROUND self

    def get_name(self):
        return self.name
    def get_orbits(self):
        return self.orbits

    def add_orbit(self, new_orbit):
        self.orbits.append(new_orbit)

def main():
    #Helper function for recursion
    def helper(orbit, target):
        if orbit == target:
            return [orbit.get_name(),]
        elif len(orbit.get_orbits()) == 0:
            return []
        else:
            for child_orbit in orbit.get_orbits():
                child_path = helper(child_orbit, target)
                if child_path != []:
                    return [orbit.get_name(),] + child_path
            return []
    #Initialising all the orbits
    orbit_instructions = readfile()
    orbits = {}
    you_orbit = None
    santa_orbit = None
    for instruction in orbit_instructions:
        orbit_one_name, orbit_two_name = instruction.split(")")
        orbit_one,orbit_two = None, None
        if orbit_one_name not in orbits.keys():
            orbit_one = Orbit(orbit_one_name)
            orbits[orbit_one_name] = orbit_one
        else:
            orbit_one = orbits[orbit_one_name]
        #Check if orbit two is YOU or SAN first
        if orbit_two_name == "YOU" or orbit_two_name == "SAN":
            if orbit_two_name == "YOU":
                you_orbit = orbit_one
            else:
                santa_orbit = orbit_one
        else:
            if orbit_two_name not in orbits.keys():
                orbit_two = Orbit(orbit_two_name)
                orbits[orbit_two_name] = orbit_two
            else:
                orbit_two = orbits[orbit_two_name]
            orbit_one.add_orbit(orbit_two)
    #Calculating direct and indirect orbits
    center = orbits["COM"]
    your_path = helper(center, you_orbit)
    santa_path = helper(center, santa_orbit)
    index = 0
    print(your_path,santa_path)
    while your_path[index] == santa_path[index]:
        index += 1
    return len(your_path) + len(santa_path) - 2 * index

def readfile():
    orbit_list = []
    with open ("input 2","r") as file:
         orbit_list = file.read().split("\n")
    file.close()
    return orbit_list

print(main())
