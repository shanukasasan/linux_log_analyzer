message = "Failed password for root from 192.168.1.50 port 51244 ssh2"

parts = message.split()
ip_index = parts.index("from") + 1
print(parts[ip_index])