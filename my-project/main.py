from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("groq:openai/gpt-oss-20b")
while True:
    user = input("Enter your Question: ")
    if user.lower() == "exit":
        break
    else:
        print("AI: ",model.invoke(user).content)
print("Your Conversation End")  