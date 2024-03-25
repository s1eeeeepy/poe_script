from pynput import keyboard
from flasks import Flask

toggle_key = keyboard.KeyCode(char="-")


def toggle_event(key):
    if key == toggle_key:
        Flask.toggle()


flask_1 = Flask(1, 5.2)
flask_2 = Flask(3, 10.5)


def main():
    listener = keyboard.Listener(on_press=toggle_event)
    listener.start()

    for flask in Flask.flasks:
        flask.create_thread()

    listener.join()


if __name__ == "__main__":
    main()
