import bluetooth

def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    try:
        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=True)
        if not nearby_devices:
            print("No devices found.")
            return

        print(f"\n{'Name':<30} {'MAC Address':<20} {'Device Class':<10}")
        print("-" * 60)
        for addr, name, device_class in nearby_devices:
            print(f"{name:<30} {addr:<20} {device_class:<10}")
    except bluetooth.BluetoothError as e:
        print(f"An error occurred while scanning: {e}")

if __name__ == "__main__":
    scan_bluetooth_devices()
