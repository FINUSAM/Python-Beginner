from pygame import mixer
import time
import datetime

x=60 # 60 for minutes & 1 for seconds 
start = (time.time()/x)-55

while(True):

	now = time.time()/x
	diff = int(now-start)

	if diff%60==0:
		mixer.init()
		mixer.music.load("water.mp3")
		mixer.music.set_volume(1)
		mixer.music.play()
		print("\nTime for Water.....")
		while True:
			inp = input("Did you drink : ")
			if inp == "drank":
				mixer.music.stop()
				actiontime=datetime.datetime.now()
				actiontimereduced=actiontime.strftime("%m/%d/%Y %H:%M:%S")
				f = open("data.txt", "a")
				f.write(f"\n{actiontimereduced} : Drank Water")
				f.close()
				break

	if diff%30==0:
		mixer.init()
		mixer.music.load("eyes.mp3")
		mixer.music.set_volume(1)
		mixer.music.play()
		print("\nTime for your Eyes.....")
		while True:
			inp = input("Did you do : ")
			if inp == "done":
				mixer.music.stop()
				actiontime=datetime.datetime.now()
				actiontimereduced=actiontime.strftime("%m/%d/%Y %H:%M:%S")
				f = open("data.txt", "a")
				f.write(f"\n{actiontimereduced} : Relaxed Eyes")
				f.close()
				break

	if diff%45==0:
		mixer.init()
		mixer.music.load("physical.mp3")
		mixer.music.set_volume(1)
		mixer.music.play()
		print("\nTime for your Body.....")
		while True:
			inp = input("Did you Exercise : ")
			if inp == "done":
				mixer.music.stop()
				actiontime=datetime.datetime.now()
				actiontimereduced=actiontime.strftime("%m/%d/%Y %H:%M:%S")
				f = open("data.txt", "a")
				f.write(f"\n{actiontimereduced} : Exercised and Stretched")
				f.close()
				break

