import os
import pickle
filename = "./students.data" #Global variable of file name, the file path where you save data

class Database:

    #Initialize the DB, 2 main functions --> Read and write to DB/File
    @staticmethod
    def initialize():
        if not (os.path.exists(filename)):
            handler = open(filename, 'wb')
            pickle.dump([], handler)
            handler.close()

    @staticmethod
    def write(students):
        with open(filename, 'wb') as handler:
            pickle.dump(students, handler)
        handler.close()

    @staticmethod
    def read():
        with open(filename, 'rb') as handler:
            customers = pickle.load(handler)
        return customers
