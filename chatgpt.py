#import openai


#class ChatGPT:
#    def __init__(self, api_key, rolle):
 #       openai.api_key = api_key
  #      self.dialog = [{"role": "system", "content": rolle}]
#
 #   def fragen(self, frage):
  #      self.dialog.append({"role": "user", "content": frage})
   #     ergebnis = openai.ChatCompletion.create(
    #        model='gpt-3.5-turbo',
     #       messages=self.dialog
      #  )
       # antwort = ergebnis.choices[0].message.content
        #self.dialog.append({"role": "assistant", "content": antwort})
        #return antwort
