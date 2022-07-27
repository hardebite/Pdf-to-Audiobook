
import pandas as pd
import pyttsx3
import PyPDF2
obj=open('Coffee+Machine+Program+Requirements-2.pdf','rb')
pdfR=PyPDF2.PdfFileReader(obj)
cnt=pdfR.numPages
pageobj=pdfR.getPage(cnt-1)
data=pageobj.extractText()

with open("data.txt","a") as opt:
    opt.writelines(data)
with open ("data.txt") as file:

    file=file.read()
    print(file)


# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
text = file
# engine.say(text)
# saving speech audio into a file
engine.save_to_file(text, " audiobook.mp3")

# play the speech
engine.runAndWait()
