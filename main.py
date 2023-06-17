import chatgpt
import user_screen

if __name__ == '__main__':
    # create user interface with tkinter
    user_screen.create_screen()
    # call api key
    with open("api.key.txt", "r") as api_key:
        API_KEY = api_key.read()
    # call chat gpt and tell him hsi role
    chat_gpt = chatgpt.ChatGPT(API_KEY, "Sei ein Lehrer: Schreibe zwei bis drei Sätze zu der Leistung eines Schülers")
                                        #"anhand dieser Bewertungskriterien die auf einer Skale von 0 bis 10 getroffen"
                                        #f"wurden:{} Pünktlichkeit:,{} Hausaufgaben erledigt:{}  Mitarbeit:{}"
                                        #f"Konzentration:{}, Kreativität{}:, Soziales Engagement:{}")
    while (frage := input('\n> ')) != "X":
        antwort = chat_gpt.fragen(frage)
        print(antwort)



