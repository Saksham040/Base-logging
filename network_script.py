import netmiko  # Import the Netmiko library for network device automation

# List of IP addresses for devices to connect to
ip_list = [
    '10.254.0.1',  # Device 1
    '10.254.0.2',  # Device 2
    '10.254.0.3',  # Device 3
]

print(ip_list[0])  # Print the first IP address in the list
print(ip_list[-1])  # Print the last IP address in the list

# Credentials and connection details
username = 'cisco' 
# Username for the devices
password = 'csico'  
# Password for the devices
device_type = 'cisco_ios' 
# Type of device (Cisco IOS)
port = 22 
# SSH port number

# List to store command outputs
output_list = []

# Loop through each IP address in the list
for ip in ip_list:
    # Establish an SSH connection to the device
    net_connect = netmiko.ConnectHandler(
        ip=ip,  # IP address of the device
        device_type=device_type,  # Device type
        username=username,  # Username
        password=password,  # Password
        port=port  # SSH port
    )

    # Send the command to get interface details
    output = net_connect.send_command('show ip interface brief')
# Append the command output to the list
output_list.append(output) 


# Print the output from each device
for output in output_list:
    print(output)  # Print the command output
