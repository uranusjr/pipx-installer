#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pathlib
import shutil
import subprocess
import sys


USER_LOCAL = pathlib.Path.home().joinpath(".local")
DEFAULT_HOME = USER_LOCAL.joinpath("pipx")
DEFAULT_BIN_DIR = USER_LOCAL.joinpath("bin")


def _find_exe(env_dir, cmd):
    path = "{}{sep}{}".format(
        env_dir.joinpath("bin"), env_dir.joinpath("Scripts"), sep=os.pathsep
    )
    result = shutil.which(cmd, path=path)
    if not result:
        raise FileNotFoundError(cmd)
    return result


def main():
    os.environ["PIP_REQUIRE_VIRTUALENV"] = "true"
    os.environ["PIP_DISABLE_PIP_VERSION_CHECK"] = "true"

    home = pathlib.Path(os.environ.get("PIPX_HOME") or DEFAULT_HOME)
    home.mkdir(parents=True, exist_ok=True)

    pipx_venv = home.joinpath("venvs", "pipx")
    subprocess.check_call(
        [sys.executable, "-m", "venv", "--prompt=pipx", str(pipx_venv)]
    )

    python = _find_exe(pipx_venv, "python")
    subprocess.check_call([python, "-m", "pip", "install", "pipx"])

    bindir = pathlib.Path(os.environ.get("PIPX_BIN_DIR") or DEFAULT_BIN_DIR)
    bindir.mkdir(parents=True, exist_ok=True)

    pipx_exe = pathlib.Path(_find_exe(pipx_venv, "pipx")).resolve()
    if pipx_exe.is_symlink():
        pipx_exe.symlink_to(bindir.joinpath(pipx_exe.name))
    else:
        shutil.copy2(pipx_exe, bindir.joinpath(pipx_exe.name))

    subprocess.check_call([python, "-m", "pipx", "ensurepath"])


if __name__ == "__main__":
    main()
