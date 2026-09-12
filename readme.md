# GhostWriter

GhostWriter is a Python-based keyboard automation project that reads text from a DOCX document and types the extracted content into a selected target application.

The project is being developed incrementally with a modular architecture so that document processing, typing behavior, configuration, and the user interface can be extended independently.

> **Project Status:** Early development / CLI prototype

---

## Features

### Current Features

- Read text from `.docx` files
- Select a DOCX file using a file picker
- Type extracted text using PyAutoGUI
- Configurable typing speed using WPM
- Configurable timing variation
- Additional pauses after punctuation
- Pause and resume typing
- Emergency stop during a typing session
- UTF-8 text handling
- Modular Python project structure

### Planned Features

- Graphical user interface
- Advanced DOCX formatting extraction
- Formatting-aware document processing
- Improved progress tracking
- Start/Pause/Resume/Stop controls in the GUI
- Improved error handling
- Application settings
- Output/document management
- Automated testing

---

## Project Structure

```text
GhostWriter/
│
├── .venv/                 # Local Python virtual environment
│
├── config.py              # Application configuration
├── docx_loader.py         # DOCX text extraction
├── guide.md               # Development/usage guide
├── main.py                # Main application entry point
├── source.docx            # Sample DOCX input
├── source.txt             # Sample text input
├── typing_engine.py       # Typing automation engine
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
│
└── __pycache__/           # Python-generated cache (not committed)