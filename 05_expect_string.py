import  netmiko
connection = netmiko.ConnectHandler(
    host = "172.1.0.254",
    device_type = "cisco_ios",
    username = "admin",
    password = "admin"
)
print("komut öncesi startap'daki hostname")
print("-"*50)
result = connection.send_command("show startup-config | i hostname",read_timeout=10)
print(result)
print("\n")
#--------------------------------------------------------------------------------------------
result += connection.send_command_expect("copy running-config startup-config", expect_string ="Destination filename")
result += connection.send_command_expect("", expect_string="Building configuration...")
print("komut sonrası startup'daki hostname")
print("-"*50)
result = connection.send_command("show startup-config | i hostname", read_timeout=10)
print(result)
print("\n")
connection.disconnect()