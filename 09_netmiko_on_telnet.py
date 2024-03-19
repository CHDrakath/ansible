import netmiko

connection = netmiko .ConnectHandler(host='192.168.18.192',
                                     device_type='cisco_ios_telnet',
                                     password='admin',
                                     secret='admin'
                                    )

print("Successful\n")
result = connection.send_command('show ip interface brief | ex un')
print(result)