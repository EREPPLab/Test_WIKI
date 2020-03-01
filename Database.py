import mysql.connector


class Database:
    def __init__(self):
        # Database connection info
        self.connection = mysql.connector.connect(host='HOST_IP',
                                                  database='DATABASE NAME',
                                                  user='USERNAME',
                                                  password='PASSWORD')
        # Connection object
        self.cursor = self.connection.cursor()

    def Get_Robot_UID(self, name):
        Check_Robot_UID = "SELECT Robot_UID FROM Robot WHERE Robot_name = '" + str(name) + "'"
        self.cursor.execute(Check_Robot_UID)
        data = self.cursor.fetchall()

        if not data:
            # Add the Robot name it doesnt exist
            Add_robot = "INSERT INTO Robot (Robot_name) VALUE ('" + str(name) + "')"
            self.cursor.execute(Add_robot)
            # Get the UID of the added Robot
            self.cursor.execute(Check_Robot_UID)
            Robot_UID = self.cursor.fetchall()
            Robot_UID = Robot_UID[0][0]
        else:
            Robot_UID = data[0][0]

        return Robot_UID

    def Get_Config_UID(self, selection_impl, crossover_impl, mutation_impl, evaluation_impl,
                       termination_impl, elitism, Population_size, Chromosome_length, Mutation_rate):

        # FIX Elitism BOOLEAN

        Check_Config_UID = "SELECT Config_UID FROM Config WHERE Selection  = '" + str(selection_impl) + "'" \
                                                                                                        " AND Crossover = '" + str(
            crossover_impl) + "' " \
                              " AND Mutation = '" + str(mutation_impl) + "'" \
                                                                         " AND Evaluation = '" + str(
            evaluation_impl) + "'" \
                               " AND Termination = '" + str(termination_impl) + "' " \
                                                                                " AND Elitism = '" + str(elitism) + "' " \
                                                                                                                    " AND Population_size = '" + str(
            Population_size) + "'" \
                               " AND Chromosome_length = '" + str(Chromosome_length) + "'" \
                                                                                       " AND Mutation_rate = '" + str(
            Mutation_rate) + "'"

        self.cursor.execute(Check_Config_UID)
        data = self.cursor.fetchall()
        # If it doesnt exist in the Table Config
        if not data:
            print("The config doesnt exist")
            # Add it to the Config table
            Add_Config_Query = "INSERT INTO Config " \
                               "( Selection, " \
                               "Crossover, " \
                               "Mutation," \
                               "Evaluation," \
                               "Termination," \
                               "Elitism, " \
                               "Population_size, " \
                               "Chromosome_length ," \
                               "Mutation_rate) " \
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            Add_Config_variables = (
                selection_impl,
                crossover_impl,
                mutation_impl,
                evaluation_impl,
                termination_impl,
                str(elitism),
                str(Population_size),
                str(Chromosome_length),
                str(Mutation_rate))

            self.cursor.execute(Add_Config_Query, Add_Config_variables)
            self.connection.commit()
            # Get the Config UID from the database
            self.cursor.execute(Check_Config_UID)
            Config_UID = self.cursor.fetchall()
            Config_UID = Config_UID[0][0]
        else:
            Config_UID = data[0][0]

        return Config_UID

    def End_connection(self):
        self.cursor.close()
        self.connection.close()

    def Add_run(self, Config_UID, generation, fitness, Current_trial, chromosome_string, Robot_UID):
        Query = "INSERT INTO Data (Config_UID, Generation, Fitness, Trial, Chromosome, Robot_UID )" \
                " VALUES (%s, %s, %s, %s, %s, %s)"

        Query_variables = (
            Config_UID,
            generation,
            fitness,
            Current_trial,
            chromosome_string,
            Robot_UID)

        self.cursor.execute(Query, Query_variables)
        self.connection.commit()

    def str_join(*args):
        return ''.join(map(str, args))

    def Add_generation(self, Generation, Config_UID):
        # Generation is a list will all the generations in it.

        Query = "INSERT INTO Data (Config_UID, Generation, Fitness, Trial, Chromosome, Robot_UID ) VALUES "

        data_list = [Query]

        for i in Generation:
            data_list.append("('" + str(Config_UID) + "'" + \
                             ",'" + str(i[0]) + "'" + \
                             ",'" + str(i[1]) + "'" + \
                             ",'" + str(i[2]) + "'" + \
                             ",'" + str(i[3]) + "'" + \
                             ",'" + str(i[4]) + "'),")

        Query = ''.join(data_list)

        Query = Query[:-1]

        self.cursor.execute(Query)
        self.connection.commit()

    def Get_yLimit(self):

        Query = "SELECT MIN(Fitness) AS LargestFitness FROM Data WHERE Generation = 1 "

        self.cursor.execute(Query)
        data = self.cursor.fetchall()

        return data[0]
