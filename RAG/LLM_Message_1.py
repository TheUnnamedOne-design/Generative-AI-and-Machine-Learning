from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

messages = [
    SystemMessage(
        content="You are a concise financial analyst."
    ),
    HumanMessage(
        content="What is liquidity risk?"
    )
]

response = llm.invoke(messages)
print(response.content[0]["text"])