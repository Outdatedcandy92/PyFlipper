import subprocess
import random

def generate_random_mac():
    """Generate a random MAC address."""
    return ":".join(["{:02x}".format(random.randint(0, 255)) for _ in range(6)])

def change_mac(interface, new_mac):
    """Change the MAC address of a given network interface."""
    try:
        # Bring the network interface down
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        
        # Change the MAC address
        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac], check=True)
        
        # Bring the network interface up
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        
        print(f"Successfully changed MAC address of {interface} to {new_mac}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to change MAC address: {e}")

def main():
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    use_random = input("Generate a random MAC address? (yes/no): ").strip().lower()

    if use_random == "yes":
        new_mac = generate_random_mac()
    else:
        new_mac = input("Enter the new MAC address (e.g., 00:11:22:33:44:55): ")

    change_mac(interface, new_mac)

if __name__ == "__main__":
    main()
