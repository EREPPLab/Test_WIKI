import matplotlib.pyplot as plt
import csv
import mysql.connector
from Database import Database

connection = mysql.connector.connect(host='HOST_IP',
                                     database='DATABASE_NAME',
                                     user='USERNAME',
                                     password='PASSWORD')
cursor = connection.cursor()


def Get_Number_trials():
    Query = "SELECT DISTINCT Trial FROM Data WHERE Robot_UID = 1"
    print(Query)
    cursor.execute(Query)
    data = cursor.fetchall()

    Number_of_trials = len(data)

    return Number_of_trials


def Get_trial_data(Trial_Number):
    Query = "SELECT Generation, Fitness From Data WHERE trial = " + str(Trial_Number) + " AND Robot_UID = 1"
    print(Query)
    cursor.execute(Query)
    Query_data = cursor.fetchall()
    return Query_data


def Parse_Gen_TotalFitness_Trial_data(data):
    Fitness_data = []
    Gen_data = []

    # Parse Data into two arrays []
    for row in data:
        Gen_data.append(row[0])
        Fitness_data.append(row[1])

    Number_generations = len(set(Gen_data))

    Sum_data = [0] * Number_generations

    # Sum of Fitness for each Generation
    for i in range(len(Gen_data)):
        index = int(Gen_data[i]) - 1
        cost = float(Fitness_data[i])
        Sum_data[index] += cost

    Generations_string = []

    for i in range(Number_generations):
        Generations_string.append(str(i))

    return [Generations_string, Sum_data]


def Parse_Gen_BestFitness_Trial_data(data):
    Fitness_data = []
    Gen_data = []

    # Parse Data into two arrays []
    for row in data:
        Gen_data.append(row[0])
        Fitness_data.append(row[1])

    Number_generations = len(set(Gen_data))

    Sum_data = []

    # Create the empty array required to store the data
    for i in range(Number_generations):
        Sum_data.append([])

    # Sort the fitness of each Generation into arrays
    for i in range(len(Gen_data)):
        index = int(Gen_data[i]) - 1
        # Add to plotting array
        Sum_data[index].append(Fitness_data[i])

    # Get the best fitness to store into the plotting array
    for i in range(len(Sum_data)):
        Sum_data[i] = min(Sum_data[i])

    # Create the Generation String for plotting
    Generations_string = []

    for i in range(Number_generations):
        Generations_string.append(str(i))

    print(Sum_data)

    return [Generations_string, Sum_data]


# Create the Database object to send and receive data
Database = Database()

fig, ax = plt.subplots()
ax.set_title("Genetic Algorithm Simulation")
ax.set_xlabel("Generation")
ax.set_ylabel("Sum of Generation Fitness")

yLimit = Database.Get_yLimit()
yLimit = yLimit[0] * 1.25

ax.set_ylim([0, yLimit])

data = []

for i in range(Get_Number_trials()):
    data.append(Parse_Gen_BestFitness_Trial_data(Get_trial_data(i)))

for i in range(Get_Number_trials()):
    ax.plot(data[i][0], data[i][1], label="Trial " + str(i) + "")

ax.legend()
plt.show()
