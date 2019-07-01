import speech_recognition as sr
import pyaudio
import fileinput
import random
r = sr.Recognizer()
#audio = sr.AudioFile('knapik.wav')
choice = True
file = 'wyjscie/testing.txt'
r.pause_threshold = 3.3
i = 0
while choice:
    with sr.Microphone() as source:
        statint = input("czas przez który chcesz włączyc nagrywanie"+'\n')
        print("dostosywuje dzwiek otoczenia....")
        r.adjust_for_ambient_noise(source, duration =1)
        print("Mów")
        audio = r.listen(source,timeout=int(statint),phrase_time_limit=int(statint))
        with open(file, 'a', encoding='utf-8') as filein:
            with open('wyjscie/sound{}.wav'.format(random.randrange(1,999)),'wb') as sound:
                sound.write(audio.get_wav_data())
            print('Done!')
            text = r.recognize_google(audio, language = 'pl-PL')
            print(text)
            filein.writelines(' ' + text.capitalize())
            filein.write('')
            print("Chcesz kontynuowac? cokolwiek jesli tak, 'nie' jesli nie ")
            inp = input("wprowadz")
            if inp!='nie':
                continue
            else:
                filein.close()
                break



