import socket

class PortFinder:
    @staticmethod
    def is_port_available(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return True
            except socket.error:
                return False

    @staticmethod
    def get_free_ports(count=10):
        sockets = []
        ports = []

        for _ in range(count):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.bind(('127.0.0.1', 0))
                port = s.getsockname()[1]
                s.close()  # Close immediately after getting port
                
                # Double check if port is really available
                if PortFinder.is_port_available(port):
                    ports.append(port)
                else:
                    # Try to find another port
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind(('127.0.0.1', 0))
                    port = s.getsockname()[1]
                    s.close()
                    ports.append(port)
                    
            except Exception as e:
                s.close()
                raise e

        return ports

