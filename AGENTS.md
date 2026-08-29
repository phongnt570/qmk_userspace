# Repository instructions

## Scope

This repository is the source of truth for phongnt570's personal QMK userspace. The maintained keymap is:

`keyboards/gmmk/pro/rev1/ansi/keymaps/phongnt570`

Use a separate `qmk_firmware` checkout only as the upstream firmware and build dependency. On the owner's current machine it is `/Users/tuanphong/qmk_firmware`. Do not mirror personal keymap edits into that checkout or treat its legacy copy as authoritative.

## Working rules

- Start by checking `git status` and reading the keymap's `readme.md`.
- Keep changes scoped to this userspace unless the task explicitly concerns upstream QMK.
- Keep `keymap.c`, `config.h`, `rules.mk`, `readme.md`, and `generate_layout.py` consistent.
- Generate `layout.pdf` only with the tracked `generate_layout.py` beside it. Never create the PDF with an untracked one-off script outside this repository.
- If the visible layout changes, update the generator and documentation, regenerate the PDF, render every page to images, and visually inspect alignment, clipping, and legibility.
- Do not commit generated files: `.bin`, `.hex`, and `.uf2` firmware and the generated `layout.pdf` are build artifacts and are ignored.
- Preserve the exact QMK commit in `.github/workflows/build_firmware.yaml`. Do not replace `qmk_ref` with a moving branch.

## Verification

The local QMK configuration should point `user.overlay_dir` at this repository. Verify and build with:

```sh
qmk userspace-list
qmk userspace-compile
git diff --check
git status --short
```

The expected target is `gmmk/pro/rev1/ansi:phongnt570`. Do not report success unless the userspace build completes successfully.

## Printable layout

The layout generator and its pinned dependency are stored with the keymap:

- `keyboards/gmmk/pro/rev1/ansi/keymaps/phongnt570/generate_layout.py`
- `keyboards/gmmk/pro/rev1/ansi/keymaps/phongnt570/requirements-layout.txt`

Use an existing compatible Python environment, or create the ignored root `.venv` when the dependency is missing:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r keyboards/gmmk/pro/rev1/ansi/keymaps/phongnt570/requirements-layout.txt
.venv/bin/python keyboards/gmmk/pro/rev1/ansi/keymaps/phongnt570/generate_layout.py
```

The command writes `layout.pdf` beside the generator. The PDF is ignored by git and never committed; the tracked generator is the source of truth, and the output is deterministic and includes a fingerprint of `keymap.c`, `config.h`, and `rules.mk`. After changing the generator, regenerate the PDF, render both pages with Poppler `pdftoppm`, and inspect the PNGs before committing the generator change.

## Hardware safety

Compiling firmware is allowed as part of normal verification. Never run `qmk flash`, enter the keyboard bootloader, or otherwise modify the connected keyboard unless the user explicitly asks to flash it in the current task. Before flashing, confirm the exact keyboard target and explain when the user must enter the bootloader.

## Git workflow

- Commit each completed logical step separately with a concise imperative commit message.
- Preserve unrelated user changes and never rewrite published history.
- Push only when the task includes publishing or the user explicitly asks for it.
- After a push that changes firmware or build configuration, verify the GitHub Actions run and the `latest` Release artifact.

## Updating QMK

When testing a newer QMK version:

1. Fetch the current official `qmk/qmk_firmware` revision in the companion checkout.
2. Build this userspace against the exact candidate commit.
3. Update `qmk_ref` to that full commit SHA only after the build passes.
4. Commit and push the pin update as its own logical step.
5. Verify GitHub Actions and the generated Release before considering the update complete.
