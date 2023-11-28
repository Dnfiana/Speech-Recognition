import speech_recognition as srec
import webbrowser
import time
import datetime
import pywhatkit 
import playsound
from playsound import playsound
from gtts import gTTS

codingers = "hans"

def berbicara (text):     
    bahasa = "id"   
    tts = gTTS(text=text, lang= bahasa)
    filename = "Bicara.mp3"
    tts.save(filename)
    playsound("C:\\SHOLIKHAN\\SEMESTER 6\\AI Programming\\Bicara.mp3") 

def setTime():
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 11:
        berbicara("Hai aku michelle, selamat pagi" + codingers)
                 
    elif hour >= 12 and hour < 14:
        berbicara("Hai aku michelle, selamat siang" + codingers)
        
    elif hour >= 15 and hour < 17:
        berbicara("Hai aku michelle, selamat sore" + codingers)
     
    elif hour >= 18 and hour < 2:
        berbicara("Hai aku michelle, selamat malam" + codingers)
       
    else:
        berbicara("Hai aku michelle, ada yang bisa aku bantu") 

def dapat_audio():
   mendengar = srec.Recognizer()
   with srec.Microphone() as source:
       print("Mendengarkan....") 
       mendengar.pause_threshold = 0.7
       audio = mendengar.listen(source,0,2)

   try:
       print("Mengenali....") 
       query = mendengar.recognize_google(audio, language= "id-ID")
       print(f"Anda Bilang : {query}")

   except:
    return ""

   query = str(query)    
   return query.lower()     
time.sleep(3)

def run_michelle():          
    dengar = dapat_audio()
    if 'putar lagu' in dengar:
        song = dengar.replace("putar lagu", "")
        print("mainkan lagu" + song)
        berbicara("mainkan lagu" + song)
        pywhatkit.playonyt(song)

    elif "jam berapa sekarang" in dengar:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print (time)
        berbicara("sekarang" + time)

    elif "buka google" in dengar:
        webbrowser.open("https://google.com")
        berbicara("google siap digunakan")

    elif "buka youtube" in dengar:
        webbrowser.open("https://youtube.com")
        berbicara("youtube siap digunakan")

    elif "berita hari ini" in dengar:
        webbrowser.open("https://www.cnnindonesia.com/")
        berbicara("beberapa berita hari ini")
    
    else:
        berbicara("maaf perintah ini tidak tersedia")
    
setTime()
while True:
    dengar = dapat_audio()
    time.sleep(3)
    run_michelle()
    

