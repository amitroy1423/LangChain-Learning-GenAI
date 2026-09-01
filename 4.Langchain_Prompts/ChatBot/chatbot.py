from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")


chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.text)

print(chat_history)

# the problem is AI: It looks like you forgot to include what you want me to multiply! because the model is not able to understand the context of the conversation. We have to maintain a chat history to provide better context. and the send the full chat history to the model for each new user input. This way, the model can understand the context of the conversation and provide more accurate responses.

#.invove() is capable enough to handle a single message or list of messages. 

# now problem is who send which message to the model. Model dont know which message is from user and which message is from bot. Solution is to send the messages in a structured format, where each message is labeled with its role (user or bot). maintaining a dictionary with keys "role" and "content".
#    user: message from user
#    bot(AI): message from bot
# langchain identifies this problem and provides a solution by using the ChatMessage class. 

# types of messahges:
# 1. System message: This is a message that sets the context for the conversation.
# 2. Human message: This is a message from the user.
# 3. AI message: This is a message from the AI model.