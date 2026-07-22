import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

# ---------------- GPIO SETUP ----------------

GPIO.setwarnings(False)
GPIO.cleanup()

time.sleep(1)

GPIO.setmode(GPIO.BCM)

# ---------------- PIN DEFINITIONS ----------------

TRIG = 23
ECHO = 24
BUZZER = 18
FLOW_SENSOR = 17
RELAY = 27

# ---------------- GPIO CONFIG ----------------

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(BUZZER, GPIO.OUT)

GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(RELAY, GPIO.OUT)

GPIO.output(TRIG, False)

# ---------------- LCD SETUP ----------------

lcd = CharLCD('PCF8574', 0x27)

time.sleep(2)

lcd.clear()

# ---------------- FLOW VARIABLES ----------------

pulse_count = 0
last_state = 1

PULSE_TARGET = 5

# ---------------- RELAY TEST ----------------
# LOW = Relay ON
# HIGH = Relay OFF

GPIO.output(RELAY, GPIO.LOW)

print("Valve OPEN")

# ---------------- DISTANCE FUNCTION ----------------

def get_distance():

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    stop = time.time()

    timeout = time.time()

    while GPIO.input(ECHO) == 0:

        start = time.time()

        if time.time() - timeout > 1:
            return 0

    timeout = time.time()

    while GPIO.input(ECHO) == 1:

        stop = time.time()

        if time.time() - timeout > 1:
            return 0

    duration = stop - start

    distance = duration * 17150

    return round(distance, 2)

# ---------------- MAIN LOOP ----------------

try:

    while True:

        # -------- DISTANCE --------

        distance = get_distance()

        # -------- FLOW SENSOR --------

        current_state = GPIO.input(FLOW_SENSOR)

        if current_state == 0 and last_state == 1:

            pulse_count += 1

            print("Pulse:", pulse_count)

            time.sleep(0.005)

        last_state = current_state

        # -------- LCD DISPLAY --------

        lcd.clear()

        lcd.write_string(f"Dist:{distance}cm")

        lcd.crlf()

        lcd.write_string(f"Pulse:{pulse_count}")

        # -------- BUZZER --------

        if distance < 10 and distance != 0:

            GPIO.output(BUZZER, True)

        else:

            GPIO.output(BUZZER, False)

        # -------- LIMIT REACHED --------

        if pulse_count >= PULSE_TARGET:

            print("LIMIT REACHED")

            lcd.clear()

            lcd.write_string("LIMIT REACHED")

            lcd.crlf()

            lcd.write_string("Valve CLOSED")

            # Buzzer ON
            GPIO.output(BUZZER, True)

            # -------- CLOSE RELAY --------
            # VERY IMPORTANT

            GPIO.output(RELAY, GPIO.HIGH)

            print("Relay OFF")
            print("Valve CLOSED")

            # Wait
            time.sleep(5)

            GPIO.output(BUZZER, False)

            break

        time.sleep(0.05)

except KeyboardInterrupt:

    print("Stopped")

finally:

    GPIO.output(BUZZER, False)

    # KEEP RELAY OFF
    GPIO.output(RELAY, GPIO.HIGH)

    lcd.clear()

    GPIO.cleanup()

    print("System Ended")
