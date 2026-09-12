import time
from tkinter import Tk, filedialog

from typing_engine import type_text
from docx_loader import load_docx
import config


def select_docx():
    """Open a file picker and let the user choose a DOCX file."""

    root = Tk()
    root.withdraw()

    filename = filedialog.askopenfilename(
        title="Select a DOCX file",
        filetypes=[
            ("Word Documents", "*.docx"),
            ("All Files", "*.*")
        ]
    )

    root.destroy()

    return filename


def main():

    print("GhostWriter")
    print("-" * 30)

    # Select source document
    source_file = select_docx()

    if not source_file:
        print("No file selected.")
        return

    print(f"Selected: {source_file}")

    # Load document
    try:
        text = load_docx(source_file)

    except Exception as error:
        print(f"Could not read the document: {error}")
        return

    if not text.strip():
        print("The selected document contains no readable text.")
        return

    print(f"Loaded: {len(text)} characters")
    print(f"Speed: {config.WPM} WPM")
    print(f"Variation: {config.VARIATION * 100:.0f}%")

    print()
    print("Controls:")
    print("F8  → Pause / Toggle")
    print("F9  → Resume")
    print("ESC → Emergency Stop")

    print()
    print(
        f"You have {config.COUNTDOWN} seconds "
        "to click inside the target application..."
    )

    time.sleep(config.COUNTDOWN)

    type_text(
        text,
        wpm=config.WPM,
        variation=config.VARIATION,
        punctuation_pause=config.PUNCTUATION_PAUSE
    )


if __name__ == "__main__":
    main()