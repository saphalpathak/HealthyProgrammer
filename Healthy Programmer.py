from pygame import mixer
import time
import datetime
def dtime():
    return datetime.datetime.now()
def music_type(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        print(f"Afer done enter {stopper}")
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def record(file,type):
    with open(file,"a") as r:
        r.write(f"{str(dtime())} -- {type}\n")
def waterr():
    global water
    music_type("water.mp3","drank")
    water -= 0.38
    print(f"{water} liters water remaining to drink")
    record("water.txt","drank water")
def eyee():
    music_type("eye.mp3","done")
    record("eye.txt","done eye exercise")
def phyy():
    music_type("physical.mp3","done")
    record("physical.txt","done physical exercise")

    
print("Welcome to healthy programmer!!!")
print("You have to drink 3.5 liters of water in 8 hours(0.38 Liter at a time) and do some eye and physical exercise")
water = float(3.5)

while True:
    print("Type start to start:")
    inp = input()
    inp = inp.lower()
    if inp == "start":
        print("Started")
        while True:
            print("Drink water after 30 min")
            time.sleep(1800)
            waterr()
            print("Next: Eye exercise after 30 min")
            time.sleep(1800)
            eyee()
            if (water <= 0.09):
                break
            print("Next: Drink water after 20 min ")        
            time.sleep(1200)
            waterr()
            print("Next: Physical exercise after 30 min")
            time.sleep(1800)
            phyy()
            print("Next: Drink water after 30 min")
            continue
        print("You have drank today's water limit and done all the exercise")
    else:
        continue
        
        
    

