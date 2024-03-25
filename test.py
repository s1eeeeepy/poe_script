from pynput import keyboard
from flasks import Flask


toggle_key = "p"
kill_key = keyboard.Key.esc


def toggle_event(key):
    if key == keyboard.KeyCode(char=toggle_key):
        Flask.toggle()


flask_1 = Flask(1, 7.4)
flask_2 = Flask(2, 8.8)
flask_3 = Flask(3, 10.5)
flask_5 = Flask(5, 5.2)


def main():
    listener = keyboard.Listener(on_press=toggle_event)
    listener.start()

    for flask in Flask.flasks:
        flask.create_thread()

    listener.join()


if __name__ == "__main__":
    main()
