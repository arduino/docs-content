#include <BlockDevice.h>
#include <FATFileSystem.h>
#include <LittleFileSystem.h>
#include <MBRBlockDevice.h>

#include "wiced_resource.h"
#include "certificates.h"

#ifndef CORE_CM7  
  #error Update the WiFi firmware by uploading the sketch to the M7 core instead of the M4 core.
#endif

using namespace mbed;

BlockDevice* root;
MBRBlockDevice* wifi_data;
MBRBlockDevice* ota_data;
FATFileSystem wifi_data_fs("wlan");
FATFileSystem ota_data_fs("fs");

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);

    Serial.begin(115200);
    for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500))
        ;

    for (auto i = 0u; i < 10; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(25);
        digitalWrite(LED_BUILTIN, LOW);
        delay(50);
    }

    Serial.println("Erasing the QSPIF");
    // Initialize the block device.
    root = BlockDevice::get_default_instance();
    auto err = root->init();
    if (err != 0) {
        Serial.print("Error Initializing the QSPIF: ");
        Serial.println(err);
        while (true) {
            digitalWrite(LED_BUILTIN, HIGH);
            delay(50);
            digitalWrite(LED_BUILTIN, LOW);
            delay(150);
        }
    }

    // Get device geometry.
    // auto read_size = root->get_read_size();
    // auto program_size = root->get_program_size();
    const auto erase_size = root->get_erase_size();
    const auto size = root->size();
    const auto eraseSectors = size / erase_size;

    for (auto i = 0u; i < eraseSectors; i++) {
        err = root->erase(i * erase_size, erase_size);
        if (i % 64 == 0) {
            digitalWrite(LED_BUILTIN, HIGH);
            delay(25);
            digitalWrite(LED_BUILTIN, LOW);
        }
        if (err != 0) {
            Serial.print("Error erasing sector ");
            Serial.println(i);
            Serial.print(" [");
            Serial.print(i * erase_size);
            Serial.print(" - ");
            Serial.print(float { i } / float { eraseSectors } * 100);
            Serial.print("%] -> ");
            Serial.print(err ? "KO" : "OK");
            Serial.println();            
            for (auto i = 0u; i < 2; i++) {
                digitalWrite(LED_BUILTIN, HIGH);
                delay(50);
                digitalWrite(LED_BUILTIN, LOW);
                delay(150);
            }
        }
    }
    Serial.println("Done");

    for (auto i = 0u; i < 5; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(25);
        digitalWrite(LED_BUILTIN, LOW);
        delay(50);
    }

    // Create the partitions on the MBR
    // WiFi Firmware and TLS TA certificates: 1MB
    // Arduino OTA: 13MB
    MBRBlockDevice::partition(root, 1, 0x0B, 0 * 1024 * 1024, 1 * 1024 * 1024);
    MBRBlockDevice::partition(root, 3, 0x0B, 14 * 1024 * 1024, 14 * 1024 * 1024);
    MBRBlockDevice::partition(root, 2, 0x0B, 1024 * 1024, 14 * 1024 * 1024);

    // Create the FS references
    wifi_data = new MBRBlockDevice(root, 1);
    ota_data = new MBRBlockDevice(root, 2);

    // Format the partitions
    Serial.print("Formatting WiFi partition... ");
    err = wifi_data_fs.reformat(wifi_data);
    if (err != 0) {
        Serial.println("Error formatting WiFi partition");
        while (true) {
            digitalWrite(LED_BUILTIN, HIGH);
            delay(50);
            digitalWrite(LED_BUILTIN, LOW);
            delay(150);
        }
    }
    Serial.println("done.");

    Serial.print("Formatting OTA partition...");
    err = ota_data_fs.reformat(ota_data);
    if (err != 0) {
        Serial.println("Error formatting OTA partition");
        while (true) {
            digitalWrite(LED_BUILTIN, HIGH);
            delay(50);
            digitalWrite(LED_BUILTIN, LOW);
            delay(150);
        }
    }
    Serial.println("done.");

    for (auto i = 0u; i < 10; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(25);
        digitalWrite(LED_BUILTIN, LOW);
        delay(50);
    }

    Serial.println("QSPI Flash Storage Ready.");

    extern const unsigned char wifi_firmware_image_data[];
    extern const resource_hnd_t wifi_firmware_image;
    FILE* fp = fopen("/wlan/4343WA1.BIN", "wb");
    const int file_size = 421098;
    int chunck_size = 1024;
    int byte_count = 0;

    Serial.println("Flashing /wlan/4343WA1.BIN file");
    printProgress(byte_count, file_size, 10, true);
    while (byte_count < file_size) {
        if (byte_count + chunck_size > file_size)
            chunck_size = file_size - byte_count;
        int ret = fwrite(&wifi_firmware_image_data[byte_count], chunck_size, 1, fp);
        if (ret != 1) {
            Serial.println("Error writing firmware data");
            break;
        }
        byte_count += chunck_size;
        printProgress(byte_count, file_size, 10, false);
    }
    fclose(fp);

    chunck_size = 1024;
    byte_count = 0;
    const uint32_t offset = 15 * 1024 * 1024 + 1024 * 512;

    Serial.println("Flashing memory mapped firmware");
    printProgress(byte_count, file_size, 10, true);
    while (byte_count < file_size) {
        if (byte_count + chunck_size > file_size)
            chunck_size = file_size - byte_count;
        int ret = root->program(wifi_firmware_image_data, offset + byte_count, chunck_size);
        if (ret != 0) {
            Serial.println("Error writing firmware data");
            break;
        }
        byte_count += chunck_size;
        printProgress(byte_count, file_size, 10, false);
    }

    chunck_size = 128;
    byte_count = 0;
    fp = fopen("/wlan/cacert.pem", "wb");

    Serial.println("Flashing certificates");
    printProgress(byte_count, cacert_pem_len, 10, true);
    while (byte_count < cacert_pem_len) {
        if (byte_count + chunck_size > cacert_pem_len)
            chunck_size = cacert_pem_len - byte_count;
        int ret = fwrite(&cacert_pem[byte_count], chunck_size, 1, fp);
        if (ret != 1) {
            Serial.println("Error writing certificates");
            break;
        }
        byte_count += chunck_size;
        printProgress(byte_count, cacert_pem_len, 10, false);
    }
    fclose(fp);

    fp = fopen("/wlan/cacert.pem", "rb");
    char buffer[128];
    int ret = fread(buffer, 1, 128, fp);
    Serial.write(buffer, ret);
    while (ret == 128) {
        ret = fread(buffer, 1, 128, fp);
        Serial.write(buffer, ret);
    }
    fclose(fp);

    Serial.println("\nFirmware and certificates updated!");
    Serial.println("It's now safe to reboot or disconnect your board.");
}

void loop()
{
}

long getFileSize(FILE* fp)
{
    fseek(fp, 0, SEEK_END);
    int size = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    return size;
}

void printProgress(uint32_t offset, uint32_t size, uint32_t threshold, bool reset)
{
    static int percent_done = 0;
    if (reset == true) {
        percent_done = 0;
        Serial.println("Flashed " + String(percent_done) + "%");
    } else {
        uint32_t percent_done_new = offset * 100 / size;
        if (percent_done_new >= percent_done + threshold) {
            percent_done = percent_done_new;
            Serial.println("Flashed " + String(percent_done) + "%");
        }
    }
}
