#Task 1 Your Mood Today: Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm".
#Using the range() function, loop through every day of the week and for each day randomly select a mood from the list and print it. Ensure that your program includes the 
#use of the random module to select the mood.

import random                                                                                                   #imported the random package to be able to make a random choice later

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]                    #defined a list containing the days of the week
possible_moods = ["happy", "sad", "energetic", "tired", "calm", "relaxed", "up-beat", "angry", "sleepy"]        #defined a list containing possible moods

for day in day_of_week:                                                                                         #for statement iterating over the day_of_week list
    mood = random.choice(possible_moods)                                                                        #random choice function to randomly select a mood from the list of moods for the day being iterated

    print(f"Today is {day} and I feel {mood}.")                                                                 #print statement inside loop to print off the day and mood

    

