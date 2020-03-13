import csv


def Graph_data(name):
    Fitness_data = []
    Gen_data = []

    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        i = 0

        for row in csv_reader:
            if i != 0:
                Gen_data.append(row[7])
                Fitness_data.append(row[8])
            i += 1

    Number_generations = len(set(Gen_data))
    Sum_data = [0] * Number_generations

    for i in range(len(Gen_data)):
        index = int(Gen_data[i]) - 1
        cost = float(Fitness_data[i])
        Sum_data[index] += cost

    Generations_sting = []

    for i in range(Number_generations):
        Generations_sting.append(str(i))

    return [Generations_sting, Sum_data]
