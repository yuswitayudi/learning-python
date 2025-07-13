# Import the socket module for network connections
import socket
# Import sys module (not used in this script, but commonly used for system-specific parameters)
import sys


# Function to check if a TCP port is open on a given host
def check_port(host, port, timeout=1):
    try:
        # Create a TCP socket (IPv4, TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt (in seconds)
        sock.settimeout(timeout)
        # Try to connect to the host and port
        sock.connect((host, port))
        # If connection is successful, print and return True
        print(f"[{host}:{port}] is open")
        return True
    except (socket.timeout, socket.error) as e:
        # If connection fails or times out, print error and return False
        print(f"[{host}:{port}] is closed or unreachable: {e}")
        return False
    finally:
        # Always close the socket to free resources
        sock.close()
    

# Example usage of the check_port function

if __name__ == "__main__":
    # Entry point for script execution
    print("Running port check script...")
    
    # Example 1: Check a common open port (HTTP)
    print("\nChecking google.com on port 80 HTTP")
    check_port("google.com", 80)
    
    # Example 2: Check a common secure port (HTTPS)
    print("\nChecking google.com on port 443 HTTPS")
    check_port("google.com", 443)
    
    # Example 3: Check a port that is likely closed on a public IP
    print("\nChecking google.com on port 9999 (likely closed)")
    check_port("google.com", 9999)
    
    # Example 4: Check a port on localhost (DNS)
    print("\nChecking localhost on port 53")
    check_port("localhost", 53)
    
    # Example 5: Check a port on localhost that is likely closed
    print("\nChecking localhost on port 9999 (likely closed)")
    check_port("localhost", 9999)