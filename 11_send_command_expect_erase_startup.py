import netmiko
connection = netmiko.ConnectHandler(
    host = "172.1.0.254",
    device_type = "cisco_ios",
    username ="admin",
    password ="admin"
)
result = connection.send_command(
    "erase startup-config",
    expect_string="Continue?",
    read_timeout=10
)
print(result)
connection.disconnect()