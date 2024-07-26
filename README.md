# KR260-AMD-SoftwareTesting

## Introduction
- The AMD Kria™ KR260 Robotics Starter Kit is the premier platform to evaluate applications targeted to robotics, machine vision, and industrial communications & control. Try all our accelerated applications and get started within minutes by following all the steps.
<br>

![image](https://github.com/user-attachments/assets/c22a1839-2e03-4b40-913e-9bc66f86c29b)

## What’s Inside the Box
- Kria KR260 Robotics Starter Kit (Kria SOM + Carrier Card + Thermal Solution)
- KR260 Power supply and Adapter (12V, 3A)
- MicroSD Card 16 GB or Above
- USB-A to micro-B Cable
- Ethernet Cable
- Getting Started Doc
- Developer Stickers

## What You’ll Need to Provide
You will need to provide the following in order to be able to take full advantage of the fact that KR260 provides a full desktop environment that will be very familiar to developers:

- USB Keyboard
- USB Mouse
- DisplayPort™ Cable (for connecting to a monitor)
- DisplayPort Display
- Use of a USB keyboard and mouse is optional. You can also use a USB camera/webcam or depth sensing camera for your robotics application.
- To begin, a computer with internet connection and with the ability to write to a microSD card is needed.

> [!WARNING]
> ### Important:  Critical Firmware Update Required
> To enable complete board functionality, compatibility with latest Operating Systems, and best performance, be sure to install the latest AMD provided boot firmware following the firmware update instructions available on the [kr260 wiki]([URL](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+K26+SOM)).


## Ubuntu Linux OS
- Ubuntu Linux OS is the best choice for Getting Started with the KR260.

## Ubuntu 22.04 Demos
- Enable a desktop-like experience without the need of connecting to a laptop/PC. 
- Access to rich set of third-party software libraries in the Ubuntu community.
- Run the ROS 2 Perception Node Accelerated App to evaluate KR260 running an Ubuntu application.

<br>

---

## Setting up the SD Card Image

- Step 1. Setting up the SD Card Image (Ubuntu)
The Starter Kit has a primary and secondary boot device, isolating the boot firmware from the run-time OS and application. This allows you to focus on developing and updating your application code within the application image on the secondary boot device, without having to touch the boot firmware. The primary boot device is a QSPI memory located on the SOM, which is pre-programmed (pre-loaded QSPI image) at the factory.  The secondary boot device is a microSD card interface on the carrier card.

> [!NOTE]
> For setting up the microSD card, you’ll need to download the latest SD card image and then write it using an Image Flashing tool.

- Download the Kria KR260 Robotics Starter Kit Image  and save it on your computer.
- Download the Balena Etcher  (recommended; available for Window, Linux, and macOS). Find additional OS specific tool options below.
- Follow the instructions in the tool and select the downloaded image to flash onto your microSD card.

- ![image](https://github.com/user-attachments/assets/73b6f784-b0f4-4e10-8464-092948877080)


> [!IMPORTANT]
> <b>Instructions for Windows</b>

> For Windows users, you can also use the Win32 Disk Imager tool instead of Balena Etcher. Ensure that your SD card is correctly formatted before using the tool.  Also, ensure that the compressed SD card image for Kria KR260 Robotics Starter Kit has been extracted using an archive decompression tool.

> ![image](https://github.com/user-attachments/assets/5360f1dd-cbe7-460f-a911-b4fb6da2f1a2)

- Browse to the location of the uncompressed image in the tool using the Blue folder icon.
- From the device drop-down menu, select the correct microSD card.
- Click on ‘Write’ and then ‘Yes’ at the prompt to continue the write process and wait till the process is completed.



## Connecting Everything

- Step 2. Connecting Everything  (Ubuntu)
- The following are the key connections for the AMD Kria™ KR260 Robotics Starter Kit:
- Insert the microSD card containing the boot image in the microSD card slot (J11) on the Starter Kit.
- Get your USB-A to micro-B cable (a.k.a. micro-USB cable), which supports data transfer.
  
> [!NOTE]
> Do not connect the USB-A end to your computer yet. Connect the micro-B end to J4 on the Starter Kit.

- Connect your USB keyboard/mouse to the USB ports (U44 and U46).
- Connect to a monitor/display with the help of a DisplayPort™ cable.
- Connect the Ethernet cable to one of the PS ETH ports (J10D which is the top right port) for required internet access with factory loaded firmware.
- Grab the Power Supply and connect it to the DC Jack (J12) on the Starter Kit. Do not insert the other end to the AC plug yet.
