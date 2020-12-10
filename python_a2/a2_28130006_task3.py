
#This task was created by Arushi Tejpal student number: 28130006.
#This task was created to run the simulation and create 3 graphs from senario A B and C
#This task enables user to input meeting probability, days and patient zero healt points.
#This task uses matplotlib.pyplot and class functions from task 2 to create simulatied graphs.
#This task was completed on the 6/6/2020.

import matplotlib.pyplot as plt
from a2_28130006_task2 import *

"""import statement to make use of functions/classes from earlier task(s) along with import of matplotlib"""

#probability value range between 1-0.0
def get_prob_value():
    """check input for Meeting Probability a float and in a specific Range"""
    maxvalue=1
    while True:
        try:
            value=float(input("Enter the meeting probability to use for the simulation(0.0 to 1 ):"))
        except ValueError:
            print(f"Please Try Again with a valid Probability float value between 0 and {maxvalue}")
            continue
        else:
            if value < 0 or value > maxvalue:
                print(f"Please Try Again with a valid Probability float value between 0 and {maxvalue}")
                continue
            else:
                return value

#range for days: cant be negaitve and less than 1
def get_days_value():
    """check input is a positive integer and in a specific Range"""
    while True:
        try:
            value=int(input("Enter number of Days to Run the Simulation:"))
        except ValueError:
            print(f"Please Try Again with Valid number of Days Integer above 0 ")
            continue
        else:
            if value < 1 :
                print(f"Please Try Again with Valid number of Days Integer above 0 ")
                continue
            else:
                return round(value)

def get_zero_value(): #input patient zero function with range of 0-49 ; for senario A B C
    """check input is a positive integer and in a specific Range"""
    maxvalue=100
    while True:
        try:
            value=int(input("Enter the health of Patient Zero in the simulation (0-100) :"))
        except ValueError:
            print(f"Please Try Again with a valid health of Patient Zero value between 0 and {maxvalue}")
            continue
        else:
            if value < 0 or value > maxvalue:
                print(f"Please Try Again with a valid health of Patient Zero value between 0 and {maxvalue}")
                continue
            else:
                return round(value)

#this function uses the import matplotlib to help make visual curve of simulation
#user types in the number of days,meeting probability and patient zero health point for curve to be simulated

def visual_curve(days, meeting_probability, patient_zero_health):
    """This function uses days meeting probibily and patient zero health imported from user to plot graph."""
    infected_list=run_simulation(days,meeting_probability,patient_zero_health)
    plt.plot(infected_list)
    plt.ylabel("Count")
    plt.xlabel("Days")
    plt.title('Assignment 2 Simulation: A, B or C ')
    plt.show()
    #plt.savefig('myfigure.png')


#call functions
def main():
    """This is the main function which takes user input to get days, meeting probability
    and patient zero health to create simulation graph."""
    days=get_days_value()
    meeting_probability=get_prob_value()
    patient_zero_health=get_zero_value()
    visual_curve(days,meeting_probability,patient_zero_health)




if __name__ == '__main__':
   main()
   #test_result=run_simulation(40,0.25,49)

