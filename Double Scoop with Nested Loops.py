#Task 1 Your Mood Tracker: Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week.
#Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly
#select a mood from a predefined list and print it. Use the random module again to randomly select the mood.

import random                                                                                                   #imported the random package to be able to make a random choice later

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]                    #defined a list containing the days of the week
possible_moods = ["happy", "sad", "energetic", "tired", "calm", "relaxed", "up-beat", "angry", "sleepy"]        #defined a list containing possible moods
time_of_day = ["morning", "afternoon", "evening"]                                                               #defined a list for the time of day

for day in day_of_week:                                                                                         #for loop to iterate through the day_of_week list
    for time in time_of_day:                                                                                    #nested for loop to iterate through the time_of_day list
        if time == "morning":                                                                                   #if statement to create a unique variable for morning
            morning_mood = random.choice(possible_moods)                                                        #setting up the variable morning_mood to be a random pick from the possible_moods list
        elif time == "afternoon":                                                                               #elif statement to create a unique variable for afternoon
            afternoon_mood = random.choice(possible_moods)                                                      #setting up the variable afternoon_mood to be a random pick from the possible_moods list
        elif time == "evening":                                                                                 #elif statemetn to crate a unique variable for evening
            evening_mood = random.choice(possible_moods)                                                        #setting up the variable evening_mood to be a random pick from the possible_moods list
    print(f"According to my mood tracker today, {day}, I felt {morning_mood} this morning, {afternoon_mood} this afternoon, and {evening_mood} this evening.")      #print statement
    


