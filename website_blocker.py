import time
from datetime import datetime as dt

host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_lists=["http://www.msn.com/en-in/?ocid=iehp","https://www.facebook.com","www.images.com"]
final_list=[redirect+""+i for i in website_lists]
final_string_blocklist=["\n".join(final_list)]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,28 < dt.now().year,dt.now().month,dt.now().day,30):
        print("within time")
        with open(host_path,"r+") as file:
            content= file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect+""+website+"\n")
    else:
        with open(host_path, "+r") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in  website_lists):
                    file.write(line)
            file.truncate()
    time.sleep(2,5)


