from pathlib import Path
from fnmatch import fnmatch

EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "env",

    # IntelliJ / Java
    ".idea",
    "out",
    "target",
    ".gradle",
    "bin",

    # Maven / build
    ".mvn",
    "build",
    "dist",

    # React / Node
    "node_modules",
    ".next",
    ".nuxt",
    ".vite",
    ".cache",
    "coverage",
}

EXCLUDED_FILES = {
    ".DS_Store",
    "Thumbs.db",

    # IntelliJ
    "*.iml",
    "*.ipr",
    "*.iws",

    # Java
    "*.class",
    "*.jar",
    "*.war",
    "*.ear",
    "*.jmod",
    "hs_err_pid*",
    "replay_pid*",

    # Maven
    "dependency-reduced-pom.xml",
    "pom.xml.tag",
    "pom.xml.releaseBackup",
    "pom.xml.versionsBackup",
    "pom.xml.next",
    "release.properties",

    # React / Node
    "*.tsbuildinfo",
    "*.map",
    "*.min.js",
    "*.min.css",
    "npm-debug.log*",
    "yarn-debug.log*",
    "yarn-error.log*",
    "pnpm-debug.log*",

    # Logs / temp
    "*.log",
    "*.tmp",
}

IGNORE_FILE = ".aihelpignore"


def load_ignore_patterns(root: Path) -> list[str]:
    ignore_path = root / IGNORE_FILE

    if not ignore_path.exists():
        return []

    patterns: list[str] = []

    for line in ignore_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        patterns.append(line)

    return patterns


def matches_pattern(path: Path, root: Path, pattern: str) -> bool:
    relative = path.relative_to(root).as_posix()

    if pattern.endswith("/"):
        directory_name = pattern.rstrip("/")
        return directory_name in path.parts

    return (
        fnmatch(path.name, pattern)
        or fnmatch(relative, pattern)
        or fnmatch(relative, f"**/{pattern}")
    )


def should_exclude(path: Path, root: Path | None = None) -> bool:
    if root is None:
        root = Path.cwd()

    if any(part in EXCLUDED_DIRS for part in path.parts):
        return True

    for pattern in EXCLUDED_FILES:
        if fnmatch(path.name, pattern):
            return True

    for pattern in load_ignore_patterns(root):
        if matches_pattern(path, root, pattern):
            return True

    return False