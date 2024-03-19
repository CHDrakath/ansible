import netmiko
connection = netmiko.ConnectHandler(
    host = "172.1.0.254" ,
    device_type = "cisco_ios",
    username = "admin",
    password = "admin"
)
connection.disconnect()