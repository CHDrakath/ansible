from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)




try:
    inventory = {
            "r1": {
                "ip" : "172.12.0.1",
                "ospf_config" : [
                    "router ospf 1", 
                    "network 172.1.0.0 0.0.255.255 area 0",
                    "network 172.12.0.0 0.0.255.255 area 0",
                    "passive-interface fastEthernet 0/0",

                ]
            },
            "r2": {
                "ip" : "172.12.0.2",
                "ospf_config" : [
                    "router ospf 1",
                    "network 172.12.0.0 0.0.255.255 area 0",
                    "passive-interface fastEthernet 0/0",
                ]
            },           
        }

    for host_name in inventory:
        device = {
            "host" : inventory[host_name]["ip"],
            "device_type":'cisco_ios_telnet',
            "username":"admin",
            "password" :"admin",
            "secret" : "admin"
        }
        with ConnectHandler(**device) as net_connect:
            net_connect.enable()
            net_connect.config_mode()
            net_connect.send_config_set(inventory[host_name]["ospf_config"])
            net_connect.exit_config_mode()
    with ConnectHandler(**device) as net_connect:
        import time as t
        result = ""
        while True:
            try:
                device = {
                "host" : "172.12.0.1",
                "device_type":'cisco_ios_telnet',
                "username":"admin",
                "password" :"admin",
                "secret" : "admin"
                }
                with ConnectHandler(**device) as net_connect:
                    t.sleep(2)
                    if str(result).find("FULL") != -1:
                        break
                    else:
                        print("waiting for ospf full state...")
                    result = net_connect.send_command("show ip ospf neighbor")
            except (NetmikoTimeoutException, NetmikoAuthenticationException) as ex:
                print(f"Request failed: {ex}")
        print(result)
except (NetmikoTimeoutException, NetmikoAuthenticationException) as ex:
    print(f"Request failed: {ex}")
