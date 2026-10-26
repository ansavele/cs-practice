def parse_record(line: str) -> dict:
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError('Ожидалось 3 поля')
    city, temp_str, date = parts
    if not city or not date:
        raise ValueError('Город или дата пустые')
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError('Температура не число')
    return {'city': city, 'temp': temp, 'date': date}
