"""Script to copy avatars in a common folder to be used.

The assumption is that all avatars are in "bot-avatars" and "repo-avatars".
"""
import os

from pathlib import Path
from shutil import copy2

REPO_ROOT = Path(__file__).parent


def copy_avatars(avatar_folder: str):
    """Copy all avatars to the ``avatars`` folder.

    Parameters
    ----------
    avatar_folder : str
        Name of the avatar folder relative to the repo root.
    """
    dest_folder = REPO_ROOT / "avatars"
    if not dest_folder.is_dir():
        os.makedirs(dest_folder)
    for avatar_path in (REPO_ROOT / avatar_folder).glob("*"):
        copy2(avatar_path, dest_folder / avatar_path.name)


if __name__ == "__main__":
    for avatar_folder in ("bot-avatars", "repo-avatars"):
        copy_avatars(avatar_folder)
