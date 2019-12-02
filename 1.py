# https://adventofcode.com/2019/day/1

#
# Part one
#
PATH = 'inputs/1.txt'

def compute_fuel_required(module_mass):
    # integer division
    return (module_mass // 3) - 2

def compute_spacecraft_requirements(path, mass_computation_function):
    with open(path, 'r') as modules_masses:
        masses = list(map(int, modules_masses))
        return sum(map(mass_computation_function, masses))

def part_one():
    print(compute_spacecraft_requirements(PATH, compute_fuel_required))

#
# Part two
#

# Note: this function would be shorter if written recursively
def compute_total_fuel_required(module_mass):
    fuel = 0
    fuel_required = compute_fuel_required(module_mass)
    while (fuel_required > 0):
        fuel += fuel_required
        fuel_required = compute_fuel_required(fuel_required)
    return fuel

def part_two():
    print(compute_spacecraft_requirements(PATH, compute_total_fuel_required))

# Another way to solve the part 2: use of generators
# Not necessary, makes the code harder to understand but it was interesting to do
def fuel_required_generator(initial_mass):
    fuel_required = compute_fuel_required(initial_mass)
    while fuel_required > 0:
        yield fuel_required
        fuel_required = compute_fuel_required(fuel_required)

def compute_spacecraft_requirements_generator(path):
    with open(path, 'r') as modules_masses:
        masses = map(fuel_required_generator, map(int, modules_masses))
        return sum(map(sum, masses))

def part_two_generator():
    print(compute_spacecraft_requirements_generator(PATH))


if __name__ == '__main__':
    part_one()
    part_two()
    part_two_generator()

