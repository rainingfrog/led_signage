import max7219
from machine import Pin, SPI
import time

# Define SPI pins
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))

# Define the number of cascaded MAX7219 devices
num_devices = 4

# Initialize the MAX7219 driver
matrix = max7219.Matrix8x8(spi, Pin(5), num_devices)

# Display scrolling text
def scroll_text(text, size=1, delay=0.1):
    for i in range(len(text) * 8 + 1):
        matrix.fill(0)
        matrix.text(text, -i, 0, size)
        matrix.show()
        time.sleep(delay)
        
def show_text(text, size=1, delay=10):
    matrix.fill(0)
    matrix.text(text, 0, 1, size)
    matrix.show()
    time.sleep(delay)

# Main function
def main():
    try:
        num = 4
        text = input("Enter the text to display: ")
        while num > 0:
            # Display scrolling text
            scroll_text(text)
            num -= 1
        #show_text("4096")
    except Exception as e:
        print("Error:", e)
    finally:
        # Clear the display before exiting
        matrix.fill(0)
        matrix.show()

# Run the main function
if __name__ == "__main__":
    main()
