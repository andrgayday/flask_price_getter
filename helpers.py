from datetime import datetime


def validate_time_format(time_str):
    """
    Проверяет, соответствует ли строка времени формату ГГГГ-ММ-ДД ЧЧ:ММ:СС.
    Возвращает True, если формат верный, иначе False.
    """
    try:
        datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
        return True
    except (ValueError, TypeError):
        return False
