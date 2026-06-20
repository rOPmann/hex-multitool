from core.display import csh, clear_all, print_banner, get_config, save_config
import os, time




loading_screen = True
userLoginName = os.getlogin()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))




schemes = ["red_to_white", "green_to_white", "blue_to_white", "purple_to_blue", "purple_to_red"]




def options_menu():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            cfg = get_config()
            print_banner()
            print(csh("┌────────────────────────────┐"))
            print(csh(f"│ (01) > Loading Screen: {'ON ' if cfg['loading_screen'] else 'OFF'} │"))
            print(csh("│ (02) > Color Scheme        │"))
            print(csh("│ (03) > Restart Tool        │"))
            print(csh("├────────────────────────────┤"))
            print(csh("│ (99) > Back to Home        │"))
            print(csh("└────────────────────────────┘"))

            print()

            try:
                c = int(input(csh(f"{userLoginName}@options ~# ").strip()))
            except ValueError:
                continue

            if c == 1:
                cfg["loading_screen"] = not cfg["loading_screen"]
                save_config(cfg)
                print(csh(f"Loading Screen set to {'ON' if cfg['loading_screen'] else 'OFF'}"))
                time.sleep(1.5)

            elif c == 2:

            
                while True:
                    clear_all()
                    print_banner()
                    print("\n\n")
                    cfg = get_config()
                    current = cfg.get("color_scheme", "red_to_white")

                    scheme_list = [
                        ("red_to_white",   "Red"),
                        ("green_to_white", "Green"),
                        ("blue_to_white",  "Blue"),
                        ("purple_to_red",  "Pink"),
                        ("rainbow",  "Rainbow"),
                        ("red_to_yellow",  "Fire"),
                        ("blue_to_cyan",  "Ocean"),
                        ("purple_to_blue",  "Galaxy"),
                        ("green_to_cyan",  "Matrix"),
                        ("red_to_black",  "Blood"),
                        
                    ]


                    


                    print(csh("┌────────────────────────────────┐"))
                    for i, (key, name) in enumerate(scheme_list):
                        check = "     ✔" if key == current else "  "
                        line = f"│ ({i+1:02d}) > {name}{check}"
                        line = line.ljust(31) + "  │"
                        print(csh(line))
                    print(csh("│────────────────────────────────│"))
                    print(csh("│ (80) > Default Terminal        │"))
                    print(csh("│────────────────────────────────│"))
                    print(csh("│ (99) > Back                    │"))
                    print(csh("└────────────────────────────────┘"))
                    print()

                    try:
                        choice = int(input(csh(f"Color (1-10): ")).strip())
                        
                        if 1 <= choice <= 10:
                            cfg["color_scheme"] = scheme_list[choice - 1][0]
                            save_config(cfg)
                            print(csh(f"Color changed to {scheme_list[choice - 1][1]}"))
                            time.sleep(1.5)
                            
                        elif choice == 99:
                            break
                        elif choice == 80:
                            cfg["color_scheme"] = "none"
                            save_config(cfg)
                            print(csh("Color changed to Default Terminal"))
                            time.sleep(1.5)
                            
                        else:
                            print(csh("Invalid Number"))
                    except ValueError:
                        pass
                    except KeyboardInterrupt:
                        break
            

            elif c == 3:
                from main import loading_screen
                from main import main_loop
                print(csh("Restarting..."))
                time.sleep(1.5)
                clear_all()
                main_loop()
                break

            elif c == 99:
                break
        except ValueError:
            continue
        except KeyboardInterrupt:
            break
