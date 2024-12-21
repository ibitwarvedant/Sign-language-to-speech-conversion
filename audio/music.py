import gtts
import playsound

text="A"
sound= gtts.gTTS(text,lang="en")
sound.save("sign.mp3") 
playsound.playsound("D:/ML project/American Sign Language/sign.mp3")
