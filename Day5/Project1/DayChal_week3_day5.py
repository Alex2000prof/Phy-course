import requests
import time
def check_open_time(url):
    try:
        start = time.perf_counter()  
        response = requests.get(url) 
        end = time.perf_counter()  
        if response.status_code == 200:
            loading_time = end - start  
            return loading_time
        else:
            return None
    except requests.RequestException:
        return None
url = input("enter url: ")
loading_time = check_open_time(url)
if loading_time is not None:
    print(f"time: {loading_time}")
else:
    print("none")