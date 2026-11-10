def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(maxsplit=2)

    if len(parts) < 3:
        raise ValueError("Строка содержит меньше трех частей")

    time, level, message = parts

    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts


def top_errors(lines, n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue

    pairs = [[msg, count] for msg, count in error_counts.items()]
    pairs.sort(key=lambda x: (-x[1], x[0]))
    return pairs[:n]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]

    sorted_levels = sorted(counts.keys())
    for level in sorted_levels:
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for msg, count in errors:
        lines.append(f"- {msg} — {count}")

    return "\n".join(lines) + "\n"