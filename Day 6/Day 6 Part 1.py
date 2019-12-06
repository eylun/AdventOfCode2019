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
    def helper(orbit,count):
        if len(orbit.get_orbits()) == 0:
            return count
        else:
            temp_count = count
            for child_orbit in orbit.get_orbits():
                count += helper(child_orbit,temp_count + 1)
            return count
    #Initialising all the orbits
    orbit_instructions = readfile()
    orbits = {}
    for instruction in orbit_instructions:
        orbit_one_name, orbit_two_name = instruction.split(")")
        orbit_one,orbit_two = None, None
        if orbit_one_name not in orbits.keys():
            orbit_one = Orbit(orbit_one_name)
            orbits[orbit_one_name] = orbit_one
        else:
            orbit_one = orbits[orbit_one_name]
        if orbit_two_name not in orbits.keys():
            orbit_two = Orbit(orbit_two_name)
            orbits[orbit_two_name] = orbit_two
        else:
            orbit_two = orbits[orbit_two_name]
        orbit_one.add_orbit(orbit_two)
    #Calculating direct and indirect orbits
    center = orbits["COM"]
    return helper(center,0)

def readfile():
    orbit_list = []
    with open ("input","r") as file:
         orbit_list = file.read().split("\n")
    file.close()
    return orbit_list

print(main())
