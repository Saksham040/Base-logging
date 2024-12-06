import netmiko  # Import the Netmiko library for network device communication.

def main():
    # Define connection details for the Cisco device.
    csr = netmiko.ConnectHandler(
        device_type='cisco_ios',  # Specify the type of device (Cisco IOS).
        host='192.168.1.1',       # IP address or hostname of the device.
        username='cisco',         # Username for authentication.
        password='cisco'          # Password for authentication.
    )
    
    # Send the 'show ip route' command and capture the output.
    output = csr.send_command('sh ip route')
    print(output)  # Print the command output to the console.
    
    # Disconnect from the device to free up resources.
    csr.disconnect()

if __name__ == '__main__':
    main()  # Call the main function to execute the script.


#Key Points and Corrections:
    #Parameters in Key-Value Format: Connection parameters (device_type, host, username, password) are correctly passed as key-value pairs to ConnectHandler.
 #   Indentation Fix: Ensured proper indentation for the code block, especially the main() function definition and call.
 #   Whitespace Removal: Removed the extra whitespace in the host=' 192.168.1.1' parameter.
 #   Comments: Added comments to explain each step of the code.
#    Best Practice: Included a csr.disconnect() method to properly close the connection after the command execution.
 #   Make sure the Netmiko library is installed using pip install netmiko before running the script. Let me know if you need further assistance!
