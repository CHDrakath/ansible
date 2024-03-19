import netmiko

connention = netmiko.ConnectHandler(
    host = "172.1.0.254",
    device_type = "cisco_ios",
    username = "admin",
    password = "admin"
)
connention.enable()
connention.config_mode()
connention.send_command("hostname Ag-1",expect_string=r"#",read_timeout=10 )
connention.exit_config_mode()
result = connention.send_command("show running-config | i hostname")
print(result)
print("\n")
connention.disconnect()