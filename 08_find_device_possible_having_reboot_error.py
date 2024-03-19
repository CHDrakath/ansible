import netmiko

d_list = ["172.1.0.254","172.12.0.254"]
print("""
cihazların up-time süresi
-------------------"""
)
for device in d_list:
    connection = netmiko.ConnectHandler(
        host = device,
        device_type = "cisco_ios",
        username = "admin",
        password = "admin"
    )
    result = connection.send_command(
        "show version",
        use_textfsm = True,
        read_timeout = 10
    )
    if result[0]['uptime_hours'].isdigit():
        if int(result[0]['uptime_hours'])>5:
            print(f"ip [{device}] : {result[0]['uptime_hours']} saat")
        else:
            print(f"ip [{device}] : Reboot Error - 1 Hour < Uptime < 5 Hour")
    else:
        print(f"ip [{device}] : Reboot Error - Uptime < 1 Hour")
    connection.disconnect()
