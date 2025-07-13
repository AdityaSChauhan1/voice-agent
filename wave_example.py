import wave

obj = wave.open("sample.wav", "rb");

print("number of channels " , obj.getnchannels())
print("smaple width " , obj.getsampwidth())
print("frame rate " , obj.getframerate())
print("number of frames " , obj.getnframes())
print("parameters " , obj.getparams())