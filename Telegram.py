import time
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop

LED_PIN = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, 0)

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if 'on' in command:
        GPIO.output(LED_PIN, 1)
        bot.sendMessage(chat_id, "LED turned ON")

    elif 'off' in command:
        GPIO.output(LED_PIN, 0)
        bot.sendMessage(chat_id, "LED turned OFF")

    else:
        bot.sendMessage(chat_id, "Send 'on' or 'off'")

bot = telepot.Bot('BOT_TOKEN')

MessageLoop(bot, action).run_as_thread()

print("Listening for commands...")

while True:
    time.sleep(10)