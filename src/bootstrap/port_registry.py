import socket

def probe_ports(ports=None):
    if ports is None:
        ports = [11434, 8000, 1234, 8080]
    
    active_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex(("localhost", port))
            if result == 0:
                active_ports.append(port)
        except Exception:
            pass
        finally:
            sock.close()
    
    return active_ports