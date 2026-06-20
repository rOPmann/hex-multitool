import requests
from core.display import csh

def server_info():
    try:
        inv = input(csh("Invite Link/Code: ")).strip()
        c = inv.split("/")[-1] if "/" in inv else inv

        print()
        r = requests.get(f"https://discord.com/api/v9/invites/{c}")
        
        if r.status_code == 200:
            d = r.json()
            g = d.get("guild", {})
            print(csh("─────────────────────────────"))
            print(csh(f"Name     : {g.get('name')}"))
            print(csh(f"ID       : {g.get('id')}"))
            print(csh(f"Members  : {d.get('approximate_member_count', 'N/A')}"))
            print(csh(f"Online   : {d.get('approximate_presence_count', 'N/A')}"))
            if "inviter" in d:
                i = d["inviter"]
                print(csh(f"Inviter  : {i.get('username')} ({i.get('id')})"))
            print(csh("─────────────────────────────"))
        else:
            print(csh(f"[!] Invalid invite. ({r.status_code})"))

        print()
        input(csh("[Enter] back ..."))
    except KeyboardInterrupt:
        return


def bot_invite_gen():
    try:
        bid = input(csh("Bot ID: ")).strip()
        link = f"https://discord.com/oauth2/authorize?client_id={bid}&scope=bot&permissions=8"
        print()
        print(csh(f"Link: {link}"))
        print()
        open_it = input(csh("Open in Browser? (y/n): ")).strip().lower()
        if open_it == "y":
            import webbrowser
            webbrowser.open(link)

        
        input(csh("[Enter] back ..."))
    except KeyboardInterrupt:
        return