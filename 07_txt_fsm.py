import netmiko
connection = netmiko.ConnectHandler(
    host ="172.1.0.254",
    device_type = "cisco_ios",
    username = "admin",
    password = "admin"
)
result = connection.send_command(
    "show version",
    use_textfsm = True,
    read_timeout=10
)
print("\n")
print(f"cihaz adı : {result[0]['hostname']}")
print(f"açık kalma süresi : {result[0]['uptime']}")
print(f"çalışan imaj : {result[0]['running_image']}")
print(f"cihaz mac adresi : {result[0]['mac_address'][0]}")
print("\n")
connection.disconnect()