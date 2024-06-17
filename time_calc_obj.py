# practice python project to remember how to code in python!!! without using chatgpt to do everything!!!!!

print("\n\nWelcome to my weird time calculator!!!      (object oriented edition)")
print("")
print("Instructions to use:\n1. Type out starting time first (like HH:MM)\n2. type + or - and then the amount of time you want to add or subtract from the starting time. (adding 3 minutes would be like: +0:03)\n3. The resulting time will be returned!\n4. You can continue adding or subtracting from your answer, forever.")
print("\nAlso this uses 24:00 hour time so you don't have to type AM or PM")

# using objects because it works in my brain better
class Time:
    # time has hours and minutes
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    
    def change_time(self, min_to_add): # adding or subtract both work
        self.minute += min_to_add
        self.fix_time()

    # fix the time format so that it makes sense, like if theres more than 60 minutes, or more than 24 hours
    def fix_time(self):
        while self.minute >= 60:
            self.minute -= 60 # trades 60 minutes for 1 hour
            self.hour += 1
        if self.minute < 0:
            while self.minute < 0:
                self.minute += 60
                self.hour -= 1
        self.hour = self.hour % 24  # %= could also be used but thats just confusing
    #to_string function
    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"
    
    def twelveHrClock(self):
        self.fix_time() # fix time just in case. 0 <= self.hour < 24
        ret_str = f"{round((self.hour - 0.00001) % 12):02}:{self.minute:02}"  # most scuffed thing here, but it works
        if self.hour >= 12:
            ret_str += " PM"
        elif self.hour < 12:
            ret_str += " AM"
        return ret_str
    
# the first time a user inputs the time, it's a string so this needs to be done
start_time = input("\n")
hour = int(start_time.split(":")[0])
minute = int(start_time.split(":")[1])

# make time object from user's time input
time_obj = Time(hour, minute)


while True:
    thing = input("") # this is when the user inputs "+0:15" or "-1:23" or something like that

    operation = thing[0] # see the first character (plus or minus)
    dhour = int(thing[1:].split(":")[0])
    dminute = int(thing[1:].split(":")[1])
    dminute += dhour * 60 # get total change in minutes

    if operation == "+":
        time_obj.change_time(dminute)
    elif operation in ['-', '–', '_']:
        time_obj.change_time(-dminute)
    # the data in time_obj gets changed by the ∆t functions

    print("\nAnswer:", time_obj, " ("+time_obj.twelveHrClock()+") ")
