from dotenv import load_dotenv   #Carga variables de entorno desde un archivo .env
from langchain_google_genai import ChatGoogleGenerativeAI   #Clase de LangChain que se conecta con modelos Gemini

from tools_agent import consultar_stock

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-3.6-flash'
)

llm_with_tools = llm.bind_tools(
    [consultar_stock]
)

question = input('Tú: ')
response = llm_with_tools.invoke(question)


tool_call = response.tool_calls[0]

resultado = consultar_stock.invoke(
    tool_call['args']
)

print('RESULTADO DE LA TOOL:')
print(resultado)

print('\nTOOL CALLS: ')
print(response.tool_calls)