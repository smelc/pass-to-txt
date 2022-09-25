#!/usr/bin/env python3
""" Main entry point """

import os
from pathlib import Path
import subprocess
import sys


def go_over_dir(root: Path, pdir: Path) -> None:
    """
    Args:
        root: The root level of the password store (~/.password-store)
        pdir: A directory within root
    """
    relative: Path = pdir.relative_to(root)
    segments: list[str] = str(relative).split(os.sep)
    indent: str = "  " * (len(segments) - 1)
    if root is not pdir:
        print(f"{indent}└─ {os.path.basename(relative)}")
    for member in pdir.iterdir():
        if member.is_dir():
            go_over_dir(root, member)
        elif os.path.isfile(member) and str(member).endswith(".gpg"):
            process_run = subprocess.run(
                ["gpg", "--decrypt", member.absolute()], check=True, capture_output=True, text=True
            )
            output: str = process_run.stdout.rstrip()
            print(f"{indent}  └─ {os.path.basename(member).removesuffix('.gpg')}")
            for line in output.split("\n"):
                print(f"{indent}    {line}")


def _main() -> int:
    """
    Returns:
        An error code
    """
    home: Path = Path.home()
    password_store: Path = home.joinpath(".password-store")
    if not password_store.is_dir():
        print(f"{password_store} is not a directory!")
        return 1
    go_over_dir(password_store, password_store)
    return 0


if __name__ == "__main__":
    sys.exit(_main())
