import keyboard
import time

def capture_keys(duration):
    start_time = time.time()
    keys_pressed = []

    while time.time() - start_time < duration:
        try:
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                keys_pressed.append(event.name)
        except keyboard.KeyboardEvent as e:
            print(e)

    return keys_pressed

if __name__ == "__main__":
    duration = 30  # seconds
    keys_pressed = capture_keys(duration)

    print("Keys pressed:")
    print(''.join(keys_pressed))
