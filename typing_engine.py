import pyautogui
import time
import random
import threading

from pynput import keyboard


class TypingController:
    def __init__(self):
        self.paused = False
        self.stopped = False

    def toggle_pause(self):
        self.paused = not self.paused

        if self.paused:
            print("\n⏸ Typing paused. Press F9 to resume.")
        else:
            print("\n▶ Typing resumed.")

    def stop(self):
        self.stopped = True
        print("\n🛑 Typing stopped.")

    def start_listener(self):
        def on_press(key):

            if key == keyboard.Key.f8:
                self.toggle_pause()

            elif key == keyboard.Key.f9:
                self.paused = False
                print("\n▶ Typing resumed.")

            elif key == keyboard.Key.esc:
                self.stop()
                return False

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        return listener


def calculate_delay(wpm):
    """Calculate approximate character delay from WPM."""

    characters_per_minute = wpm * 5

    return 60 / characters_per_minute


def type_text(
    text,
    wpm=45,
    variation=0.25,
    punctuation_pause=True
):
    """Type text with pause/resume/stop controls."""

    controller = TypingController()

    listener = controller.start_listener()

    base_delay = calculate_delay(wpm)

    try:

        for character in text:

            # Wait while paused
            while controller.paused:

                if controller.stopped:
                    return

                time.sleep(0.1)

            # Stop immediately
            if controller.stopped:
                return

            # Calculate variable delay
            minimum = base_delay * (1 - variation)
            maximum = base_delay * (1 + variation)

            delay = random.uniform(
                minimum,
                maximum
            )

            pyautogui.write(character)

            # Punctuation pauses
            if punctuation_pause:

                if character in ".!?":
                    time.sleep(delay + 0.3)

                elif character in ",;:":
                    time.sleep(delay + 0.15)

                elif character == " ":
                    time.sleep(delay * 1.2)

                else:
                    time.sleep(delay)

            else:
                time.sleep(delay)

    finally:

        listener.stop()

        if controller.stopped:
            print("Typing session terminated.")
        else:
            print("Typing session finished.")