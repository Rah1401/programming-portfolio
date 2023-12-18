import sys

def report_os_platform():
    """
    Reports the operating system platform using the sys module.
    """
    platform = sys.platform
    if platform.startswith('linux'):
        print("Linux platform detected.")
    elif platform.startswith('darwin'):
        print("Mac OS platform detected.")
    elif platform.startswith('win'):
        print("Windows platform detected.")
    else:
        print("Unknown platform detected:", platform)

if __name__ == "__main__":
    report_os_platform()
