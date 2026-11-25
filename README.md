# Port Monitoring

A small PyQt5 utility that records data coming from a serial (COM) port into a
CSV log while showing the incoming lines in a live console window. It was
written for a device that streams measurements over a virtual COM port, so it is
a personal tool rather than a reusable library.

## Features

- Port name (default `COM5`), baud rate (default `9600`) and read timeout are
  set in the window before starting.
- **Start / Stop** opens the port, reads it line by line and appends
  `unix_timestamp,payload` rows to the chosen log file (`.csv` is added to the
  file name automatically).
- Console panel that tails the log while recording is running.
- The read loop runs in a background thread, so the window stays responsive.
- Failures (for example a busy port) are reported in a message box.

## Requirements

- Python 3.8+, `PyQt5`, `pyserial`; Tkinter for the "save as" dialog (bundled
  with the official Windows Python build).

## Run

```
pip install PyQt5 pyserial
python monitoring.py
```

Press **Start**, pick the destination file, and incoming lines will be written
to it until you press **Stop**.

## Build a standalone executable

```
pyinstaller monitoring.spec
```

## Files

- `monitoring.py` — the whole application: UI, serial reader, CSV logger.
- `monitoring.spec` — PyInstaller build spec.

## Notes

- In practice Windows only: the default port and the file dialog assume it.
- A few UI strings are stored with a broken encoding and render as garbage; the
  behaviour is unaffected, but they are worth rewriting.
