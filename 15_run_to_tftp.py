from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

device = {
    "host" : "172.1.0.254",
    "device_type" : "cisco_ios",
    "username" : "admin",
    "password" : "admin"
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
    print(f"Request failed: {ex}")