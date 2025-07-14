import wave

obj = wave.open("sample.wav", "rb");

print("number of channels " , obj.getnchannels())
print("smaple width " , obj.getsampwidth())
## this is the frequency
print("frame rate " , obj.getframerate())
print("number of frames " , obj.getnframes())
print("parameters " , obj.getparams())

t_audio =obj.getnframes() /obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames) , type(frames[0]))
print(len(frames))

obj.close()

obj_new = wave.open("new.wav" , "wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(48000)

obj_new.writeframes(frames)
obj_new.close()
