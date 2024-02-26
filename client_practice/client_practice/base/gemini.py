import textwrap
import google.generativeai as genai
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key="AIzaSyBWq2ZDZshKrFnjPYJLhSwvQ_XVT0G8OzA")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
response = chat.send_message("This is Yuu. Aj. Bill is my teacher. I am studying ICT301")


def reply(prompt):
    global chat
    respond = chat.send_message(prompt)
    return respond.text


question = input("What would you like to ask? ")
print(reply(question))
