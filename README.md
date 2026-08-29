# phongnt570 QMK userspace

Personal QMK keymap for the GMMK Pro Rev 1 ANSI, optimized for macOS.

- [Keymap documentation](keyboards/gmmk/pro/rev1/ansi/keymaps/phongnt570/readme.md)
- [Printable layout (PDF)](keyboards/gmmk/pro/rev1/ansi/keymaps/phongnt570/layout.pdf)
- [Printable layout generator](keyboards/gmmk/pro/rev1/ansi/keymaps/phongnt570/generate_layout.py)

## Build locally

Install and set up [QMK](https://docs.qmk.fm/newbs_getting_started), then point it at this userspace repository:

```sh
qmk config user.overlay_dir=/path/to/qmk_userspace
qmk userspace-compile
```

The configured build target is `gmmk/pro/rev1/ansi:phongnt570`.

## Update QMK

The GitHub Actions workflow uses a pinned QMK revision so builds remain reproducible. To update it, change `qmk_ref` in `.github/workflows/build_binaries.yaml`, build locally, then commit and push the change.
