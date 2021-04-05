import board
import digitalio
import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_debouncer import Debouncer

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

pins = [
	  board.GP16, board.GP17, board.GP18, board.GP19,
	  board.GP20, board.GP21, board.GP22, board.GP26
	]

buttons = []

for pin in pins:
	button_pin = digitalio.DigitalInOut(pin)
	button_pin.direction = digitalio.Direction.INPUT
	button_pin.pull = digitalio.Pull.DOWN
	buttons.append(Debouncer(button_pin))
 
while True:
	for button in buttons:
		button.update()
		if button.rose:
			midi.send(ControlChange(buttons.index(button), 127))
