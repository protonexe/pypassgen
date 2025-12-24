# Secure Password Vault & Generator

A professional-grade Python security tool that generates high-entropy random passwords and memorable passphrases. Designed with modularity and user experience in mind.

## 🚀 Features
- **Dual-Mode Generation**: Switch between complex character strings (Mode 1) and human-friendly word passphrases (Mode 2).
- **Security Validation**: Built-in strength evaluator that judges entropy based on character diversity and length.
- **Persistent Storage**: Automatically logs all generated passwords to `vault.txt` with a unique ID for auditing.
- **Auto-Copy**: Integrated with `pyperclip` to automatically copy the latest password to your clipboard.
- **Clean UI**: Uses f-string padding to provide a tabular, easy-to-read terminal dashboard.

## 🛠️ Technical Skills Demonstrated
- **Modular Programming**: Use of functions and the `if __name__ == "__main__":` guard.
- **Error Handling**: Implemented `try-except` blocks to prevent crashes from invalid user inputs.
- **File I/O**: Practical application of persistent data storage using Python's file handling.
- **External Libraries**: Integration of third-party modules via `pip`.

## 📦 Installation & Usage
1. Clone this repository.
2. Install the required dependency:
   ```bash
   pip install pyperclip