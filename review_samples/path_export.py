from pathlib import Path

def export_report(requested_name: str, content: str) -> None:
    # Deliberately unsafe: a user-controlled path can escape the reports folder.
    destination = Path("reports") / requested_name
    destination.write_text(content, encoding="utf-8")
