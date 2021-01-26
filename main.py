from pydub import AudioSegment
from pydub.playback import play
import os
import random
import simpleaudio.functionchecks as fc
import sys
if sys.platform.startswith('linux'):
	os.system('clear')
	path = os.path.join("/alarm-testing")
else:
	os.system('cls')
	path = os.path.join("C:/alarm-testing-music")


path = os.path.join("/alarm-testing")
print(path)

try:
    os.mkdir(path)
    print("Path made successfully")
except FileExistsError:
    print("Directory exist")

list = [path + "/sum41-in-too-deep.mp3", path + "/sum41-still-waiting.mp3", path + "/scotty-doesnt.mp3"]
url = ['https://github.com/amalyar/alarm-clock/raw/main/sum41-in-too-deep.mp3',
       'https://github.com/amalyar/alarm-clock/raw/main/sum41-still-waiting.mp3',
       'https://raw.githubusercontent.com/amalyar/alarm-clock/main/scotty-doesnt.mp3']  # if song doesn't exists then it will be downloaded from github

for idk in range(0, (len(list))):
    # checks if file exists if not download it
    try:
        f = open(list[idk])
        song = list[idk]
        print(list[idk])
        print("File exist!")

    except FileNotFoundError:
        import wget

        print(url[idk])
        print(list[idk])
        print('File does not exist')
        wget.download(url[idk], list[idk])


import keyboard
import time
import datetime
import threading

test = "ok"
ans1 = 0
checking = ''

# Check the time right now, and print hour and min
now = datetime.datetime.now()
print(now.hour, now.minute)

# Takes the alarm hour and min from me
hour = int(input("Enter the hour: "))
minit = int(input("Enter the min: "))

# Set the alarm time and start the timer time
alarm_time = datetime.datetime.combine(now.date(), datetime.time(hour, minit, 0))
print(alarm_time)

# time.sleep((alarm_time - now).total_seconds())
start = False




# Checks if you are awake by answering "yes", with timer of 10 sec and if there isn't any input then starting again :(
def awake_check_big():
    awake = None
    list_songs_check = []
    list_songs_check = list

    def awakecheck():
        time.sleep(10)
        
        if awake != None:
            print("awake")
            start = True
            print(start)
            mathtest()
        print("\n you didnt answer fast enough so im starting again haha ---__---")
        for i in range(0, (len(list) - 1)):
            print(songs_alone[i])
            sound = AudioSegment.from_mp3(songs_alone[i])
            print("\nlistening lala")
            play(sound)
            awake_check_big()

    l = threading.Thread
    l(target=awakecheck).start()
    awake = input("Are you awake!?")

def mathtest():
    list_songs_check = []
    list_songs_check = list

    score = 0
    count = 1
    while count == 1:
        count = 1
        while count == 1:
            print("If you want to cancle you have to answer the next questions, Goodluck!")

            for i in range(0, 4):
                num1 = random.randint(0, 100)
                num2 = random.randint(0, 100)

                print(num1, '+', num2)
                ans1 = int(input("First quest: "))
                if ans1 != (num1 + num2):
                    print("worng")
                else:
                    print("Good!")
                    score = score + 1
            if score == 0 or score < 3:
                print("Nope")
                print("Im starting again haha --__--")
                sound = AudioSegment.from_file(random.choice(list_songs_check), format="mp3")	
                play(sound)

                

            if score >= 3:
                print("Well Done ! ")
                start = False
                quit()
            count = 2
        break
        


# asking some simple question (with random numbers), and you need to answer at l
songs_alone = []
for num in range(0, (len(list))):
    songs_alone.append(random.choice(list))

while start is False:
    for num1 in range(0, (len(list))):
        print(songs_alone[num1])
        sound = AudioSegment.from_file(songs_alone[num1], format="mp3")
        play(sound)
        print("listening lala")
        awake_check_big()

        if (keyboard.wait('q') == None):
            mathtest()
        else:
            print("hi!")
            sound = AudioSegment.from_file(songs_alone[num1], format="mp3")
            play(sound)
