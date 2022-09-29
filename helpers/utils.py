import os
import pathlib


def get_project_root() -> pathlib.Path:
    """Get pytest project root, based on conftest.py location

    Returns: absolute path of project's root directory

    """
    root_dir = pathlib.Path().resolve().parent
    if not os.path.exists(os.path.join(root_dir, 'conftest.py')):
        root_dir = pathlib.Path().resolve()
        if not os.path.exists(os.path.join(root_dir, 'conftest.py')):
            raise RuntimeError('Cannot find conftest.py in root directory')
        return root_dir

    return root_dir
