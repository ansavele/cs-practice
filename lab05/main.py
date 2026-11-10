import sys
from logstats import count_levels, top_errors, format_report


def main():
    filename = sys.stdin.readline().strip()

    if not filename:
        return

    with open(filename, encoding="utf-8") as f:
        lines = list(f)

    counts = count_levels(lines)
    errors = top_errors(lines, n=3)

    total_lines = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total_lines)
    print(error_count)
    print(broken_count)

    report_text = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)


if __name__ == "__main__":
    main()