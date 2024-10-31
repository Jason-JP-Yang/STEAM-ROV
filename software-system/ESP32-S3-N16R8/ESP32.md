# ROV Project - ESP32-S3-N16R8
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/all.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/fontawesome.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/brands.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/solid.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/regular.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/thin.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/light.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/duotone.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/sharp-solid.min.css">

> Hong Kong Po Leung Kuk Ngan Po Ling College Steam Team Robotics ROV Team 2 </br>
> Teammates: JP-YANG, Jasmine, Walter, Mark Chan, Kasey Chan
<div align="right">
<a title="zh-CN" href="./ESP32.md"><img src="https://img.shields.io/badge/-English-A31F34?style=for-the-badge" alt="English" /></a>
<a title="zh-CN" href="./ESP32_zh-CN.md"><img src="https://img.shields.io/badge/-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-545759?style=for-the-badge" alt="简体中文"></a>
<a title="zh-TW" href="./ESP32_zh-TW.md"><img src="https://img.shields.io/badge/-%E7%B9%81%E4%BD%93%E4%B8%AD%E6%96%87-545759?style=for-the-badge" alt="繁体中文"></a>
</div>  

![](/markdown-resource/esp32-c-ROV.png)
## Hardware Introduction
*According to official document, this part won't provide english and zh-TW version*
![](/additional-resource/YD-ESP32-S3_materials/YD-ESP32-S3-Hardware%20info/hardware_img.PNG)

| 主要组件                                 | 介绍                                                         |
| :--------------------------------------- | ------------------------------------------------------------ |
| ESP32-S3-WROOM-1                         | ESP32-S3-WROOM-1 是通用型 Wi-Fi + 低功耗蓝牙 MCU 模组，具有丰富的外设接口、强大的神经网络运算能力和信号处理能力，专为人工智能和 AIoT 市场打造。ESP32-S3-WROOM-1  采用 PCB 板载天线。 |
| 5 V to 3.3 V LDO（5 V 转 3.3 V LDO）     | 电源转换器，输入 5 V，输出 3.3 V,电流为1A                    |
| Pin Headers（排针）                      | 所有可用 GPIO 管脚（除 flash 的 SPI 总线）均已引出至开发板的排针。 |
| USB-to-UART Port（USB 转 UART 接口）     | Type-c-USB 接口，可用作开发板的供电接口，可烧录固件至芯片，也可作为通信接口，通过板载 USB 转 UART 桥接器与芯片通信。 |
| Boot Button（Boot 键）                   | 下载按键。按住 **Boot** 键的同时按一下 **Reset** 键进入“固件下载”模式，通过串口下载固件。如果启动完毕可以当做普通的输入按键使用，使用到的IO为GPIO0。 |
| Reset Button（Reset 键）                 | 复位按键。                                                   |
| USB Port（USB 接口）                     | ESP32-S3 USB OTG 接口，支持全速 USB 1.1 标准。ESP32-S3 USB 接口可用作开发板的供电接口，可烧录固件至芯片，可通过 USB 协议与芯片通信，也可用于 JTAG 调试。 |
| USB-to-UART Bridge（USB 转 UART 桥接器） | 芯片为CH343P,厂商为沁恒，网址为http://www.wch-ic.com/ 驱动：http://www.wch-ic.com/products/CH343.html? |
| RGB LED                                  | 可寻址 RGB 发光二极管，由 GPIO48 驱动。型号为WS2812。        |
| PWR LED                                  | 电源指示灯，板子供电后，亮起，不可以程序控制。               |
| TX LED                                   | ESP32-S3的串口TXD线路上的led,当有串口数据发出时，LED闪烁，如果不使用串口功能可以当做GPIO使用,GPIO43 |
| RX LED                                   | ESP32-S3的串口RXD线路上的led,当有串口数据接收时，LED闪烁，如果不使用串口功能可以当做GPIO使用，GPIO44 |
### Remarks of hardware
在板载 ESP32-S3-WROOM-1 模组系列（使用 8 线 SPI flash/PSRAM）的开发板，管脚 GPIO35、GPIO36 和 GPIO37 已用于内部 ESP32-S3 芯片与 SPI flash/PSRAM 之间的通信，外部不可使用。
### Power Supply
您可从以下三种供电方式中任选其一给开发板供电：

- USB 转 UART 接口供电或 ESP32-S3 USB 接口供电（选择其一或同时供电）**- 默认供电方式（推荐）**
- 5V 和 G (GND) 排针供电
- 3V3 和 G (GND) 排针供电
## PinOUT Diagram
*According to official document, this part won't provide english and zh_TW version*
![](/additional-resource/YD-ESP32-S3_materials/YD-ESP32-S3-Hardware%20info/pinInOut.jpg)

- P：电源；I：输入；O：输出；T：可设置为高阻。
#### P1 SIDE

| 序号 | 名称 | 类型  | 功能                                                         |
| ---- | ---- | ----- | ------------------------------------------------------------ |
| 1    | 3V3  | P     | 3.3 V 电源                                                   |
| 2    | 3V3  | P     | 3.3 V 电源                                                   |
| 3    | RST  | I     | EN                                                           |
| 4    | 4    | I/O/T | RTC_GPIO4, GPIO4, TOUCH4, ADC1_CH3                           |
| 5    | 5    | I/O/T | RTC_GPIO5, GPIO5, TOUCH5, ADC1_CH4                           |
| 6    | 6    | I/O/T | RTC_GPIO6, GPIO6, TOUCH6, ADC1_CH5                           |
| 7    | 7    | I/O/T | RTC_GPIO7, GPIO7, TOUCH7, ADC1_CH6                           |
| 8    | 15   | I/O/T | RTC_GPIO15, GPIO15, U0RTS, ADC2_CH4, XTAL_32K_P              |
| 9    | 16   | I/O/T | RTC_GPIO16, GPIO16, U0CTS, ADC2_CH5, XTAL_32K_N              |
| 10   | 17   | I/O/T | RTC_GPIO17, GPIO17, U1TXD, ADC2_CH6                          |
| 11   | 18   | I/O/T | RTC_GPIO18, GPIO18, U1RXD, ADC2_CH7, CLK_OUT3                |
| 12   | 8    | I/O/T | RTC_GPIO8, GPIO8, TOUCH8, ADC1_CH7, SUBSPICS1                |
| 13   | 3    | I/O/T | RTC_GPIO3, GPIO3, TOUCH3, ADC1_CH2                           |
| 14   | 46   | I/O/T | GPIO46                                                       |
| 15   | 9    | I/O/T | RTC_GPIO9, GPIO9, TOUCH9, ADC1_CH8, FSPIHD, SUBSPIHD         |
| 16   | 10   | I/O/T | RTC_GPIO10, GPIO10, TOUCH10, ADC1_CH9, FSPICS0, FSPIIO4, SUBSPICS0 |
| 17   | 11   | I/O/T | RTC_GPIO11, GPIO11, TOUCH11, ADC2_CH0, FSPID, FSPIIO5, SUBSPID |
| 18   | 12   | I/O/T | RTC_GPIO12, GPIO12, TOUCH12, ADC2_CH1, FSPICLK, FSPIIO6, SUBSPICLK |
| 19   | 13   | I/O/T | RTC_GPIO13, GPIO13, TOUCH13, ADC2_CH2, FSPIQ, FSPIIO7, SUBSPIQ |
| 20   | 14   | I/O/T | RTC_GPIO14, GPIO14, TOUCH14, ADC2_CH3, FSPIWP, FSPIDQS, SUBSPIWP |
| 21   | 5V   | P     | 5 V 电源                                                     |
| 22   | G    | G     | 接地                                                         |

#### P2 SIDE

| 序号 | 名称 | 类型  | 功能                                                  |
| ---- | ---- | ----- | ----------------------------------------------------- |
| 1    | G    | G     | 接地                                                  |
| 2    | TX   | I/O/T | U0TXD, GPIO43, CLK_OUT1                               |
| 3    | RX   | I/O/T | U0RXD, GPIO44, CLK_OUT2                               |
| 4    | 1    | I/O/T | RTC_GPIO1, GPIO1, TOUCH1, ADC1_CH0                    |
| 5    | 2    | I/O/T | RTC_GPIO2, GPIO2, TOUCH2, ADC1_CH1                    |
| 6    | 42   | I/O/T | MTMS, GPIO42                                          |
| 7    | 41   | I/O/T | MTDI, GPIO41, CLK_OUT1                                |
| 8    | 40   | I/O/T | MTDO, GPIO40, CLK_OUT2                                |
| 9    | 39   | I/O/T | MTCK, GPIO39, CLK_OUT3, SUBSPICS1                     |
| 10   | 38   | I/O/T | GPIO38, FSPIWP, SUBSPIWP                              |
| 11   | 37   | I/O/T | SPIDQS, GPIO37, FSPIQ, SUBSPIQ                        |
| 12   | 36   | I/O/T | SPIIO7, GPIO36, FSPICLK, SUBSPICLK                    |
| 13   | 35   | I/O/T | SPIIO6, GPIO35, FSPID, SUBSPID                        |
| 14   | 0    | I/O/T | RTC_GPIO0, GPIO0                                      |
| 15   | 45   | I/O/T | GPIO45                                                |
| 16   | 48   | I/O/T | GPIO48, SPICLK_N, SUBSPICLK_N_DIFF, RGB LED           |
| 17   | 47   | I/O/T | GPIO47, SPICLK_P, SUBSPICLK_P_DIFF                    |
| 18   | 21   | I/O/T | RTC_GPIO21, GPIO21                                    |
| 19   | 20   | I/O/T | RTC_GPIO20, GPIO20, U1CTS, ADC2_CH9, CLK_OUT1, USB_D+ |
| 20   | 19   | I/O/T | RTC_GPIO19, GPIO19, U1RTS, ADC2_CH8, CLK_OUT2, USB_D- |
| 21   | G    | G     | 接地                                                  |
| 22   | G    | G     | 接地                                                  |

## Device Usage
Micropython will be the programming languages use for the MCU ESP32 S3 N16R8. The stable version of Micropython 1.19 will be used in the project. </br>
Visual Studio Code will be the software to develop program on ESP32 using Micropython.

There is few steps need to follow to start the use of Micropython.
1. Create a python environment (not suggested using base environment avoid packages conflicts)
2. Install plugin of RT-Thread Micropython and Python on VS-Code
3. Write the micropython firmware into the ESP32 board
4. Restart and reconnect the board, finally check status ensure everything work correctly.
### 1. Create a python environment for Micropython
There are so many ways that you can create a individual python environment for Micropython. Suggest use AnaConda. </br>
You can click the link below to install AnaConda on your computer https://www.anaconda.com/download</br>
Press Ctrl+Shift+P in VsCode and find option of "Python: Select Interpreter" to select the correct python environment

---
***Introduction and usage of anaconda*** </br>
It is a distribution where packages can be easily obtained and managed, and the environment can be managed in a unified way. Anaconda contains more than 180 science packages and their dependencies, including conda and Python. That is, it can create multiple python environments you want on your computer, and install different packages for each python environment, and switch between different environments, easy to operate and easy to use!
1. Open the downloaded Anaconda.exe enter the install program
2. Click next until the page of advanced options
3. Select add conda to 'PATH'
4. Click next until the installation is successful. If you face problems, seek help on anaconda community.
5. If you mainly use the software in mainland, you should add extra download source to global config.
``` command
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/$ anaconda/pkgs/free/
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/$ anaconda/pkgs/main/
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/$ anaconda/cloud//pytorch/
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/$ anaconda/cloud/conda-forge/
$ conda config --set show_channel_urls yes
```
6. Create a python environment and manage basic packages
``` command
$ conda create -n Micropython python=3.12
$ conda env list
$ conda activate Micropython
```
If you want more information about using anaconda, visit following link: https://docs.anaconda.com/anaconda/getting-started/
### 2. Install plugin of RT-Thread Micropython and Python on VS-Code
Search the pulgin of RT-Thread Micropython and Python on VS-Code and install them. You may be required to restart the software to make plugin active. 

***Usage of RT-Thread Micropython*** </br>
*According to official document, this part won't provide english and zh-TW version* 

你的开发板必须能访问串口，这需要组策略的允许。你可能需要将自己的账户加入该组，通常在默认情况下你的账户可能并不在该组。首先，确认你的账户不在 “dialout” 组.</br>
MicroPython 开发的第一步是创建 MicroPython 工程用来编写和运行代码。使用 MicroPython 插件创建工程的方法是，点击左下方的 “Create MicroPython project” 按钮。</br>
点击 VSCodium 左下方的 “Connection” 按钮，进行 VSCodium 与开发板的连接，在弹出的列表中，选择要连接的物理设备。

在 VSCodium 中可以通过在开发板上运行单个程序文件，很方便快捷的进行程序调试。快捷键 Alt+Q 会触发一个特定的插件，该插件会将当前的 Python 文件上传到开发板内存中。你还可以在当前 Python 文档界面点击右键，然后选择 “Run the MicroPython file directly on the device” 实现同样的功能。</br>
如果你需要以不上传代码的方式检查一组代码，可以使用“代码片段”功能。要运行 MicroPython REPL 环境中的代码片段，在编辑器中选中要运行的片段，右键菜单中点击 “Execute the selected MicroPython code on the device” 


点击左下角“同步”按钮可以启动工程同步，该操作将把本地工程中所有的文件和目录同步到开发板的文件系统。建议在完成程序调试之后进行该操作，调试过程中不需要频繁进行同步操作。工程的同步操作完成后，开发板上的文件列表可以在 “Device Files List” 列看到。

在 REPL 环境中运行 os.listdir() 命令，可以检查文件和目录是否成功加载。当然，也可以通过相应的命令删除 REPL 中的文件或目录。</br>
删除文件的命令如下：`os.remove('file_to_delete')`</br>
删除目录的命令如下：`os.rmdir('folder_to_delete')`
### 3. Write the micropython firmware into the ESP32 board
**First of all, you need to install CH343P drive computer to connect through UART**. </br>
Click the link to redirect to the folder: [USB to serial CH343 drive /additional-resource/YD-ESP32-S3_materials/USB to serial CH343 driver/](/additional-resource/YD-ESP32-S3_materials/USB%20to%20serial%20CH343%20driver/)

Open firmware download tools and then select ESP32 + Develop + UART mode. [Micropython firmware download tool /additional-resource/YD-ESP32-S3_materials/firmware-downloard tool/](/additional-resource/YD-ESP32-S3_materials/firmware-downloard%20tool/)</br>
Select firmware of "YD-ESP32-S3-N16R8-MPY.bin" to write at 0x00 of flash of ESP32 board.</br>
SpiFlashConfig select: 40MHz, DIO SPI MODE. </br>
Finally select correct COM port (depends on the physical port on computer) and BAUD must be 115200

If you want to have more advance use on the firmware download tool you can read the user guidelines PDF file in the folder. [User Guideline of Firmware download tool](/additional-resource/YD-ESP32-S3_materials/firmware-downloard%20tool/Flash_Download_Tool__en.pdf)
### FINALLY: Restart and reconnect the board, finally check status ensure everything work correctly.
After that, you start develop python program on ESP32 perfectly. 

## ***Basic / Example Projects of ESP32***
Here is some example projects done by Jason yang. It can be a good examples of using Micropython in programming ESP32. 
### Control of implanted RGB
It can make the implanted RGB light light in a breathing mode without block the main program (work in multi-threads). It will turn in rainbow colours (GREEN -> BLUE -> RED -> YELLOW) with 300 steps transition each time.

Here is some key knowledge that you can study from this example project: 
- using machine.Pin to control the PWM output of GPIO Pin
- study the difference between `utime` and `time` in micropython, `utime` provide more useful functions such as sleep in a smaller interval and provide a more accurate tick counter.
- learn the python decorator usage. Write the multi-thread in a decorator and make it can directly use for function to run without block of main thread.
### Network Access through implanted WIFI in ESP32
There provide two kind of working mode of WIFI (AP mode and WIFI mode). It makes ESP32 can serve as server and client separately.
- AP mode (ESP32 act as a server):
It will create a hotpot object with your self defined name (without a password). There is a WIFI 4 802.11n implanted in ESP32.
- WIFI mode (Normal mode of ESP32 act as a client):
It can connect to a WIFI and send and receive LAN messages. With the provided wifi name and password, ESP32 can get access to the WIFI network.

Here is some key knowledge that you can study from this example project: 
- The basic use of `network` to create a WIFI object in STA-IF and AP_IF mode