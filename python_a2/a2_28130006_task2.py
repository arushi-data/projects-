#This task was created by Arushi Tejpal student id: 28130006
#This task is to simulate the spread of the disease
#This task uses the person class function from task1 and imports random
#This task was completed on the 6/6/2020


#import math
import random
#import numpy


from a2_28130006_task1 import Person #import person class from task1

default_health=75 #average person health points



class Patient(Person): #pateint class function with parent class: person from task 1.

    def __init__(self, first_name, last_name, health):
        super().__init__(first_name, last_name) #super class/parent class: person first name and last name from task 1.
        self.health_point = health

    def get_health(self):
        return self.health_point #returns health point

    def set_health(self, new_health):
        self.health_point=round(new_health) #new health
        return self.health_point


    def is_contagious(self):
        """this is the range for health point in boolean form"""
        if 75 <= self.health_point <= 100: #not contagious
            return False
        elif self.health_point == 75: #not contagious
            return False
        elif 50 <= self.health_point <= 74: #not contagious
            return False
        elif 30 <= self.health_point <= 49: #is contagious
            return True
        elif 0 <= self.health_point <= 29: #is contagious
            return True
        else:
            print(f"not in range{self.health_point}")

    def infect(self, viral_load):
        """using viral load effect of infection using health points."""
        if self.health_point<=29:
            self.health_point=round(self.health_point-(0.1*viral_load))
        elif self.health_point < 50 and self.health_point >29 :
            self.health_point=round(self.health_point-(1.0*viral_load))
        elif self.health_point >=50:
            self.health_point=round(self.health_point-(2.0*viral_load))
        else:
            self.health_point=0


    def sleep(self):
        """when sleep 5 health point is added  along with range of health point between 100-0."""
        if self.health_point <= 100 and self.health_point>=0:
            self.health_point=self.health_point+5
            if self.health_point>100:
                self.health_point=100


def load_patients(initial_health):
    """read file from a2_sample_set.txt and seperates person and their friends"""
    with open("a2_sample_set.txt", 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            name_list = []
            for line in lines:
                person_list = line.strip().split(': ')
                fullname = person_list[0]
                first_name, last_name = fullname.strip().split()
                obj_count = Patient(first_name, last_name,initial_health)
                friend_list = person_list[1]
                friend_list = friend_list.strip().split(", ")
                for l in friend_list:
                    obj_count.add_friend(l)
                name_list.append(obj_count)
            return name_list


def is_visiting(prob):
    """using random probability"""
    if random.random() <= prob:
        visiting=True
        return visiting

    else:
        visiting=False
        return visiting


def viral_load(person): #if contagious viral load will be implemented
    """this function calculates the viral load of person who is contagious. """
    if person.is_contagious() == True:
        viral_load= round(5 + ((person.health_point-25)**2/62))
        return viral_load
    else:
        viral_load=0
        return viral_load

def effect_zero_person(a_list,zero_health): #patient zero is first person to get infected.
    """This function sets the zero health of first person in list which is Gill Bates to create simulation. """
    for person in a_list:
        if person == a_list[0]:
            person.set_health(zero_health)
    return a_list

def get_infected_count(full_list):
    """this function calculates the number of infected person in the simulation from list."""
    infected_people = 0
    for person in full_list:
        if person.is_contagious():
            infected_people += 1
    return infected_people

def send_sleep(full_list):
    """this function adds 5 health points when person sleeps in simulation."""
    for person in full_list:
        person.sleep()
    #print("sending to sleep")

def spread_viral(full_list,prob):
    """This function spreads the viral load in the list using is_contagious and viral load function """
    for person in full_list:
        for friend in person.get_friends():
            for obj in full_list:
                if obj.get_name() == friend and obj.is_contagious():
                    if is_visiting(prob):
                        #lv=viral_load(obj)
                        person.infect(viral_load(obj))
                elif person.is_contagious() and obj.get_name()==friend:
                    if is_visiting(prob):
                        #lv=viral_load(person)
                        obj.infect(viral_load(person))
    return full_list


def run_simulation(days, meeting_probability, patient_zero_health):
    """This function  runs the simulation by using the meeting probability, days and patient zero health points """
    infected_list=[]
    full_list=load_patients(initial_health=default_health)
    full_list=effect_zero_person(full_list,patient_zero_health)
    for i in range(1, days + 1):
        full_list=spread_viral(full_list,meeting_probability)
        send_sleep(full_list)
        infected_list.append(get_infected_count(full_list))
    return infected_list




if __name__ == '__main__':


    #test_result = run_simulation()
   test_result=run_simulation(40,0.25,49)



