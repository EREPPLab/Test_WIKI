from Constants import Constants
from Evaluation.Evaluation import Evaluation
import serial
import time


class SumOfDiffEvaluation(Evaluation):
    def __init__(self, target_height):
        self.target_height = target_height
        # make a serial connection ONCE
        # Establish the connection with the ardunio
        self.ser = serial.Serial(Constants.arduino_comm_port, baudrate=9600, timeout=1)
        # Allow the arduino to initialize
        time.sleep(3)

    def get_fitness(self, chromosome):
        fitness = 0
        # Encode chromosome into byte data to send to the ardunio
        string = ','.join(map(str, chromosome)) + ',*'
        self.ser.write(str.encode(string))
        print("\t\t" + str(string))

        for i in range(len(chromosome)):

            # Read the ardunio gene score.
            gene = self.ser.readline().decode().split('\r\n')

            # How many genes to read in the string.
            if i < len(chromosome):
                # In case the sensor misses a reading
                if gene[0] != '':
                    gene = int(gene[0])
                else:
                    gene = 0

            # If the gene hits 6cm then add one to the score
            delta = min(16, abs(self.target_height - gene))
            fitness += delta
            print("\t\tCurrent = " + str(gene) + ". Delta = " + str(delta) + ". Fitness = " + str(fitness))
        print("\t\tEnd\n")
        time.sleep(10)

        return fitness
