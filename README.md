# Port Scanner with Banner Grabbing

## Description

This project implements a multi-threaded port scanner that identifies open ports on a specified server and attempts to grab the service banner from those ports. The scanner is capable of scanning a wide range of ports efficiently by using a semaphore to limit the number of concurrent threads. It supports customizable port ranges and timeouts.

## Features

- Multi-threaded scanning for faster performance
- Ability to grab service banners from open ports
- Configurable port ranges and timeouts
- Handles common socket errors gracefully

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vshloda/port-scanner.git
   cd port-scanner

## Usage

	1.	Open the port_scanner.py file and update the target_ip variable to the IP address of the server you want to scan.
	2.	Define the port range in the port_range variable (default is 1 to 10000).
	3.	Run the script:
   
```bash
python port_scanner.py
```



## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
