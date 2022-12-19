# Модуль для выполнения опереаций


def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """Принимает на вход строку-пример.
    Возвращает результат примера."""
    pass


def solve_eq(expr: str) -> str:  # x**3 - 8 = 0 -> "2" # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    pass


def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """Упрощает введенный многочлен"""
    pass


# import sympy   догадаетесь сами, где может пригодиться)

# expr = input('Enter expr: ')
# x = sympy.Symbol('x')
# try:
#     ans = sympy.solve(expr, x)
#     print(ans)
# except ValueError:
#     print('Incorrect input')
