# Password Generator and Vault

Educational project to generate passwords and passphrases while storing them locally on disk.

## Features
- **Dual-Mode Generation**: Switch between complex character strings (Mode 1) and human-friendly word passphrases (Mode 2).
- **Security Validation**: Built-in strength evaluator that judges entropy based on character diversity and length.
- **Persistent Storage**: Automatically logs all generated passwords to `vault.txt` with a unique ID for auditing.
- **Auto-Copy**: Integrated with `pyperclip` to automatically copy the latest password to your clipboard.


