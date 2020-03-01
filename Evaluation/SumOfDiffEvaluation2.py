from Constants import Constants
from Evaluation.Evaluation import Evaluation
import serial
import time


class SumOfDiffEvaluation2(Evaluation):
    def __init__(self, target_height):
        self.target_height = target_height
        # make a serial connection ONCE
        # Establish the connection with the ardunio
        self.ser = serial.Serial(Constants.arduino_comm_port, baudrate=9600, timeout=1)
        # Allow the arduino to initialize
        time.sleep(3)

    def is_valid(self, sentString, recvString):
        if sentString in recvString:
            return True
        else:
            return False
        # string must be in this format: [1,2,3]{4,5,6}
        # string is received directly from arduino

    def send_command_to_ardunio(self):
        pass

    def get_fitness(self, chromosome):
        fitness = 0
        # Encode chromosome into byte data to send to the ardunio
        string = '[' + ','.join(map(str, chromosome)) + ']'
        encoded = str.encode(string)
        self.ser.write(encoded)
        # print("Sending:")
        # print("\t" + str(string))

        what_i_just_read = self.ser.readline().decode()  # Send command

        valid = self.is_valid(string, what_i_just_read)
        # [1,2,3]{4,5,6}

        while not valid:
            what_i_just_read = self.ser.readline().decode()
            # Valid Format - [1252,1267,1248,1264,1242,1249,1267,1265,1263,1267]{4,3,90,3,15,3,3,76,15,15}
            valid = self.is_valid(string, what_i_just_read)  # Waiting for correct signal

        print("Receiving:")
        print("\t" + str(what_i_just_read))

        heights = what_i_just_read.replace(string, '')  # {4,3,90,3,15,3,3,76,15,15}
        heights = heights.replace('{', '')  # 4,3,90,3,15,3,3,76,15,15}
        heights = heights.replace('}', '')  # 4,3,90,3,15,3,3,76,15,15
        # split by comma and make an int array
        heights = heights.split(',')  # 4,3,90,3,15,3,3,76,15,15 an array of strings
        heights_int = []
        for height_str in heights:
            try:
                add_height = int(height_str)
            except ValueError:
                # If the ardunio sends a wrong signal then set height manually
                add_height = 16
                print('ERROR: We got {' + height_str + '} from' + str(what_i_just_read))

            heights_int.append(min(Constants.max_height, add_height))

        fitness = 0
        for height in heights_int:
            fitness += abs(self.target_height - height)
        fitness /= len(chromosome) # get avg fitness for all heights

        print("\tFitness = " + str(fitness))

        return fitness
