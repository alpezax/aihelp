from pathlib import Path

from aihelp.services.ignore_service import should_exclude


def iter_project_files(root: Path):
    for path in sorted(root.rglob("*")):
        if should_exclude(path, root):
            continue
        if path.is_file():
            yield path


def render_files_context(root: Path) -> str:
    blocks: list[str] = []

    for file_path in iter_project_files(root):
        relative_path = file_path.relative_to(root)

        blocks.append("=" * 80)
        blocks.append(f"FILE: {relative_path}")
        blocks.append("=" * 80)

        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            blocks.append("[No se puede mostrar: fichero no es texto UTF-8]")
            blocks.append("")
            continue
        except Exception as exc:
            blocks.append(f"[Error leyendo fichero: {exc}]")
            blocks.append("")
            continue

        blocks.append(content)
        if not content.endswith("\n"):
            blocks.append("")
        blocks.append("")

    return "\n".join(blocks)