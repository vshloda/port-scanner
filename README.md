# port-scanner
This project implements a multi-threaded port scanner that identifies open ports on a specified server and attempts to grab the service banner from those ports. The scanner is capable of scanning a wide range of ports efficiently by using a semaphore to limit the number of concurrent threads. It supports customizable port ranges and timeouts.
