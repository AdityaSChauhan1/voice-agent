## if you are on windows :-
## step 1 :- install chocolatey , it helps managa package
## step 2 :- install ffmpeg using chocolatey
## perform step 1 and 2 on windows powershell in administrator mode
## step 3 :- on terminal of VS code write =>  pip install pydub 


from pydub  import AudioSegment

audio = AudioSegment.from_wav("sample.wav")


audio =audio+6

audio = audio * 2

audio = audio.fade_in(2000)

audio.export("mashup.mp3" , format="mp3")
audio2 = AudioSegment.from_mp3("mashup.mp3")

print("done")