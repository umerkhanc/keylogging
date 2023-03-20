import keyboard

def on_press(key):
    with open("typing_log.txt", "a") as file:
        file.write(key.name)

keyboard.on_press(on_press)

print("Recording started. Press 'esc' to stop.")
keyboard.wait('esc')
print("Recording stopped.")
