# TCP Port Scanner

A Python-based TCP port scanner for discovering open ports and common network services.

## Project Description

This project is a simple network security tool developed using Python. It scans selected TCP ports on a target IPv4 address and identifies which ports are open.

The scanner focuses on common network services and generates a report containing the scan results.

## Features

- IPv4 address validation
- TCP port scanning
- Detection of open ports
- Identification of common network services
- Scan start and finish timestamps
- Automatic scan report generation
- Support for localhost and private IPv4 addresses

## Technologies Used

- Python
- Socket
- IP Address
- Datetime

## Common Ports

The scanner checks the following ports:

| Port | Service |
|---|---|
| 20 | FTP-DATA |
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 8080 | HTTP-ALT |

## Security Concepts

- TCP Networking
- Port Scanning
- Network Reconnaissance
- Service Discovery
- Network Security
- IP Address Validation

## How to Run

1. Clone the repository.
2. Open the project directory.
3. Run the following command:

```bash
python port_scanner.py
```

4. Enter a valid localhost or private IPv4 address.

## Output

The scanner displays detected open ports in the terminal.

It also automatically generates a file named `scan_report.txt` containing:

- Target IP address
- Scan start time
- Scan finish time
- Total number of open ports
- List of detected open ports

## Security Note

This project is developed for educational purposes and authorized security testing.

Only scan systems and networks that you own or have explicit permission to test.

## Author

Computer Engineering Student | Cybersecurity Enthusiast