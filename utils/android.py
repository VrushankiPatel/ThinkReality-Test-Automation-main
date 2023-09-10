from utils.util import execute
from getgauge.python import step


def adb(args, check=False, shell=False):
    return execute("adb " + args, check, shell).strip()

def check_wifi_connectivity():
    adb("shell dumpsys wifi | grep -E 'mWifiInfo SSID: \"[^\"]+\"' | cut -d'\"' -f2", shell=True) != None

def swipe_up():
    adb("shell input swipe 500 1500 0 0")  # workaround to scroll up

def force_stop_app(package_name):
    adb(f"shell am kill {package_name}")

def push_provision_file_to_device():
    adb("push 'c:\\Android\\udc-provision.json' 'sdcard/Download'")

def grant_camera_permissions(package_name):#com.qualcomm.qti.spaces.services
    adb(f"shell pm grant {package_name} android.permission.CAMERA")

def grant_microphone_permissions(package_name):
    adb(f"shell pm grant {package_name} android.permission.RECORD_AUDIO")

def grant_notification_permissions(package_name):
    adb(f"shell pm grant {package_name} android.permission.POST_NOTIFICATIONS")

def start_app_activity(package_name, activity_name):
    adb(f"shell am start -n {package_name}/{activity_name}")

def install_udc_app():
    adb("install 'C:\\Android\\udc.apk'")

def check_current_activity() -> str:
    return adb("shell \"dumpsys activity | grep 'mCurrentFocus'\"")