import os
import subprocess

def setup_bluetooth_monitor_mode():
    """
    Configures the Bluetooth device into monitor mode.
    """
    print("Configuring Bluetooth device into monitor mode...")
    try:
        # Bring up the Bluetooth device
        subprocess.run(['hciconfig', 'hci0', 'down'], check=True)
        subprocess.run(['hciconfig', 'hci0', 'up'], check=True)
        
        # Enable scanning
        subprocess.run(['hciconfig', 'hci0', 'piscan'], check=True)
        
        print("Bluetooth device is now in monitor mode.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to configure Bluetooth device: {e}")
        exit(1)

def start_sniffer():
    """
    Starts the Bluetooth sniffer using hcitool and hcidump.
    """
    print("Starting Bluetooth sniffer...")
    try:
        # Launch hcitool to start scanning for devices
        print("Starting scan with hcitool...")
        scan_process = subprocess.Popen(['hcitool', 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Launch hcidump to capture HCI events
        print("Starting hcidump to capture HCI packets...")
        dump_process = subprocess.Popen(['hcidump', '-X'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Monitor and process output
        print("\nListening for Bluetooth HCI events. Press Ctrl+C to stop.\n")
        while True:
            output = dump_process.stdout.readline().decode('utf-8').strip()
            if output:
                print(output)

    except KeyboardInterrupt:
        print("\nStopping sniffer...")
    finally:
        # Terminate processes gracefully
        scan_process.terminate()
        dump_process.terminate()
        print("Sniffer stopped.")

if __name__ == "__main__":
    # Ensure script is run as root
    if os.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
    else:
        setup_bluetooth_monitor_mode()
        start_sniffer()
