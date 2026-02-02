import datetime

endTime = datetime.datetime(2027,12,4)
site_block = ["www.regexr.com","www.youtube.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"


while True:
    if datetime.datetime.now() < endTime:
        with open(host_path,"+r") as host_file:
            data = host_file.read()
            for site in site_block:
                if site not in data :
                    print(f"{site} is blocked.")
                    host_file.write(f"{redirect} {site}")

    else :
        print("Unblocked")
        with open(host_path,"+r") as host_file:
            data = host_file.read()
            host_file.seek(0)
            data_list = data.split("\n")
            for lines in data_list:
                for site in site_block:
                    if site not in lines:
                        host_file.write(f"{lines}\n")



                    