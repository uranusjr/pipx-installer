# DON’T USE.

I moved to a Scoop-managed standalone installation method instead.

https://github.com/uranusjr/pipx-standalone

-----

# Install pipx along with other venvs it manages

This script is only intended for myself. Use at your own risks.

Instead of installing pipx globally, it is installed into a venv at
`PIPX_HOME/venvs/pipx` and symlinked/cpoied into `PIPX_HOME/bin`. These
paths are consistant with pipx itself, making it completely self-contained.
