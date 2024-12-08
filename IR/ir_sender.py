import pigpio
import time

TRANSMITTER_PIN = 18  # GPIO pin for IR transmitter

def send_pulse(gpio, frequency, duty_cycle, duration):
    period = 1.0 / frequency
    high_time = period * duty_cycle
    low_time = period - high_time
    end_time = time.time() + duration

    while time.time() < end_time:
        pi.write(gpio, 1)
        time.sleep(high_time)
        pi.write(gpio, 0)
        time.sleep(low_time)

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    print("Failed to connect to pigpio daemon.")
    exit()

# Set up the IR transmitter pin
pi.set_mode(TRANSMITTER_PIN, pigpio.OUTPUT)

try:
    print("Sending IR signal...")
    send_pulse(TRANSMITTER_PIN, frequency=38000, duty_cycle=0.5, duration=1)  # 38 kHz for 1 second
finally:
    pi.write(TRANSMITTER_PIN, 0)
    pi.stop()
