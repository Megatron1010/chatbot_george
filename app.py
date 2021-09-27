###
#class chatter(self, text):
##    def replier(text):

###
import pandas as pd
import datetime

items = {"1": "toilet", "2": "bathtub", "3": "sink", "4":" geyser", "5":" bathroom taps", "6": "kitchen taps", }
jobs = {"1": "repair something", "2": "install something", "3": "replace something" }

jobList = []
workList = []
dict = {}
counter = 0

#Time module
time = datetime.datetime.now()

# App logic

while counter == 0:
    print("Good day, If you are looking for the services of a Plumber, you in the right place:\n")
    user = input("Please enter your name:\n")

    print("Hello \n", user)

    counter += 1

    print("What can we do for you:\n")
while counter == 1:
    print("Reply with the relevent number\n")
    job = (input("1. repair something. 2. install something 3. replace something:\n"))

    if job not in "123":
        counter = 1

    else:
        jobList.append(jobs[job])
        counter += 1

    while counter == 2:
        work = (input("1: toilet, 2: bathtub, 3: sink, 4: geyser, 5: bathroom taps, 6: kitchen taps:\n"))
        if work not in "123456":
            counter = 2

        else:
            workList.append(items[work])
            counter += 1

        while counter == 3:
            add = input("1: get quote, 2: add more:\n")
            if add not in "12":
                counter = 3
            elif add == "1":
                contact = input("Please enter your phone number:\n")

                dict.update({"customer":user, "contact":contact, "job": jobList, "work": workList,"time": time })
                #df.append(dict, ignore_index = True)
                counter += 1
                for x in range(len(jobList)):
                    print(dict['customer']+ ": " + dict["job"][x]+ ": " + dict["work"][x])
            else:
                counter = 1

df = pd.DataFrame([dict])
df.to_csv('my_database.csv', index=False,  mode ="a", header=False)
