import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
        octets = ip.split(".")
        for octet in octets:
            if len(octet) > 1 and octet.startswith("0"):
                return False
            try:
                if not 0 <= int(octet) <= 255:
                    return False
            except ValueError:
                return False
        return True
    return False

if __name__ == "__main__":
    main()