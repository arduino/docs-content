/**
  Opta device information retrieval 
  Name: opta_info.ino
  Purpose: Retrieve information of an Opta device such as its bootloader version, hardware functionalities, external memory size, and MAC address.

  @author Arduino PRO Content team
  @version 1.0 27/03/22
*/

// Include the necessary header files and define macros
uint8_t* bootloader_data = (uint8_t*)(0x801F000);
uint8_t* bootloader_identification = (uint8_t*)(0x80002F0);

#if __has_include("opta_info.h")
#include "opta_info.h"
#define GET_OPTA_OTP_BOARD_INFO
OptaBoardInfo* info;
OptaBoardInfo* boardInfo();
#endif

void setup() {
  Serial.begin(115200);
  while (!Serial) {}
  delay(2500);

  Serial.println("Opta Device Information");

  uint8_t currentBootloaderVersion = bootloader_data[1];
  String currentBootloaderIdentifier = String(bootloader_identification, 15);

  if (!currentBootloaderIdentifier.equals("MCUboot Arduino")) {
    currentBootloaderIdentifier = "Arduino loader";
  }

  Serial.println("- Bootloader identifier: " + currentBootloaderIdentifier);
  Serial.println("- Magic number (validation): " + String(bootloader_data[0], HEX));
  Serial.println("- Bootloader version: " + String(bootloader_data[1]));

#if defined(GET_OPTA_OTP_BOARD_INFO)
  printOptaSecureInfo();
#endif
}

#if defined(GET_OPTA_OTP_BOARD_INFO)

/**
  Checks if the magic number is 0xB5. If it is, prints the secure information of the device in the Serial Monitor.
  
  @params none
  @return none
*/
void printOptaSecureInfo() {
  info = boardInfo();
  if (info->magic == 0xB5) {
    Serial.println("- Secure information version: " + String(info->version));
    Serial.println("- Ethernet functionality: " + String(info->_board_functionalities.ethernet == 1 ? "Yes" : "No"));
    Serial.println("- Wi-Fi module functionality: " + String(info->_board_functionalities.wifi == 1 ? "Yes" : "No"));
    Serial.println("- RS-485 functionality: " + String(info->_board_functionalities.rs485 == 1 ? "Yes" : "No"));
    Serial.println("- QSPI memory size: " + String(info->external_flash_size) + " MB");
    Serial.println("- Secure board revision: " + String(info->revision >> 8) + "." + String(info->revision & 0xFF));
    Serial.println("- Secure VID: 0x" + String(info->vid, HEX));
    Serial.println("- Secure PID: 0x" + String(info->pid, HEX));
    Serial.println("- Ethernet MAC address: " + String(info->mac_address[0], HEX) + ":" + String(info->mac_address[1], HEX) + ":" + String(info->mac_address[2], HEX) + ":" + String(info->mac_address[3], HEX) + ":" + String(info->mac_address[4], HEX) + ":" + String(info->mac_address[5], HEX));
    if (info->_board_functionalities.wifi == 1) {
      Serial.println("- Wi-Fi MAC address: " + String(info->mac_address_2[0], HEX) + ":" + String(info->mac_address_2[1], HEX) + ":" + String(info->mac_address_2[2], HEX) + ":" + String(info->mac_address_2[3], HEX) + ":" + String(info->mac_address_2[4], HEX) + ":" + String(info->mac_address_2[5], HEX));
    }
  } else {
    Serial.println("- No secure information available!");
    printBootloaderInfo();
  }
}
#endif

/**
  Prints clock source, USB speed, Ethernet functionality, Wi-Fi functionality, RAM memory size, QSPI memory size, video output functionality, and secure element functionality.
  
  @params none
  @return none
*/
void printBootloaderInfo() {
  Serial.println("- Clock source: " + getClockSource(bootloader_data[2]));
  Serial.println("- USB Speed: " + getUSBSpeed(bootloader_data[3]));
  Serial.println("- Ethernet functionality: " + String(bootloader_data[4] == 1 ? "Yes" : "No"));
  Serial.println("- Wi-Fi functionality: " + String(bootloader_data[5] == 1 ? "Yes" : "No"));
  Serial.println("- RAM size: " + getRAMSize(bootloader_data[6]));
  Serial.println("- QSPI memory size: " + String(bootloader_data[7]) + " MB");
  Serial.println("- Video output functionality: " + String(bootloader_data[8] == 1 ? "Yes" : "No"));
  Serial.println("- Secure element functionality: " + String(bootloader_data[9] == 1 ? "Yes" : "No"));
}

/**
  Convert a flag in the bootloader data to USB speed information.
  
  @param bootloader flag (uint8_t)
  @return USB speed information as a String
*/
String getUSBSpeed(uint8_t flag) {
  switch (flag) {
    case 1:
      return "USB 2.0/Hi-Speed (480 Mbps)";
    case 2:
      return "USB 1.1/Full-Speed (12 Mbps)";
    default:
      return "N/A";
  }
}

/**
  Convert a flag in the bootloader data to clock source information.
  
  @param bootloader flag (uint8_t)
  @return clock source information as a String
*/
String getClockSource(uint8_t flag) {
  switch (flag) {
    case 0x8:
      return "External oscillator";
    case 0x4:
      return "External crystal";
    case 0x2:
      return "Internal clock";
    default:
      return "N/A";
  }
}

/**
  Convert a flag in the bootloader data to RAM size information.
  
  @param bootloader flag (uint8_t)
  @return RAM size information as a String
*/
String getRAMSize(uint8_t flag) {
  if (flag == 0) {
    return "N/A";
  }
  return (String(flag) + "MB");
}

void loop() {
  delay(1000);
}