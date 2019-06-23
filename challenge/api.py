# Suppose we have an API running somewhere 
# that provide us the hability to make a DDoS
# attack in any system we want...

# Suppose an intern made two functions to
# access this API: post_ddos and get_ddos
# He is a total Python Noobie but he want
# us to help to unittest it.
# but we can't make any change in the code
# or the manager will find out that we are
# helping this guy :^(


import time
import requests
# Make a POST request to start the DDoS attack
def post_ddos(
    bank_name: str,
    retry_times: int = 4
):
    # Maybe our API is too busy with the DDoS
    # so we have to retry a few times...
    payload = {
        'bank': bank_name
    }
    for _ in range(retry_times):
        try:
            res = requests.post('http://127.0.0.1/api/ddos', json=payload)
            break
        except TimeoutError:
            # We have to sleep a little and continue
            time.sleep(5)
            continue
    if res.status_code != 200:
        return "Something is wrong with the API!", res.status_code
    return res.text, res.status_code


# Sometimes the manager wants some information about the process...
def get_ddos(
    bank_name: str
):
    # The payload is the same!
    payload = {
        'bank': bank_name
    }
    # TODO
    # Maybe I'll have to change how we make this request
    # Senior Eng. said that he will fix the SSL certificate
    # I have to be careful not to mess this up when I change it
    res = requests.get('http://127.0.0.1/api/ddos', json=payload)
    return res.text, res.status_code