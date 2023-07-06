import chatgpt
import better_user_interface
import openai
import better_user_interface as bui


def create_prompt(criteria):
    prompt = f"""
Sei ein Lehrer: Schreibe zwei bis drei Sätze zu der Leistung eines Schülers 
anhand dieser Bewertungskriterien die auf einer Skale von 0 bis 10 getroffen wurden
und beschränke dich auf eine für ein 
Zeugnis vernünftige länge. Erwähne nicht die Skala oder die dir gegebenen Zahlen:

Pünktlichkeit:{criteria["Pünktlichkeit"]},
Hausaufgaben erledigt:{criteria["Hausaufgaben erledigt"]},
Mitarbeit:{criteria["Mitarbeit"]},
Konzentration:{criteria["Konzentration"]},
Kreativität{criteria["Kreativität"]}:,
Soziales Engagement:{criteria["Soziales Engagement"]}
"""

    return prompt


if __name__ == '__main__':
    # call api key
    with open("api.key.txt", "r") as api_key:
        API_KEY = api_key.read()
        # call chat gpt and tell him hsi role

        def update_func():
            prompt = create_prompt(bui.criteria)
            # chat_gpt = chatgpt.ChatGPT(API_KEY, prompt)
            openai.api_key = API_KEY
            dialog = [{"role": "system", "content": prompt}]
            ergebnis = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=dialog
            )
            answer = ergebnis.choices[0].message.content
            bui.answer_form_gpt = answer
            print(answer)

        def update_gpt_answer():
            # create user interface with tkinter

            better_user_interface.create_screen(update_func)
    update_gpt_answer()

