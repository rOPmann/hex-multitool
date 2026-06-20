import requests
from core.display import csh

def webhook_spammer():
    try:
        url = input(csh("Webhook URL: ")).strip()
        msg = input(csh("Webhook Message: ")).strip()
        amount = int(input(csh("Amount: ")).strip())

        try:
            for i in range(amount):
                requests.post(url, json={"content": msg})
                print(csh(f"Sent: {i+1}/{amount}"), end='\r')
        except KeyboardInterrupt:
            print(csh(f"\nStopped. Sent: {i+1}"))
        
        input(csh("\n[Enter] back ..."))
    except KeyboardInterrupt:
        pass


    

        



def webhook_delete():
    try:
        url = input(csh("Webhook URL: ").strip())
        
        try:
            r = requests.delete(url)
            if r.status_code == 204:
                print(csh("Webhook deleted!"))
            else:
                print(csh(f"Error: {r.status_code}"))
        except KeyboardInterrupt:
            pass
        
        input(csh("[Enter] back ..."))
    except KeyboardInterrupt:
        pass