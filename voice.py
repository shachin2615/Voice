import pyttsx3
import speech_recognition as sr
import google.generativeai as ai

ai.configure(api_key="AIzaSyBGgITtEWAfy5hfEBeRM-UAcPWpQqOjNwQ")
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
r = sr.Recognizer()

class TtoS:
    engine: pyttsx3.Engine

    def __init__(self):
        self.engine=pyttsx3.init()
    def text_to_speech(self,i):
        self.engine.say(i)
        self.engine.runAndWait()

def call_fun(given):
    res=chat_session.send_message(given)
    print("bot: ",res.text)
    ch=TtoS()
    ch.text_to_speech(res.text)

model = ai.GenerativeModel(
  model_name="gemini-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "your name is now instrutca you are a educational assiant,limit the responses to one line\n",
      ],
    },
   
  ]
)
if __name__=="__main__":
    count=0
    temp="none"
    while(True):
        print("You:",end=" ")
     
        #given=input("You:")
        
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                given = r.recognize_google(audio2)
        except sr.RequestError as e:
            print("unknown error")
            
        except sr.UnknownValueError:
            print("unknown error")
        
        given=given.lower()
        print(given)   
        if temp!=given:
            call_fun(given)
            temp=given
        elif "exit" == given:
            print("Bot: OKAY")
            break
        