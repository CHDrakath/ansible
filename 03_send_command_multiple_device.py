import netmiko

d_list = ["172.1.0.254", "172.12.0.254"]
for device in d_list:
    connection = netmiko.ConnectHandler(
        host = device,
        device_type = "cisco_ios",
        username = "admin",
        password = "admin"
    )
    result = connection.send_command("show ip interface brief | ex un")
    print(f"{device} ip li cihazın interfaceleri")
    print(result)
    print("\n")
    connection.disconnect()
