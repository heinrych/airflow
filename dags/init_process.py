import requests
import json
import time 


base_url = "http://localhost:8080/nifi-api/"

def get_process(processor_id):
    url  = base_url + f"processors/{processor_id}"

    response = requests.get(url)

    return response.json()['component']['state'], response.json()['revision']['version']


def get_status(processor_id):
    url  = base_url + f"processors/{processor_id}/state"

    return requests.get(url).json()['componentState']['localState']['state'][0]['value']

   

def set_status(processor_id,version,status):
    url = base_url + f"processors/{processor_id}/run-status"

    body = json.dumps({
        "revision":{"version": int(version)},
        "state": status,
    })


    headers={
        'Content-type':'application/json', 
        'Accept':'application/json'
    }

    return requests.put(url, headers=headers, data=body)


def start_process():

    status,version = get_process("f3e04459-018f-1000-0000-00003ad8f1d1")
    print(status,version)

    if status == 'STOPPED': 

        set_status("f3e04459-018f-1000-0000-00003ad8f1d1",version,'RUNNING')
        time.sleep(5)
    
    status,version = get_process("f3e04459-018f-1000-0000-00003ad8f1d1")
    print(set_status("f3e04459-018f-1000-0000-00003ad8f1d1",version,'STOPPED'))


if __name__ == "__main__":
    
    
    start_process()

    start_time = time.time()

    first_value = get_status("f440860b-018f-1000-ffff-ffffe17ecee8")

    while True:

        check_time = time.time()
        if (check_time - start_time) > 60*60:
            print("process time-out ...")
            break

        new_value =  get_status("f440860b-018f-1000-ffff-ffffe17ecee8")

        if first_value == new_value:
            print("Waiting ...")
            time.sleep(5)

        else:
            print("Terminating ...") 
            break   
