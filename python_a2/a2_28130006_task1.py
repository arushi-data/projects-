# Task 1 code  for FIT9136 Assignment 2.
#Task was created by Arushi Tejpal student number: 28130006
#This task is representing social connections in the program
#This task is made to enable the Class person function.
#Create first name last name and full name of people in the list  generated from the a2_sample_set.txt
#The load people function opens and reads the a2_dample_set.txt file.
#This task uses the load people function to create a full list of people and seperating their friends
#Using the class function it generates the first name and last name of each friend and the person from list.
#This task was finished and finalised on the 5/6/2020

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []


    def add_friend(self, friend_person):
        self.friends.append(friend_person)

    def get_name(self):
        fullname = f'{self.first_name} {self.last_name}'
        return fullname

    def get_friends(self):
        return self.friends

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


def load_people():
    """this function is made to open and read file and to seperate the person and their friends"""
    with open("a2_sample_set.txt", 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        name_list = []
        for line in lines:
            person_list = line.strip().split(': ') #used to seperate friend and person from semicolon
            fullname=person_list[0] # 0 is the person
            first_name, last_name=fullname.strip().split()
            obj_count=Person(first_name,last_name)
            friend_list =person_list[1] # 1 is the friend list
            friend_list = friend_list.strip().split(", ")
            for l in friend_list:
                obj_count.add_friend(l)
            name_list.append(obj_count)
        return name_list



if __name__ == '__main__':

    full_list=load_people()
    #print(full_list)
#print(len(full_list))
#for person in full_list:
   #print(person.get_name())
    #print(person.get_friends())