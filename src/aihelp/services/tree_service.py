from pathlib import Path

from aihelp.services.ignore_service import should_exclude


def _build_tree(root: Path, current: Path, prefix: str = "") -> list[str]:
    entries = [
        p for p in sorted(current.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        if not should_exclude(p, root)
    ]

    lines: list[str] = []

    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "
        lines.append(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            extension = "    " if index == len(entries) - 1 else "│   "
            lines.extend(_build_tree(root, entry, prefix + extension))

    return lines


def render_tree(root: Path) -> str:
    lines = [root.resolve().name]
    lines.extend(_build_tree(root, root))
    return "\n".join(lines)