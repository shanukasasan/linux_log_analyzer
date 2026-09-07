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

failed_attempts=0
invalid_user_attempts=0
invalid_users = {}
failed_ips = {}
failed_users = {}
with open("data/sample.log", "r") as file:
    for line in file:
        if failed_logins(line):
            failed_attempts += 1

            #Extracting IP address and username from the log line
            ip_address = get_ip(line)
            username = get_username(line)       

            if is_invalid_user(line):
                invalid_user_attempts += 1
                increase_count(invalid_users, username)
           
            increase_count(failed_ips, ip_address)
            increase_count(failed_users, username)

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