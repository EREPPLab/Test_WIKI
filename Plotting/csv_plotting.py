import matplotlib.pyplot as plt
import csv


Fitness_data = []
Gen_data = []


def Graph_data(name):
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

    for i in range(40):
        Generations_sting.append(str(i))

    return [Generations_sting, Sum_data]


data1 = Graph_data('Jeff_trial_1_40at40Gen.csv')
data2 = Graph_data('Linda_trial_1_40at40Gen.csv')

fig, ax = plt.subplots()
ax.plot(data1[0], data1[1], label="Jeff")
ax.plot(data2[0], data2[1], label="Linda")
ax.legend()

plt.show()
