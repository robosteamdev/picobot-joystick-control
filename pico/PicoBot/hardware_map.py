# hardware_map.py
#
# Pins, I2C addresses and servo limits of the PicoBot.
# Based on https://github.com/robosteamdev/picobot-web-control
# Change a value only if your robot is wired or built differently.

# ══════════════════════════════════════════════════════════════════════════════
# MOTOR PCA9685  (picobot_motors.py)
# ══════════════════════════════════════════════════════════════════════════════
# All motor drive signals go through a PCA9685 on I2C bus 0.
# There are no direct GPIO motor PWM/direction pins.
#
# Three channels per motor: (pwm_ch, in1_ch, in2_ch)
#   pwm_ch : speed — pca.pwm(ch, 0, 0..4095)
#   in1_ch : direction bit 1 — 0 = LOW, 4095 = HIGH
#   in2_ch : direction bit 2
#
# Direction encoding (picobot_motors.py MotorDir, setLevel()):
#   forward  : IN1=LOW(0),     IN2=HIGH(4095), PWM=speed
#   backward : IN1=HIGH(4095), IN2=LOW(0),     PWM=speed
#   stop     : IN1=0, IN2=0, PWM=0
#
# Physical motor → firmware name (assembly manual A/B/C/D → picobot_motors.py names):
#   A1/A2 front-left  → LeftFront  → FL
#   B1/B2 back-left   → LeftBack   → BL
#   C1/C2 front-right → RightFront → FR
#   D1/D2 back-right  → RightBack  → BR

MOTOR_I2C_BUS  = 0
MOTOR_I2C_SDA  = 20       # GP20
MOTOR_I2C_SCL  = 21       # GP21
MOTOR_I2C_FREQ = 100_000
MOTOR_PCA_ADDR = 0x40
MOTOR_PCA_FREQ = 50       # Hz

MOTOR_FL_CHS = (0,  1,  2)   # (pwm, in1, in2)
MOTOR_BL_CHS = (3,  4,  5)
MOTOR_FR_CHS = (6,  7,  8)
MOTOR_BR_CHS = (9,  10, 11)

# No direct GPIO motor pins — intentionally empty.
MOTOR_INPUT_PINS = ()

# ══════════════════════════════════════════════════════════════════════════════
# ARM / SERVO PCA9685  (picobot_arm.py)
# ══════════════════════════════════════════════════════════════════════════════
# Separate PCA9685 on I2C bus 1.
# picobot_arm.py: I2C(id=1, sda=Pin(2), scl=Pin(3))
# Assembly manual confirms GP2=SDA, GP3=SCL.

ARM_I2C_BUS  = 1
ARM_I2C_SDA  = 2        # GP2
ARM_I2C_SCL  = 3        # GP3
ARM_I2C_FREQ = 400_000  # MicroPython I2C default; arm.py did not set freq
ARM_PCA_ADDR = 0x40
ARM_PCA_FREQ = 50       # Hz

SERVO_BASE_CH = 0
SERVO_ARM_CH  = 1
SERVO_CLAW_CH = 2

# Servo pulse range  (picobot_arm.py)
# min_pulse=102 ticks, max_pulse=512 ticks at 4096 ticks / 20 ms period
# => 102/4096 × 20 000 µs ≈ 498 µs  (rounds to 500 µs at 0°)
# => 512/4096 × 20 000 µs = 2500 µs (at 180°)
SERVO_PULSE_MIN_US = 500
SERVO_PULSE_MAX_US = 2500

# ══════════════════════════════════════════════════════════════════════════════
# MECANUM MIXER  (picobot.py)
# ══════════════════════════════════════════════════════════════════════════════
# picobot.py starf_right(): FL=fwd, BL=back, FR=back, BR=fwd
# Matches X-pattern mecanum with s=+1 → strafe right.
# => STRAFE_SIGN = +1.
STRAFE_SIGN = 1  # set to -1 if the robot strafes the wrong way

# ══════════════════════════════════════════════════════════════════════════════
# DISTANCE SENSOR
# ══════════════════════════════════════════════════════════════════════════════
TRIG_PIN = 27   # GP27 — HC-SR04 Trig
ECHO_PIN  = 26  # GP26 — HC-SR04 Echo

# ══════════════════════════════════════════════════════════════════════════════
# OPTIONAL SETTINGS
# ══════════════════════════════════════════════════════════════════════════════

# GPIO of a motor driver enable (STBY / nSLEEP) pin, if your board has one wired to
# the Pico. This robot does not use one, so leave it None.
MOTOR_ENABLE_PIN = None

# Servo safe angle limits  (picobot_main.py)
# Base: full 0–180° range (no mechanical obstruction).
# Arm and claw: restricted to 40–140° to avoid hardware damage.
# Home position: 90° for all three (centre of travel).
SERVO_BASE_MIN  =   0
SERVO_BASE_MAX  = 180
SERVO_BASE_HOME =  90

SERVO_ARM_MIN   =  40
SERVO_ARM_MAX   = 140
SERVO_ARM_HOME  =  90

SERVO_CLAW_MIN  =  40
SERVO_CLAW_MAX  = 140
SERVO_CLAW_HOME =  90
