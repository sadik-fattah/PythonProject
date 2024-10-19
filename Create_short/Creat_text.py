from pydoc import replace
import google.generativeai as genai

API_KEY =''
genai.configure(api_key=API_KEY)

prompt = (
    "tell me about Islamic History a last then 60 seconds"
)
model = genai.GenerativeModel(
    'gemini-1.5-flash'
)
chat = model.start_chat(history=[])
response = chat.send_message(prompt)

filetext = "script.txt"
with open(filetext, 'a') as file:
    file.write(response.text.replace(".","\n"))

    print(f" Prompt create sucssflly to {filetext}")