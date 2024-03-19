import netmiko
connection = netmiko.ConnectHandler(
    host ="172.1.0.254",
    device_type ="cisco_ios",
    username ="admin",
    password ="admin"
)
result = connection.send_command(
    "show run",
    read_timeout=10
)
# result = connection.send_commend_expert(
#      "show tcp brief",
#      read_timeout=60
# )
print(result)
connection.disconnect()