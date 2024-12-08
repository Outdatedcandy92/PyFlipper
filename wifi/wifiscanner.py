import subprocess
import re
import sys

def set_monitor_mode(interface):
    """Enable monitor mode on the specified wireless interface."""
    try:
        print(f"Setting {interface} to monitor mode...")
        subprocess.run(['sudo', 'airmon-ng', 'start', interface], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to set monitor mode: {e}")
        sys.exit(1)

def set_managed_mode(interface):
    """Disable monitor mode and revert to managed mode."""
    try:
        print(f"Reverting {interface} to managed mode...")
        subprocess.run(['sudo', 'airmon-ng', 'stop', f"{interface}mon"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to revert to managed mode: {e}")
        sys.exit(1)

def scan_wifi():
    """Scan for Wi-Fi networks."""
    try:
        # Use `iwlist` to scan for networks
        result = subprocess.run(['sudo', 'iwlist', 'wlan0mon', 'scan'], stdout=subprocess.PIPE, text=True)
        output = result.stdout

        networks = []
        # Parse the output to extract network details
        for block in output.split("Cell"):
            ssid_match = re.search(r'ESSID:"(.+?)"', block)
            freq_match = re.search(r"Frequency:(\d+\.\d+) GHz", block)
            signal_match = re.search(r"Signal level=(-\d+)", block)
            enc_match = re.search(r"Encryption key:(\w+)", block)

            if ssid_match:
                ssid = ssid_match.group(1)
                frequency = freq_match.group(1) if freq_match else "Unknown"
                signal = signal_match.group(1) if signal_match else "Unknown"
                encryption = "Enabled" if enc_match and enc_match.group(1) == "on" else "Open"
                networks.append({
                    "SSID": ssid,
                    "Frequency (GHz)": frequency,
                    "Signal Strength (dBm)": signal,
                    "Encryption": encryption
                })

        if networks:
            print(f"{'SSID':<30}{'Frequency (GHz)':<20}{'Signal Strength (dBm)':<25}{'Encryption':<15}")
            print("=" * 90)
            for net in networks:
                print(f"{net['SSID']:<30}{net['Frequency (GHz)']:<20}{net['Signal Strength (dBm)']:<25}{net['Encryption']:<15}")
        else:
            print("No Wi-Fi networks found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'wlan0' with your wireless interface name
    wireless_interface = "wlan0"

    try:
        set_monitor_mode(wireless_interface)
        scan_wifi()
    finally:
        set_managed_mode(wireless_interface)
