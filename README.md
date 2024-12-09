# Project Documentation

## AppleJuice

### app.py
This script is used to send various Apple BLE proximity pairing notifications. It allows you to select different messages to send to nearby Apple devices. You can learn about Bluetooth Low Energy (BLE) and how to interact with Apple devices using BLE.

**Key Concepts:**
- **Bluetooth Low Energy (BLE):** A wireless personal area network technology designed for novel applications in healthcare, fitness, beacons, security, and home entertainment.
- **Proximity Pairing Notifications:** Messages that appear on Apple devices when they detect nearby Apple accessories.

**Code Breakdown:**
- **Argument Parsing:** The script uses `argparse` to handle command-line arguments, allowing users to specify options like advertising interval and random charge values.
- **BLE Advertising:** Functions like `start_le_advertising` and `stop_le_advertising` are used to control BLE advertising, sending custom data packets to nearby devices.
- **Randomization:** The script can send random charge values to simulate different battery levels of Apple devices.

## bluetooth

#### bltscan.py
This script scans for nearby Bluetooth devices and displays their information. You can learn about Bluetooth scanning and how to discover nearby devices using Python.

**Key Concepts:**
- **Bluetooth Scanning:** The process of discovering nearby Bluetooth devices by sending inquiry requests and listening for responses.
- **Device Discovery:** Identifying and listing nearby Bluetooth devices along with their names, MAC addresses, and device classes.

**Code Breakdown:**
- **Bluetooth Library:** The script uses the `bluetooth` library to perform device discovery.
- **Device Information:** The script retrieves and displays the name, MAC address, and device class of each discovered device.

#### bltsniffer.py
This script sets up a Bluetooth sniffer to capture Bluetooth packets. You can learn about Bluetooth packet sniffing and how to capture and analyze Bluetooth traffic.

**Key Concepts:**
- **Bluetooth Sniffing:** Capturing and analyzing Bluetooth packets to understand the communication between devices.
- **Packet Analysis:** Examining the contents of captured Bluetooth packets to extract useful information.

**Code Breakdown:**
- **Packet Capture:** The script uses a Bluetooth sniffer to capture packets in real-time.
- **Data Parsing:** The captured packets are parsed to extract relevant information, such as device addresses and packet types.

## cc1101

#### config.py
This script contains configuration settings for the CC1101 module. You can learn about configuring the CC1101 module for different communication settings.

**Key Concepts:**
- **CC1101 Module:** A low-cost sub-1 GHz transceiver designed for very low-power wireless applications.
- **Configuration Settings:** Parameters that control the behavior of the CC1101 module, such as frequency, data rate, and modulation.

**Code Breakdown:**
- **Configuration Parameters:** The script defines various configuration parameters for the CC1101 module.
- **Initialization:** The script initializes the CC1101 module with the specified configuration settings.

#### transmit.py
This script demonstrates how to transmit data using the CC1101 module. You can learn about using the CC1101 module for wireless communication and how to send data using Python.

**Key Concepts:**
- **Wireless Communication:** Transmitting data wirelessly using the CC1101 module.
- **Data Transmission:** Sending data packets over the air to a receiver.

**Code Breakdown:**
- **Data Preparation:** The script prepares the data to be transmitted.
- **Transmission:** The script uses the CC1101 module to transmit the prepared data packets.

## IR

#### ir_reciver.py
This script demonstrates how to receive infrared (IR) signals using an IR receiver module. You can learn about receiving and decoding IR signals using Python.

**Key Concepts:**
- **Infrared Signals:** Electromagnetic waves with wavelengths longer than visible light, commonly used for remote controls.
- **Signal Reception:** Capturing and decoding IR signals to extract information.

**Code Breakdown:**
- **IR Receiver Module:** The script interfaces with an IR receiver module to capture incoming IR signals.
- **Signal Decoding:** The captured signals are decoded to retrieve the transmitted information.

#### ir_sender.py
This script demonstrates how to send infrared (IR) signals using an IR transmitter module. You can learn about sending IR signals and how to control IR devices using Python.

**Key Concepts:**
- **Infrared Transmission:** Sending IR signals to control devices like TVs and air conditioners.
- **Signal Encoding:** Encoding information into IR signals for transmission.

**Code Breakdown:**
- **IR Transmitter Module:** The script interfaces with an IR transmitter module to send IR signals.
- **Signal Encoding:** The script encodes the information to be transmitted into IR signals.

## pn532

#### androidhce.py
This script demonstrates how to use the PN532 module for Android Host Card Emulation (HCE). You can learn about using the PN532 module for NFC communication and how to emulate NFC cards.

**Key Concepts:**
- **NFC (Near Field Communication):** A set of communication protocols that enable two electronic devices to communicate when they are within 4 cm of each other.
- **Host Card Emulation (HCE):** A technology that allows a device to emulate a contactless smart card.

**Code Breakdown:**
- **PN532 Module:** The script interfaces with the PN532 module to perform NFC communication.
- **HCE Setup:** The script sets up the PN532 module for HCE and handles communication with NFC readers.

#### formatndef.py
This script demonstrates how to format NFC tags using the PN532 module. You can learn about formatting NFC tags and how to write NDEF records using Python.

**Key Concepts:**
- **NFC Tags:** Small, passive devices that store data and can be read by NFC-enabled devices.
- **NDEF (NFC Data Exchange Format):** A standardized data format for storing and exchanging information on NFC tags.

**Code Breakdown:**
- **Tag Formatting:** The script formats NFC tags to prepare them for storing NDEF records.
- **NDEF Writing:** The script writes NDEF records to the formatted NFC tags.

#### MemDump.py
This script demonstrates how to dump the memory of NFC tags using the PN532 module. You can learn about reading and analyzing the memory contents of NFC tags.

**Key Concepts:**
- **Memory Dumping:** Reading the entire memory contents of an NFC tag.
- **Data Analysis:** Analyzing the dumped memory to extract useful information.

**Code Breakdown:**
- **Memory Reading:** The script reads the memory contents of NFC tags using the PN532 module.
- **Data Analysis:** The script analyzes the dumped memory to extract and display the stored information.

#### ndeftoclasssic.py
This script demonstrates how to convert NDEF records to classic format using the PN532 module. You can learn about converting and writing different types of NFC records.

**Key Concepts:**
- **NDEF Conversion:** Converting NDEF records to a different format for compatibility with various NFC devices.
- **Data Writing:** Writing the converted records to NFC tags.

**Code Breakdown:**
- **Record Conversion:** The script converts NDEF records to a classic format.
- **Data Writing:** The script writes the converted records to NFC tags using the PN532 module.

#### p2praw.py
This script demonstrates how to use the PN532 module for peer-to-peer (P2P) communication. You can learn about setting up P2P communication and exchanging data using NFC.

**Key Concepts:**
- **Peer-to-Peer Communication:** Direct communication between two NFC-enabled devices.
- **Data Exchange:** Exchanging data between devices using NFC.

**Code Breakdown:**
- **P2P Setup:** The script sets up the PN532 module for P2P communication.
- **Data Exchange:** The script handles the exchange of data between NFC devices.

#### readmifare.py
This script demonstrates how to read MIFARE cards using the PN532 module. You can learn about reading and authenticating MIFARE cards using Python.

**Key Concepts:**
- **MIFARE Cards:** A family of contactless smart cards used for various applications, including access control and public transportation.
- **Card Reading:** Reading data from MIFARE cards using an NFC reader.

**Code Breakdown:**
- **Card Authentication:** The script authenticates MIFARE cards before reading their data.
- **Data Reading:** The script reads data from authenticated MIFARE cards using the PN532 module.

#### uid.py
This script demonstrates how to read the UID of NFC tags using the PN532 module. You can learn about reading unique identifiers (UIDs) of NFC tags.

**Key Concepts:**
- **UID (Unique Identifier):** A unique number assigned to each NFC tag, used for identification purposes.
- **Tag Reading:** Reading the UID of NFC tags using an NFC reader.

**Code Breakdown:**
- **UID Reading:** The script reads the UID of NFC tags using the PN532 module.
- **Data Display:** The script displays the read UID to the user.

#### updatendef.py
This script demonstrates how to update NDEF records on NFC tags using the PN532 module. You can learn about updating and modifying NDEF records on NFC tags.

**Key Concepts:**
- **NDEF Updating:** Modifying existing NDEF records on NFC tags.
- **Data Writing:** Writing updated NDEF records to NFC tags.

**Code Breakdown:**
- **Record Updating:** The script updates existing NDEF records on NFC tags.
- **Data Writing:** The script writes the updated records to NFC tags using the PN532 module.

## wifi

#### deauth.py
This script demonstrates how to perform a deauthentication attack on Wi-Fi networks. You can learn about Wi-Fi security and how deauthentication attacks work.

**Key Concepts:**
- **Deauthentication Attack:** A type of denial-of-service attack that disconnects devices from a Wi-Fi network by sending deauthentication frames.
- **Wi-Fi Security:** Understanding the vulnerabilities and security measures of Wi-Fi networks.

**Code Breakdown:**
- **Packet Injection:** The script injects deauthentication frames into the Wi-Fi network to disconnect devices.
- **Network Monitoring:** The script monitors the network to identify and target devices for deauthentication.

#### macaddr.py
This script demonstrates how to change the MAC address of your Wi-Fi adapter. You can learn about MAC address spoofing and how to change your MAC address using Python.

**Key Concepts:**
- **MAC Address:** A unique identifier assigned to network interfaces for communication on a network.
- **MAC Spoofing:** Changing the MAC address of a network interface to disguise its identity.

**Code Breakdown:**
- **Address Generation:** The script generates a new MAC address, either randomly or based on user input.
- **Address Assignment:** The script assigns the new MAC address to the Wi-Fi adapter.

#### wifiscanner.py
This script scans for nearby Wi-Fi networks and displays their information. You can learn about Wi-Fi scanning and how to discover nearby networks using Python.

**Key Concepts:**
- **Wi-Fi Scanning:** The process of discovering nearby Wi-Fi networks by sending probe requests and listening for responses.
- **Network Discovery:** Identifying and listing nearby Wi-Fi networks along with their SSIDs, signal strengths, and security types.

**Code Breakdown:**
- **Network Discovery:** The script uses a Wi-Fi adapter to scan for nearby networks.
- **Data Display:** The script retrieves and displays the SSID, signal strength, and security type of each discovered network.