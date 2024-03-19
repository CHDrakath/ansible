from netmiko import (
    ConnectHandler,
    NetMikoTimeoutException,
    NetmikoAuthenticationException,    
)
device = {
    "host" : "172.1.0.254",
    "device_type" : "cisco_ios",
    "username" : "admin",
    "password" : "admin"
}
try:
    with ConnectHandler(**device) as connection:
        acl_command_list = [
            "access-list 19 deny host 19.19.19.19",
            "access-list 19 permit any",
        ]
        connection.send_config_set(acl_command_list, read_timeout=10)
        result = connection.send_command(
            "show access-list", read_timeout=10
        )
        print(result)
        print("\n")
        acl_command_list = [
            "no access-list 19"
        ]
        connection.send_config_set(acl_command_list, read_timeout=10)
        result = connection.send_command(
            "show access-list", read_timeout=10
        )
        print(result)
except(NetMikoTimeoutException, NetmikoAuthenticationException) as ex:
    print(f"Request failed: {ex}")