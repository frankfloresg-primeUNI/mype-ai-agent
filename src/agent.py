from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool

from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode


load_dotenv()


# ==========================================
# TOOLS
# ==========================================

@tool
def consultar_stock(producto: str) -> str:
    """Consulta cuántas unidades hay disponibles de un producto."""

    stock = {
        "laptop lenovo": 8,
        "monitor lg": 15,
        "mouse logitech": 25,
        "teclado redragon": 10,
    }

    producto = producto.lower()

    if producto in stock:
        return f"Hay {stock[producto]} unidades de {producto}."

    return f"No encontré información de stock para {producto}."


@tool
def calcular_descuento(precio: float, porcentaje: float) -> float:
    """Calcula el precio final aplicando un descuento."""

    descuento = precio * (porcentaje / 100)

    return round(precio - descuento, 2)


tools = [
    consultar_stock,
    calcular_descuento
]


# ==========================================
# GEMINI
# ==========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
)

llm_with_tools = llm.bind_tools(tools)


# ==========================================
# AGENT
# ==========================================

def agent(state: MessagesState):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# ==========================================
# TOOL NODE
# ==========================================

tool_node = ToolNode(tools)


# ==========================================
# ROUTING
# ==========================================

def should_continue(state: MessagesState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return END


# ==========================================
# GRAPH
# ==========================================

builder = StateGraph(MessagesState)

builder.add_node("agent", agent)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        END: END
    }
)

builder.add_edge("tools", "agent")

graph = builder.compile()


def get_text(message):

    if isinstance(message.content, str):
        return message.content

    if isinstance(message.content, list):

        texts = []

        for block in message.content:

            if isinstance(block, dict):
                if block.get("type") == "text":
                    texts.append(block.get("text", ""))

        return "".join(texts)

    return str(message.content)



# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    question = "Explicame las CNN"

    result = graph.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    final_message = result["messages"][-1]

    print(get_text(final_message))