# WhatsBotMessages

WhatsBotMessages is a small Windows-oriented Python utility that automates
message sending in WhatsApp Web through Selenium. It reads recipients from a
text file, reads one message body from another text file, sends that message
to each recipient, and optionally sends media files with fixed filenames.

This repository contains an early/BETA implementation. It is not an official
WhatsApp API client and has no browser-independent delivery service.

## User Flow

The current script (`whatsbotmessage.py`) performs this flow:

1. Read `contatos.txt` and `mensagem.txt` from the current working directory.
2. Check for optional `midia.mp4` and `midia.jpg` files in that directory.
3. Open `https://web.whatsapp.com/` in Chrome using Selenium.
4. Wait 20 seconds for WhatsApp Web to become available and for the user to
   complete any required browser authentication.
5. Search for the first recipient, send the message, and send any available
   media.
6. Repeat the message and media send for each remaining line in
   `contatos.txt`.
7. Print a count and elapsed time, wait three seconds, and close the browser.

The implementation locates WhatsApp Web controls using selectors that include
Portuguese UI text and CSS class names. These selectors can stop working when
WhatsApp Web changes.

## Project Structure

| Path | Purpose |
| --- | --- |
| `whatsbotmessage.py` | Selenium automation entry point. |
| `contatos.txt` | One recipient or group name per line. The tracked file is currently empty. |
| `mensagem.txt` | Message body. The tracked file is currently empty. |
| `midia.mp4` | Optional video sent after each message when present. Not included in the repository. |
| `midia.jpg` | Optional image sent after each message when present. Not included in the repository. |
| `chromedriver.exe` | Windows ChromeDriver binary used by the source script. |
| `whatsbotmessage.spec` | PyInstaller specification for the executable build. |
| `script.iss` | Inno Setup installer script with machine-specific paths. |
| `dist/`, `build/`, and `Instalador What Bot Message.zip` | Checked-in Windows build/installer artifacts. |
| `icone.ico` | Application icon used by the build configuration. |
| `obs.txt` | Notes listing the optional media filenames. |

There is no `requirements.txt`, `pyproject.toml`, package manifest, database,
configuration directory, logging directory, or automated test suite. There is
also no application HTML or JavaScript source; HTML and JavaScript under the
build artifacts are generated or bundled dependency files.

## Prerequisites

- Windows is the supported environment indicated by `chromedriver.exe`, the
  Windows paths in the source, and the Inno Setup configuration.
- Google Chrome must be installed.
- A ChromeDriver version compatible with the installed Chrome version must be
  available. The repository contains `chromedriver.exe`, but it may be stale.
- Python is required to run the source script. The bundled build artifacts
  indicate Python 3.10, but the project does not declare a supported Python
  version.
- A WhatsApp account with access to WhatsApp Web is required.

## Local Run

Clone the repository using the public HTTPS URL:

```bash
git clone https://github.com/xfelipealves/WhatsBotMessages.git
cd WhatsBotMessages
```

Create and activate a virtual environment in PowerShell:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install selenium webdriver-manager
```

Prepare the inputs:

- Put one WhatsApp contact or group name on each line of `contatos.txt`.
- Put the message text in `mensagem.txt`.
- Optionally place `midia.mp4` and/or `midia.jpg` in the repository root.

Run the source script from the repository root:

```powershell
python .\whatsbotmessage.py
```

The script does not accept command-line options or environment-variable
configuration. It uses the files and driver path hard-coded in the source.
The bundled executable in `dist\whatsbotmessage\whatsbotmessage.exe` is an
alternative Windows artifact, but it has not been documented as a current,
reproducible release.

## Configuration and Credential Safety

- No API keys, passwords, or credentials are defined in the source.
- WhatsApp Web authentication happens in the browser. Do not share QR codes,
  browser profiles, cookies, or session data.
- Treat recipient lists and message files as potentially sensitive. Review and
  redact them before publishing or attaching logs/builds.
- Do not commit real recipient data, private message content, or media unless
  it is intentionally public and every recipient has provided the required
  consent.
- The repository has no `.gitignore`; local sensitive files are not
  automatically excluded.
- Use the automation only where recipients have consented and in accordance
  with WhatsApp terms and applicable law.

## Testing and Status

There are no automated tests, CI configuration, dependency lockfiles, or
declared release process. Browser execution was not made part of the static
validation for this documentation pass because it requires a live WhatsApp Web
session, a compatible Chrome/ChromeDriver pair, and real recipient data.

Known implementation limitations include:

- The first recipient is handled separately from the remaining lines.
- Search and message selectors depend on WhatsApp Web's current DOM and
  Portuguese labels.
- The search field is not cleared by the script between recipients.
- The script uses fixed 20-second and 1.5-second sleeps instead of robust
  readiness checks for the full flow.
- Media support is limited to the exact filenames `midia.mp4` and `midia.jpg`.
- The source uses Windows-style paths and a relative ChromeDriver path.
- The current Selenium invocation and bundled ChromeDriver may require updates
  for current Selenium/Chrome releases.
- The installer script contains absolute paths from the original development
  machine and is not portable without editing.

## Contributing

There is no `CONTRIBUTING.md` or formal contribution policy in this
repository. Proposed improvements can be submitted as a pull request, with
changes kept focused and sensitive test data excluded.

## License

No `LICENSE` file or open-source license declaration is present. Until the
maintainer adds one or grants permission, treat the repository as having no
granted redistribution or reuse license.
