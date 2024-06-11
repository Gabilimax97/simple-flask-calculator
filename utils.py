def add(a: float, b: float) -> float:
    """
        Returns a plus b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
        Returns a minus b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
        Returns a times b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
        Returns a divided by b
    """
    return a / b

def operation_as_symbol(operation: str) -> str:
    """
    transforma a operação selecionada 
    pelo usuário em símbolo correspondente 
    """
    data = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/',
    }
    return data[operation]
