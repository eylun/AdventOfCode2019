import math

class Reaction():
    def __init__(self, inputs, output_amount, output_chemical):
        self.inputs = inputs
        self.output_chemical = output_chemical
        self.output_amount = output_amount

    def get_inputs(self):
        return self.inputs

    def get_output_amount(self):
        return self.output_amount

    def get_output_chemical(self):
        return self.output_chemical

leftover_dict = {}

def main():
    reaction_dict = {}

    def helper_recursion(reaction, amount):
        amount = math.ceil(amount / reaction.get_output_amount())
        if "ORE" in reaction.get_inputs().keys():
            return amount * reaction.get_inputs()["ORE"]
        else:
            count = 0
            for required_input in reaction.get_inputs().keys():
                extras = 0
                if required_input in leftover_dict.keys():
                    extras = leftover_dict[required_input]
                    leftover_dict[required_input] = 0
                required_amount = amount * reaction.get_inputs()[required_input] - extras
                ores_used = helper_recursion(reaction_dict[required_input], required_amount)
                count += ores_used
                accumulated = reaction_dict[required_input].get_output_amount() - required_amount % reaction_dict[required_input].get_output_amount()
                if accumulated == reaction_dict[required_input].get_output_amount():
                    accumulated = 0
                if accumulated != 0:
                    if required_input not in leftover_dict.keys():
                        leftover_dict[required_input] = accumulated
                    else:
                        leftover_dict[required_input] += accumulated
            return count

    reactions = readfile()
    for reaction in reactions:
        reaction_dict[reaction.get_output_chemical()] = reaction
    fuel_start = 0
    ore_count = 0
    base_reaction = reaction_dict["FUEL"]
    fuel_count = 0
    tril = 1000000000000
    min_fuel, max_fuel = 1, tril // helper_recursion(base_reaction, 1) * 2
    while min_fuel < max_fuel:
        midpoint = (min_fuel + max_fuel) // 2
        ore_needed = helper_recursion(base_reaction, midpoint)
        leftover_dict.clear()
        if ore_needed > tril:
            max_fuel = midpoint - 1
        elif ore_needed <= tril:
            min_fuel = midpoint
    print(midpoint - 1)






def readfile():
    reactions = []
    with open("input","r") as f:
        instructions = f.read().split("\n")
        f.close()
    for instruction in instructions:
        reaction_inputs = {}
        inputs, output = instruction.split(" => ")
        inputs = list(map(lambda x: x.split(" "), inputs.split(", ")))
        output = output.split(" ")
        output = [int(output[0]), output[1]]
        for chemical in inputs:
            reaction_inputs[chemical[1]] = int(chemical[0])
        reactions.append(Reaction(reaction_inputs,output[0], output[1]))
        #print(reaction_inputs, reaction_outputs)
    return reactions

main()