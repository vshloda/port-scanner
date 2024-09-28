import socket
import threading

# Maximum number of concurrent threads
max_threads = 50
# Semaphore to limit the number of active threads
semaphore = threading.Semaphore(max_threads)

def grab_banner(s):
    """
    Attempts to grab a banner from the connected socket.
    
    Args:
        s (socket.socket): The socket to read from.
    
    Returns:
        str or None: The banner if successfully retrieved, otherwise None.
    """
    try:
        # Receive up to 1024 bytes from the socket and decode it
        banner = s.recv(1024).decode().strip()
        return banner
    except Exception as e:
        # Handle exceptions while grabbing the banner
        # print(f"Error grabbing banner: {e}")
        return None

def scan_port(target, port, timeout):
    """
    Scans a specific port on the target server to check if it is open.
    
    Args:
        target (str): The target IP address or hostname.
        port (int): The port number to scan.
        timeout (float): The timeout duration for the connection attempt.
    """
    with semaphore:
        try:
            # Create a new socket for the connection
            with socket.socket() as s:
                s.settimeout(timeout)  # Set the timeout for the socket
                s.connect((target, port))  # Attempt to connect to the target on the specified port
                banner = grab_banner(s)  # Try to grab the service banner
                if banner:
                    print(f"Port {port} is open: {banner}")  # Print the open port and the banner if available
                else:
                    print(f"Port {port} is open")  # Print the open port if no banner was retrieved
        except (socket.timeout, ConnectionRefusedError):
            # Ignore timeout or connection refusal errors
            pass
            # print(f"Port {port} is closed or filtered (timeout)")
        except Exception as e:
            # Handle other exceptions
            # print(f"Error on port {port}: {e}")
            pass

def banner_grabbing_port_scan(target, port_range, timeout=0.1, batch_size=100):
    """
    Scans a range of ports on the target server using multiple threads.
    
    Args:
        target (str): The target IP address or hostname.
        port_range (tuple): A tuple specifying the range of ports (start, end).
        timeout (float): The timeout duration for each connection attempt.
        batch_size (int): The number of ports to scan concurrently.
    """
    ports = range(*port_range)  # Create a range of ports to scan
    for i in range(0, len(ports), batch_size):
        threads = []
        for port in ports[i:i + batch_size]:
            # Create a thread for scanning the current port
            t = threading.Thread(target=scan_port, args=(target, port, timeout))
            threads.append(t)
            t.start()  # Start the thread

        for t in threads:
            t.join()  # Wait for all threads to finish

# Entry point of the script
if __name__ == "__main__":
    target_ip = '192.168.1.1'  # Replace with the target IP address
    port_range = (1, 10001)  # Define the range of ports to scan (1 to 10000)
    banner_grabbing_port_scan(target_ip, port_range)  # Start the port scanning process
