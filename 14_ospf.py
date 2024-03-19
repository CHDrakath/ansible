from netmiko import (
    ConnectHandler,
    NetMikoTimeoutException,
    NetmikoAuthenticationException,    
)
device = {
    "host" : "172.12.0.1",
    "device_type" : "cisco_ios_telnet",
    "username" : "admin",
    "password" : "admin",
    "secret" : "admin"
}
try:
    with ConnectHandler(**device) as connection:
        acl_command_list = [
            "router ospf 1",
            "network 172.12.0.0 0.0.255.255 area 0",
            "network 172.1.0.0 0.0.255.255 area 0",
        ]
        connection.enable()
        connection.config_mode()
        connection.send_config_set(acl_command_list, read_timeout=10)
        connection.exit_config_mode()
        result = connection.send_command(
            #"show run | i ospf", read_timeout=10
            "show run | s router ospf", read_timeout=10
            #"show ip ospf neighbor", read_timeout=10
        )
        print(result)
except(NetMikoTimeoutException, NetmikoAuthenticationException) as ex:
    print(f"Request failed: {ex}")