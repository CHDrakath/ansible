from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

d_list = ["172.1.0.254", "172.12.0.254"]

for asd in d_list:
    device = {
        "host": asd,  # Corrected to use the IP address from d_list
        "device_type": "cisco_ios",
        "username": "admin",
        "password": "admin"
    }

    try:
        with ConnectHandler(**device) as net_connect:
            result = ""
            commands = [
                "copy running-config tftp",
                "192.168.22.58",
                "\n",
            ]
            for cmd in commands:
                result += net_connect.send_command_timing(
                    cmd,
                    strip_command=False,
                    strip_prompt=False
                )
            print(result)
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as ex:
        print("\n")
        print(f"Request failed for {asd}: {ex} ")