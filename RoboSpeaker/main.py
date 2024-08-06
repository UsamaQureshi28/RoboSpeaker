import pyttsx3 as P
if __name__ == '__main__':
   # pass   #es ka mtlb ye ha k hm yhn bd mn wapis ayn gy ya bd mn use krn gy taa k error sy bacha ja sky
   print("*****Welcome to Robo Speaker 2.0 invented by a Musketeer*****\n")
   while(True):
      Sentence=input("Tell me what you want me to speak: ")
      if(Sentence.lower()=="stop"):
         P.speak("Good Bye Friend")
         break
      P.speak(Sentence)
