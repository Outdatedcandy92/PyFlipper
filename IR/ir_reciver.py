import pigpio
import time

RECEIVER_PIN = 23  # GPIO pin for IR receiver

def ir_callback(gpio, level, tick):
    if level == pigpio.FALLING_EDGE:
        print(f"Falling edge detected on pin {gpio}")

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    print("Failed to connect to pigpio daemon.")
    exit()

# Set up the IR receiver pin
pi.set_mode(RECEIVER_PIN, pigpio.INPUT)
pi.callback(RECEIVER_PIN, pigpio.FALLING_EDGE, ir_callback)

print("Listening for IR signals...")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    pi.stop()
