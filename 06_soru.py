import netmiko

d_list = ["172.1.0.254","172,12,0,254"]
print("Def. isimli cihazlar\n-------------------------")
for device in d_list:
    connection = netmiko.ConnectHandler(
        host = device,
        device_type = "cisco_ios",
        username = "admin",
        password = "admin"
    )
    result = connection.send_command(
        "show version",
        use_textfsm =True,
        read_timeout =10
    )
    if result[0]['hostname'] == "Switch":
        print(f"ip: {device}")
    connection.disconnect()