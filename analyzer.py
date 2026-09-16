from datetime import datetime


def increase_count(dictionary,key):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def get_ip(line):
    parts = line.split()
    ip_index = parts.index("from") + 1
    ip_address = parts[ip_index]
    return ip_address

def get_username(line):
    parts = line.split()
    username_index = parts.index("from") -1
    username = parts[username_index]
    return username

def failed_logins(line):
    if "failed password" in line.lower():
        return True
    return False

def is_invalid_user(line):
    if "invalid user" in line.lower():
        return True
    return False

def get_timestamp(line):
    parts = line.split()
    month = parts[0]
    day = parts[1]
    time = parts[2]
    timestampholder = f"{month} {day} {time}"
    timestamp = datetime.strptime(timestampholder, "%b %d %H:%M:%S")
    return timestamp

def is_brute_force(timestamp,threshold=5, window=60):
    if len(timestamp) >= threshold:
        for i in range(len(timestamp) - threshold + 1):
            start_time = timestamp[i]
            end_time = timestamp[i + threshold - 1]
            time_diff = (end_time - start_time).total_seconds()
            if time_diff <= window:
                return True, start_time, end_time

    return False, None, None

def successful_logins(line):
    if "accepted password" in line.lower() or "accepted publickey" in line.lower():
        return True
        
    return False




failed_attempts=0   
invalid_user_attempts=0
invalid_users = {}
failed_ips = {}
failed_users = {}
failed_timestamps = {}
successful_logins_data = {}
with open("data/sample.log", "r") as file:
    for line in file:
        if failed_logins(line):
            failed_attempts += 1

            #Extracting IP address and username from the log line
            ip_address = get_ip(line)
            username = get_username(line)
            timestamp = get_timestamp(line)

            if is_invalid_user(line):
                invalid_user_attempts += 1
                increase_count(invalid_users, username)
           
            increase_count(failed_ips, ip_address)
            increase_count(failed_users, username)

            if ip_address in failed_timestamps:
                failed_timestamps[ip_address].append(timestamp)
            else:
                failed_timestamps[ip_address] = [timestamp]

        if successful_logins(line):
            
            username = get_username(line)
            ip_address = get_ip(line)
            timestamp = get_timestamp(line)

            key = (username, ip_address)

            if key in successful_logins_data:
                successful_logins_data[key].append(timestamp)
            else:
                successful_logins_data[key] = [timestamp]
           

print("****************Log Analysis Report****************\n")
print(f"Total failed password attempts: {failed_attempts}")
print(f"Total invalid user attempts: {invalid_user_attempts}\n")

print("Failed Attempts by IP Address:")
for ip, count in failed_ips.items():
    if count >= 5:
        print(f"IP Address: {ip:<15}, Failed Attempts: {count:<5} <---Potential Brute Force Attack Detected!")
    else:
        print(f"IP Address: {ip:<15}, Failed Attempts: {count:<5}")

print("\nTargeted Accounts:")        
for username, count in failed_users.items():
    print(f"{username:<10}: Failed Attempts: {count:<5}")

print("\nInvalid Accounts Detected:")
for username, count in invalid_users.items():
    print(f"{username:<10}: Failed Attempts: {count}")

print("\nTimestamps of Failed Attempts by IP Address:")
for ip, timestamps in failed_timestamps.items():
    detected, start_time, end_time = is_brute_force(timestamps)
    if detected:
        duration = (end_time - start_time).total_seconds()
        print(f"IP Address: {ip:<15}")
        print(f"Attack Window: {start_time} to {end_time}")
        print(f"Duration: {duration} seconds")
        print("Potential Brute Force Attack Detected!")
    
print("\nSuccessful Logins:")
for (username, ip), timestamps in successful_logins_data.items():
    print(f"Username: {username:<10}, IP Address: {ip:<15}, Successful Logins: {len(timestamps)}")