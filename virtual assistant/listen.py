import speech_recognition

robot_ear=speech_recognition.Recognizer()
with speech_recognition.Microphone()as mic:
	print("Robot: i'm listening ")
	audio=robot_ear.listen(mic)

try:
	you= robot_ear.recognize_google(audio)
except:
 	you== "" 

print("you :"+you) 