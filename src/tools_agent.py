from langchain.tools import tool

@tool
def consultar_stock(producto: str) -> str:
    """Consulta el stock disponible de un producto."""
    stock = {
        "laptop lenovo": 8,
        "monitor lg": 15,
        "mouse logitech": 25,
        "teclado redragon": 10,
    }    

    producto = producto.lower()
    if producto in stock:
        return f"Hay {stock[producto]} unidades de {producto}."
    return f'No encontre información para {producto}'