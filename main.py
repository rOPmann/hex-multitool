import os, sys, ctypes, webbrowser, time
from modules.sysinfo import sysinfo
from modules.webhook import webhook_delete, webhook_spammer
from core.display import csh, print_banner, print_banner2, clear_all, hide_cursor, show_cursor, get_config
from modules.vuln_scanner import dir_scanner
from modules.discord_tools import server_info, bot_invite_gen
from modules.toolinfo import toolinfo
from modules.options import options_menu
from modules.lookup import whois_lookup, phone_lookup, ip_lookup, dns_lookup
from modules.qrcode import generate_qrcode



# create Terminal
os.system("mode con: cols=120 lines=40")
userLoginName = os.getlogin()
tool_version = "vb1.0"
ctypes.windll.kernel32.SetConsoleTitleW(f"*Hex @ {userLoginName} ~ {tool_version}")



# slow typing print func
def type_print(text, delay=0.03):
    sys.stdout.write(csh( "  [*] "))
    [ (sys.stdout.write(csh(c)), sys.stdout.flush(), time.sleep(delay)) for c in text ]
    sys.stdout.write("\n")



# loading screen 
def loading_screen():
    clear_all()
    cfg = get_config()
    if not cfg.get("loading_screen"):
        return
    print("Loading Hex Framework... ")
    time.sleep(2)
    hide_cursor()
    for _ in range(3):
        
        clear_all()
        print_banner2("\033[1;37m") # white banner
        time.sleep(0.2)

        clear_all()
        print_banner() # red banner
        time.sleep(0.2)
    
    print("\n\n\n\n\n\n\n")
    show_cursor()
    time.sleep(1)
    
    type_print(f"Booting Hex OS [ User: {userLoginName} ]", 0.03)
    type_print("Connecting to the Hell...", 0.03)
    type_print("Initializing Hex Protocol... ", 0.03)
    print("\n\n")
    type_print(f"Synchronizing interface with terminal... Hex {tool_version}", 0.03)
    time.sleep(1.7)



# home loop

def home_loop():
    clear_all()
    print_banner()
    print("\n\n")

    top    = "┌────────────────────────────┐"
    bottom = "└────────────────────────────┘"
    gap    = "  "

    left_box = [
        "│         MALICIOUS          │",
        "│ (01) > Discord Tools       │",
        "│ (02) > Ip Grabber          │",
        "│ (03) > Vuln Scanner        │",
        "│ (04) > QrCode Generator    │",
    ]

    middle_box = [
        "│           OSINT            │",
        "│ (05) > Phone Lookup        │",
        "│ (06) > Whois Lookup        │",
        "│ (07) > DNS Lookup          │",
        "│ (08) > IP Lookup           │",
    ]

    right_box = [
        "│          SYS/GEN           │",
        "│ (80) > Systeminformation   │",
        "│ (81) > Tool Info           │",
        "│ (82) > Options             │",
        "│ (99) > Exit Program        │",
    ]

    top = "┌────────────────────────────┐"
    bottom = "└────────────────────────────┘"
    gap = "  "

    width = os.get_terminal_size().columns
    block_width = len(top + gap + top + gap + top)
    pad = " " * ((width - block_width) // 2)

    print(csh(pad + top + gap + top + gap + top))

    for l, m, r in zip(left_box, middle_box, right_box):
        print(csh(pad + l + gap + m + gap + r))

    print(csh(pad + bottom + gap + bottom + gap + bottom))
    print("\n\n")



# main
def main_loop():
    loading_screen()
    try:
        while True:
            home_loop()
            try:
                c = int(input(csh(f"{userLoginName}@hex ~# ").strip()))
            except ValueError:
                continue
            
            if c == 1:
                # didscord tools menu ----------------------
                clear_all()
                print_banner()
                print(csh("┌────────────────────────────┐"))
                print(csh("│ (01) > Webhook Tools       │"))
                print(csh("│ (02) > Server Info         │"))
                print(csh("│ (03) > Bot Invite Generator│"))
                print(csh("├────────────────────────────┤"))
                print(csh("│ (99) > Back to Home        │"))
                print(csh("└────────────────────────────┘"))
                
                try:
                    print()
                    ch = int(input(csh(f"{userLoginName}@dcTools ~# ").strip()))
                except ValueError:
                    continue
                except KeyboardInterrupt:
                    main_loop()

                
                if ch == 1:
                    try:
                        clear_all()
                        print_banner()
                        print(csh("┌────────────────────────────┐"))
                        print(csh("│ (01) > Webhook Spammer     │"))
                        print(csh("│ (02) > Delete Webhook      │"))
                        print(csh("├────────────────────────────┤"))
                        print(csh("│ (99) > Back to Home        │"))
                        print(csh("└────────────────────────────┘"))

                        try:
                            cho = int(input(csh(f"{userLoginName}@webhookTools ~# ").strip()))
                        except ValueError:
                            return
                        except KeyboardInterrupt:
                            return

                        if cho == 1:
                            webhook_spammer()

                        elif cho == 2:
                            webhook_delete()

                        elif cho == 99:
                            pass

                        else:
                            print(csh("Enter a valid option"))
                    except ValueError:
                        return
                    except KeyboardInterrupt:
                        return


                elif ch == 2:
                    server_info()

                elif ch == 3:
                    bot_invite_gen()

                elif ch == 99:
                    home_loop()

                else:
                    print(csh("Enter a valid option"))
                    
           
                
            elif c == 2:
                # ip grabber
                webbrowser.open("https://iplogger.org/")

            elif c == 3:
                # vuln scanner
                clear_all()
                dir_scanner()

            elif c == 4:
                # qrcode gen
                generate_qrcode()

            elif c == 5:
                clear_all()
                phone_lookup()


            elif c == 6:
                # whois lookup
                clear_all()
                whois_lookup()

            elif c == 7:
                # dns lookup
                clear_all()
                dns_lookup()

            elif c == 8:
                # ip lookup
                clear_all()
                ip_lookup()


            elif c == 80:
                # sysinfo menu
                # print("System Information")
                clear_all()
                sysinfo()
                input(csh("\n[Enter] back... "))


            elif c == 81:
                clear_all()
                toolinfo()
                

            elif c == 82:
                # options
                clear_all()
                options_menu()


            elif c == 99:
                clear_all()
                sys.exit()


            elif c == 0:
                # testing
                clear_all()
                type_print("Hello this is a test for my type print function", 0.03)
                input(csh("[Enter] back... "))
                
            else:
                pass
    except KeyboardInterrupt:
        clear_all()
        sys.exit()

if __name__ == "__main__":
    main_loop()