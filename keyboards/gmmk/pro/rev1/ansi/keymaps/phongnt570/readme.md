# phongnt570 keymap

A two-layer macOS-oriented keymap for the GMMK Pro Rev 1 ANSI.

Printable reference: [keymap layout (PDF)](layout.pdf).

## Base layer

- The main ANSI layout is unchanged.
- The key beside the encoder sends Play/Pause; pressing the encoder sends Mute.
- The navigation column is Delete, Page Up, Page Down, End.
- Left modifiers are Control, Option, Command.
- Right modifiers are Command, Option, Fn; the Fn key opens the Fn layer.
- Turning the encoder adjusts system volume.

## Fn layer

Keys not listed here are transparent and fall through to the base layer.

| Key | Action |
| --- | --- |
| Esc | Toggle RGB matrix |
| F1 / F2 | Display brightness down / up |
| F3 | Mission Control |
| F4 | Spotlight (`Command` + `Space`) |
| F5 / F6 | RGB brightness down / up |
| F7 / F8 / F9 | Previous track / play-pause / next track |
| F10 / F11 / F12 | Mute / volume down / volume up |
| `\` | Enter the bootloader |
| Space | Emoji and Symbols (`Control` + `Command` + `Space`) |
| N | Toggle NKRO |
| Q / W | RGB brightness down / up |
| A / S | RGB saturation down / up |
| Z / X | RGB hue down / up |
| Page Down / Page Up | RGB animation speed down / up |
| Left / Right | Home / End |
| Down / Up | Previous / next RGB effect |
| Encoder | RGB brightness down / up |

The RGB matrix turns off after 20 minutes without keyboard activity and resumes on the next input.

## Build

```sh
qmk compile -kb gmmk/pro/rev1/ansi -km phongnt570
```

## Flash

Press `Fn` + `\` to enter the bootloader, then run:

```sh
qmk flash -kb gmmk/pro/rev1/ansi -km phongnt570
```
