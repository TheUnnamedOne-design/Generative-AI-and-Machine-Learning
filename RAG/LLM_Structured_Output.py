from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

class RiskSummary(BaseModel):
    risk_type: str = Field(description="Type of financial risk")
    severity: str = Field(description="low | medium | high")
    explanation: str

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
structured_llm = llm.with_structured_output(RiskSummary)

result=structured_llm.invoke("Analyse liquidity risk for a startup.")
print(result.risk_type, result.severity)
