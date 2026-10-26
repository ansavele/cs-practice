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

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            records.append(record)
        except ValueError:
            pass
    return records

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for r in records:
        c = r['city']
        total[c] = total.get(c, 0.0) + r['temperature']
        count[c] = count.get(c, 0) + 1
    return {c: round(total[c] / count[c], 1) for c in total}

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ''
    return max(averages, key=lambda c: (averages[c], -ord(c[0])))
