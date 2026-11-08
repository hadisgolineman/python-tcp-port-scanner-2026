import socket
import ipaddress
from datetime import datetime

COMMON_PORTS = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP-ALT"
}


def get_target():
    target = input("Enter target IPv4 address: ")

    try:
        ip = ipaddress.ip_address(target)

        if ip.version == 4 and (ip.is_loopback or ip.is_private):
            return str(ip)

        print("Only localhost and private IPv4 addresses are allowed.")
        return None

    except ValueError:
        print("Invalid IP address.")
        return None


def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            return result == 0

    except OSError:
        return False


def main():
    target = get_target()

    if target is None:
        return

    start_time = datetime.now()

    print(f"\nScanning target: {target}")
    print(f"Scan started at: {start_time}")

    open_ports = 0
    scan_results = []

    for port, service in COMMON_PORTS.items():

        if scan_port(target, port):
            result = f"Port {port} ({service}) is OPEN"

            print(result)
            scan_results.append(result)
            open_ports += 1

    end_time = datetime.now()

    print(f"\nScan finished at: {end_time}")
    print(f"Total open ports: {open_ports}")

    with open("scan_report.txt", "w", encoding="utf-8") as file:

        file.write(f"Target IP: {target}\n")
        file.write(f"Scan started: {start_time}\n")
        file.write(f"Scan finished: {end_time}\n")
        file.write(f"Total open ports: {open_ports}\n")

        file.write("\nOpen Ports:\n")

        for result in scan_results:
            file.write(result + "\n")

    print("\nReport saved successfully.")


if __name__ == "__main__":
    main()