from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


load_dotenv()

@tool
def get_market_rate(asset: str) -> float:
    """Get the mock market rate for a cryptocurrency asset."""

    rates={
        "BTC":60000.00,
        "Eth":3200.0
    }
    return rates.get(asset.upper(), 0.0)



@tool
def get_company_info(asset: str) -> str:
    """Get the company info from various list of comapnies"""

    companies = {
        "APPLE": "Apple is a technology company known for iPhone, Mac, and other consumer electronics.",
        "GOOGLE": "Google is a technology company owned by Alphabet and known for search, cloud, and AI products."
    }
    return companies.get(asset.upper(),"Tech Company")


@tool
def calculate_profit(revenue: float, expenses: float) -> float:
    "Calculate the profit made given the revenue made and the expenses incurred"
    return revenue-expenses


llm=ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

llm_with_tools = llm.bind_tools(
    [
        get_market_rate,
        get_company_info,
        calculate_profit
    ]
)

response = llm_with_tools.invoke(
    "What is the market rate for BTC?"
)

print(response.tool_calls)

