import google.generativeai as genai
from openai import responses

API_KEY ="AIzaSyArkDikk4BBKZKo1L452OJ2qZyBwaRAKMc"

genai.configure(api_key=API_KEY)

model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat()

print("chat with gemini! type 'exit' to quit")
while True:
    user_input=input("You:")
    if user_input.lower()=="exit":
        break
    response=chat.send_message(user_input)
    print("Gemini:",response.text)