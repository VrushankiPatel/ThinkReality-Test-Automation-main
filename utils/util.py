import shlex
import subprocess
import os
import sys
import time


def execute(command, check, shell):
    if not shell:
        # split string into list of strings (words)
        parsed_command = shlex.split(command)
    else:
        parsed_command = command

    # # subprocess.PIPE: store output into memory (variables), instead of outputting to console
    process = subprocess.run(
        parsed_command,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=check, shell=shell,
    )

    return process.stdout


def load_appium_driver_setting(package_name, activity_name, enable_web_debugging=False, no_reset=False):
    capabilities = dict(
        platformName="Android",
        automationName="uiautomator2",
        # deviceName = "motorola edge 30 pro",
        appPackage=package_name,
        appActivity=activity_name,
        autoGrantPermissions=True,  # Automatically grant access when popup appears
        enableMultiWindows=True, # Allow driver to detect overlay windows
        noReset=no_reset, # Determine if the driver will delete cache when starting app
    )

    if enable_web_debugging:
        capabilities['chromedriverExecutable'] = os.getenv("CHROME_DRIVER_LOCATION")
        capabilities['setWebContentsDebuggingEnabled'] = True

    return capabilities


def countdown(second):
    for remaining in range(second, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
