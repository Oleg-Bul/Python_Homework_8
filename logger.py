# Модуль для записи резуьтатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('history.txt', 'a', encoding='utf-8') as history:
        history.write(f'\n{expr} = {result}')


def get_history() -> str:
    """Возвращает содержимое файла с результатами вычислений"""
    with open('history.txt') as f:
        history = [line.rstrip('\n') for line in f]
        return history
