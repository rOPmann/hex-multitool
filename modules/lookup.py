import phonenumbers, whois, requests, webbrowser, socket, pyperclip
from phonenumbers import carrier, geocoder
from core.display import csh, clear_all, print_banner

def trim(val, max_len=35):
    return val if len(val) <= max_len else val[:max_len] + "..."


def dns_lookup():
    clear_all()
    print_banner()
    print("\n\n")
    print(csh("┌────────────────────────────┐"))
    print(csh("│         DNS LOOKUP         │"))
    print(csh("└────────────────────────────┘"))
    print()

    try:
        dns_input = input(csh("Enter your Host (ex: google.com): ")).strip()
    except KeyboardInterrupt:
        return

    try:
        ip = socket.gethostbyname(dns_input)
    except socket.gaierror:
        print(csh(f" [!] ERROR: Dns could not be resolved"))
        input(csh("\n[Enter] back... "))
        return
    except Exception as e:
        print(csh(f" [!] ERROR: {e}"))
        input(csh("\n[Enter] back... "))
        return

    if not dns_input: return

    try:
        clear_all()
        print_banner()
        print("\n\n")

        res = {
            "IP": ip
        }

        print(csh(f"Domain: {str(dns_input)}"))
        print()
        print(csh("  ┌───────────────────────────┐"))
        for k, v in res.items():
            line = f"  │  {k:<5} : {v}"
            line = line.ljust(30) + "│"
            print(csh(line))
        print(csh("  └───────────────────────────┘"))

    except Exception as e:
        print(csh(f" [!] ERROR: {e}"))
    except KeyboardInterrupt:
        return

    print()
    c = input(csh(f"Copy IP ({ip}) to clipboard? (y/n) (default: n): ")).strip().lower()
    if c == "n" or c == "":
        pass
    elif c == "y":
        pyperclip.copy(ip)
        print(csh(f"\nIP ({ip}) successfuly saved to clipboard"))
    else:
        print(csh(" [!] ERROR: Please enter either (y/n)"))
    print()
    input(csh("[Enter] back... "))



def whois_lookup():
    clear_all()
    print_banner()
    print("\n\n")
    print(csh("┌────────────────────────────┐"))
    print(csh("│        WHOIS LOOKUP        │"))
    print(csh("└────────────────────────────┘"))
    print()

    try:
        domain_input = input(csh("Enter your domain (ex: google.com): ")).strip()
    except KeyboardInterrupt:
        return

    if not domain_input:
        return

    try:
        w = whois.whois(domain_input)
    except Exception as e:
        print(csh(f" [!] ERROR: {e}"))
        input(csh("\n[Enter] back... "))
        return

    if not w:
        return

    try:
        clear_all()
        print_banner()
        print("\n\n")

        domain_name = w.domain_name[0] if isinstance(w.domain_name, list) else w.domain_name

        res = {
            "Registrar"  : trim(str(w.registrar)),
            "Created"    : trim(str(w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date)),
            "Exp. Date"  : trim(str(w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date)),
            "Updated"    : trim(str(w.updated_date[0] if isinstance(w.updated_date, list) else w.updated_date)),
            "Server"     : trim(str(w.name_servers[0] if isinstance(w.name_servers, list) else w.name_servers)),
            "Country"    : trim(str(w.country)),
            "Org"        : trim(str(w.org)),
            "DNSSEC"     : trim(str(w.dnssec)),
        }

        print(csh(f"Domain: {str(domain_name)}"))
        print()
        print(csh("  ┌─────────────────────────────────────────────────────────┐"))
        for k, v in res.items():
            line = f"  │  {k:<13} : {v}"
            line = line.ljust(60) + "│"
            print(csh(line))
        print(csh("  └─────────────────────────────────────────────────────────┘"))

    except Exception as e:
        print(csh(f" [!] ERROR: {e}"))
    except KeyboardInterrupt:
        return

    print()
    input(csh("[Enter] back... "))


def phone_lookup():
    clear_all()
    print_banner()
    print("\n\n")
    print(csh("┌────────────────────────────┐"))
    print(csh("│        PHONE LOOKUP        │"))
    print(csh("└────────────────────────────┘"))
    print()

    try:
        c = input(csh("Enter your phone number (ex: +1 ...): ")).strip()
    except ValueError:
        return
    except KeyboardInterrupt:
        return
    
    if not c:
        return
    
    print()

    try:
        clear_all()
        print_banner()
        print("\n\n")
        p = phonenumbers.parse(c, None)
        valid = phonenumbers.is_valid_number(p)

        res = {
            "Valid": str(valid),
            "Region": phonenumbers.region_code_for_number(p),
            "Location": geocoder.description_for_number(p, "en"),
            "E164": phonenumbers.format_number(p, phonenumbers.PhoneNumberFormat.E164),
            "INTERNATIONAL": phonenumbers.format_number(p, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "NATIONAL": phonenumbers.format_number(p, phonenumbers.PhoneNumberFormat.NATIONAL),
            "Carrier": carrier.name_for_number(p, "en") or "unknown",
            "Type": "Mobile" if phonenumbers.number_type(p) == phonenumbers.PhoneNumberType.MOBILE else "Fixed",
            
        }

        
        

        print(csh(f"Number: [{c}]"))
        print()
        print(csh("  ┌───────────────────────────────────────┐"))
        for k, v in res.items():
            line = f"  │  {k:<13} : {v}"
            line = line.ljust(42) + "│"
            print(csh(line))
        print(csh("  └───────────────────────────────────────┘"))

    except Exception as e:
        print(csh(f" [!] ERROR: {e}"))
    except KeyboardInterrupt:
        return

    print()
    input(csh("[Enter] back... "))
    

def ip_lookup():
    clear_all()
    print_banner()
    print("\n\n")
    print(csh("┌───────────────────────────┐"))
    print(csh("│         IP LOOKUP         │"))
    print(csh("└───────────────────────────┘"))
    print()

    try:
        c = input(csh("Enter the IP (ex: 127.0.0.1): ")).strip()
    except KeyboardInterrupt:
        return
    
    print()
    try:

        clear_all()
        print_banner()
        print("\n\n")
        r = requests.get(f"http://ip-api.com/json/{c}", timeout=5)
        data = r.json()

        if data.get("status") == "fail":
            print(csh(f"  [!] Error: {data.get('message')}"))
            return
        
        maps_link = f"google.com/maps?q={data.get('lat')},{data.get('lon')}"

        res = {
            "IP"        : data.get("query"),
            "ISP"       : data.get("isp"),
            "Org"       : data.get("org"),
            "Country"   : data.get("country"),
            "City"      : data.get("city"),
            "Region"    : data.get("regionName"),
            "Zip"       : data.get("zip"),
            "Latitude"  : data.get("lat"),
            "Longitude" : data.get("lon"),
            "Timezone"  : data.get("timezone"),
            "GoogleMaps": maps_link,
        }


        print(csh(f"IP: [{c}]"))
        print()
        print(csh("  ┌───────────────────────────────────────────────────────┐"))
        for k, v in res.items():
            if k == "GoogleMaps" or k == "Country":
                print(csh("  ├───────────────────────────────────────────────────────┤"))
            line = f"  │  {k:<13} : {v}"
            line = line.ljust(58) + "│"
            print(csh(line))
        print(csh("  └───────────────────────────────────────────────────────┘"))

        print()
        ch = input(csh("Open Link in Google Maps (y/n) (default: n): ")).strip()
        if ch.upper() == "Y":
            webbrowser.open("https://www." + maps_link)
        else:
            pass


    except Exception as e:
        print(csh(f" [!] ERROR: {e}"))
        print()
        input(csh("[Enter] back... "))
    except KeyboardInterrupt:
        return

    print()
    input(csh("[Enter] back... "))


