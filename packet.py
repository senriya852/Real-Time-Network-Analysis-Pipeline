# -*- coding: utf-8 -*-
"""packets.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IIikMRqkkDBoYwmozUx2OSGe2_jPr8qc
"""

from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

sniff(prn=packet_callback, count=1000)  # Sniff 1000 packets

from scapy.all import sniff, wrpcap

# Define a callback function to process each captured packet
def packet_callback(packet):
    # Append the packet to the list
    packets.append(packet)

# Initialize an empty list to store captured packets
packets = []

# Sniff packets with the callback function applied
sniff(prn=packet_callback, count=100)  # Capture 100 packets

# Write the captured packets to a pcapng file
wrpcap("captured_packets.pcapng", packets)

print("Packets captured and saved to captured_packets.pcapng")

import os

# Get the current working directory
current_directory = os.getcwd()

# Print the location of the pcapng file
print("Location of pcapng file:", os.path.join(current_directory, "captured_packets.pcapng"))
