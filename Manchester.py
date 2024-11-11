
import numpy as np
import matplotlib.pyplot as plt

dataToEncode = "10110"
outputSignal = ""
lastValue = "none"
dataprint = ""


BinaryToEncode=input("Enter the binary data to encode: ")
dataToEncode=BinaryToEncode

# Constructing the ASCII sequence for textual visualization
for i in dataToEncode:
    dataprint += " " + i + "| "

# Initializing a list to store signal values for plotting
signal_values = []

# Loop to encode each bit in Manchester according to the specified convention
for i in range(len(dataToEncode)):
    current_bit = dataToEncode[i]

    # If the bit is 1, add "10" (high-to-low transition in Manchester)
    if current_bit == "1":
        outputSignal += "|10|"
        signal_values.extend([1, 0])  # High-to-low transition for 1

    # If the bit is 0, add "01" (low-to-high transition in Manchester)
    else:
        outputSignal += "|01|"
        signal_values.extend([0, 1])  # Low-to-high transition for 0


# Display the ASCII signal
print("Signal Manchester ASCII:", outputSignal)
print("Data bits:", dataprint)

# Plotting the Manchester signal
plt.figure(figsize=(12, 4))
plt.step(
    np.arange(len(signal_values)), signal_values, where="post", color="b", linewidth=2
)
plt.ylim(-0.25, 1.25)
plt.xlim(0, len(signal_values))
plt.title("Manchester Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()
