import wave

obj = wave.open("sample.wav", "rb")
print("Number of channels", obj.getnchannels())
print("Sample Width", obj.getsampwidth())
print("Frame Rate", obj.getframerate())
print("Number of frames", obj.getnframes())
#all the parameters :
#print("Parameters", obj.getparams())

#getting time(in seconds) of audio
time_audio = obj.getnframes() / obj.getframerate()
print("Time duration of the audio:", time_audio ,"seconds")

#reading the franes
frames = obj.readframes(-1)
#analysing the type 
print(type(frames), type(frames[0]))
#length of frames
print(len(frames))

obj.close()

obj2 = wave.open("sample.wav", "wb") #write mode

#getters changed to setters
obj2.setnchannels(2)
obj2.setsampwidth(2) 
obj2.setframerate(88200.0)

obj2.writeframes(frames)
obj2.close()

#changed parameters
obj_new = wave.open("sample.wav", "rb")
print("Number of channels", obj_new.getnchannels())
print("Sample Width", obj_new.getsampwidth())
print("Frame Rate", obj_new.getframerate())
print("Number of frames", obj_new.getnframes())
time_audio2 = obj_new.getnframes() / obj_new.getframerate()
print("Time duration of the audio:", time_audio2 ,"seconds")
frames2 = obj_new.readframes(-1)
print(type(frames2), type(frames2[0]))
print(len(frames2))



