from netmiko import(
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
device = {
    "host" : "172.1.0.254",
    "device_type" : "cisco_ios",
    "username" : "admin",
    "password" : "admin",
}

try:
    with ConnectHandler(**device) as net_connect:
        acl_config_file ="acl_config.txt"
        net_connect.send_config_from_file(acl_config_file,read_timeout=10)
        result=net_connect.send_command(
            "show access-list",read_timeout=10
        )
        print(result)
except (NetmikoTimeoutException,NetmikoAuthenticationException) as ex :
    print(f"Request failed: {ex}")