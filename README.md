# Run Test

## Test Environment Setup
**Following steps may be ignored when using Docker approach** 
### 1. Appium Installation

#### Install Node.js
1. Go to the Node.js [website](https://nodejs.org/en/download) and select Windows Installer 64-bit
2. Run the installer
3. Check if Node.js is correctly setup, open the command line and input `node -v`

#### Install Android SDK tool
1. Go to Android SDK tool [website](https://developer.android.com/tools/releases/platform-tools), and select **Download SDK Platform-Tools for Windows**
2. Unzip the file, and the place the **platform-tools** folder to a dedicated location (ex: C:\Android\platform-tools)
3. Add a new environment variable
    * ANDROID_HOME = C:\Android\platform-tools
4. Add to PATH
    * C:\Android\platform-tools

#### Install OpenJDK (Java)
1. Go to OpenJDK download [page](https://adoptium.net/temurin/releases/?version=11)
2. Download Windows JDK msi 
3. Run the installer
    * Click Set JAVA_HOME variable

#### Install Appium server and driver
1. Open the command line
1. Run command `npm i -g appium@next`
2. Run command `appium driver install uiautomator2`
3. Test server running, run command `appium` 

### 2. Python Installation
1. Download the [Python Installer](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)
2. Follow the steps from this [website](https://www.digitalocean.com/community/tutorials/install-python-windows-10) to run the installer

### 3. Gauge Installation
1. Download the [Gauge Installer](https://github.com/getgauge/gauge/releases/download/v1.4.3/gauge-1.4.3-windows.x86_64.exe) and run

## Prerequisites
### 0. Devices & Environments
* Rogue phone
* ADB (Android Debug Bridge) tool installed
* Python3 installed
* Gauge installed
* Appium installed


### 1. Enable Wifi debugging
1. Connect the Moto Phone to your laptop using a USB cable.
2. Run the following command to check if the device is connected:
    ```
    adb devices
    ```
3. Connect the Rogue Phone and your laptop to the same Wi-Fi network. Use "Mobile Hotspot" from Windows and connect the Moto Phone to the Windows network.
4. Run the following commands to enable Wi-Fi debugging on the Moto Phone. You can find the IP address in Setting -> About phone -> 192.168.xxx.xxx
    ```
    adb tcpip 5555
    adb connect <phone_ip_address>
    ```

### 2. Install Python Dependencies
1. Run the following command to check if the device is connected
    ```
    pip install -r requirements.txt
    ```
### 3. Download Chromedriver for Moto Phone

1. Find all the available chromedriver from this [page](https://chromedriver.chromium.org/downloads)
2. Select the version that correspond to the Chrome version on Moto phone
3. Download `chromedriver_win32.zip`
4. Extract the file and place at any desired location


### 4. Run Appium Server
1. Run the following command to start the Appium server
    ```
    appium --allow-insecure chromedriver_autodownload --allow-insecure adb_shell
    ```
## Run Tests

*  Run tests on specific file
    ```
    gauge run --hide-suggestion --simple-console --max-retries-count 3 c:\Android\Project\ThinkReality-test-automation\specs\<filename>.spec
    ```


## Troubleshooting
1. If device cannot connect to adb through wifi:

    * Create "Mobile Hotshot" using laptop, and set phone wifi to connect to that

        Click Windows Search -> Type "Mobile Hotspot"

    * Run the following command to restart adb server
        ```
        adb kill-server
        ```

### Reference
[UDC Test suite](https://bitbucket.tc.lenovo.com/projects/UDC/repos/test-suite/browse)
