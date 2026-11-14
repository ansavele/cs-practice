def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        filename = path.split('/')[-1]

        dot_index = filename.rfind('.')

        if dot_index > 0:
            ext = filename[dot_index + 1:].lower()
        else:
            ext = ""

        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    best_path = sorted(paths, key=lambda p: (-p.count('/'), p))[0]
    return best_path


def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"

    units = ["КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes

    for unit in units:
        size /= 1024.0
        if size < 1024:
            return f"{size:.1f} {unit}"

    return f"{size:.1f} ТБ"
