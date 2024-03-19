from netmiko import(
    ConnectHandler,
    NetMikoTimeoutException,
    NetmikoAuthenticationException,
)
import time
device = {
    "host" : "172.1.0.254",
    "device_type" : "cisco_ios",
    "username" : "admin",
    "password" : "admin"
}
try:
    start_time =time.time()
    with ConnectHandler(**device) as connection:
        result = connection.send_command(
            "show tcp brief",
            read_timeout=1800
        )
        print(result)
except (NetMikoTimeoutException, NetmikoAuthenticationException) as ex:
    print(f"Request failes: {ex}")
finally:
    end_time = time.time()
    duration = end_time -start_time
    print(f"Running time of code: {duration:.2f} seconds")