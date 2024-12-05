import netmiko  # Import the Netmiko library for network device automation
import re  # Import the regular expression library for pattern matching and manipulation

# Establish an SSH connection to the device
csr = netmiko.ConnectHandler(
    '10.254.0.1',  # IP address of the device
    username='cisco',  # Username for the device
    password='cisco',  # Password for the device
    device_type='cisco_ios'  # Specify the device type (Cisco IOS in this case)
)

# Fetch the running configuration of the device
running_config = csr.send_command('show run')  # Send the 'show run' command to get the current configuration
# Uncomment the next line to see the full running configuration
# print(running_config)

# Define a regular expression pattern to find the specific interface configuration
pattern = r'interface  GigabitEthernet1\n.+'  # Match the 'interface GigabitEthernet1' line and its associated configuration

# Define the replacement string with the updated configuration
repl = ' interface GigabitEthernet1\n ip address 10.11.0.1 255.255.255.0'  # Replace the IP configuration of the interface

# Use re.sub() to replace the matched pattern with the new configuration string
update_config = re.sub(pattern, repl, running_config)  # Replace the matched section in the running configuration with the new configuration

# Print the updated configuration to verify changes
print(update_config)  # Display the modified configuration to confirm the update

# send the updated configuration back to the device
csr.send_config_set(update_config.split('\n'))

#Save the configuration to the startup configuration:
csr.send_command('write memory')


#Disconnect the session once done:
csr.disconnect()
