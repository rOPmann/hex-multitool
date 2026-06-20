from core.display import clear_all, print_banner, csh

def toolinfo():
    try:
        clear_all()
        print_banner()
        print("\n\n")

        
        print(csh("┌────────────────────────────┐"))
        print(csh("│ Github:                    │"))
        print(csh("│ Developer: ;               │"))
        print(csh("│ Version: vb1.0             │"))
        print(csh("└────────────────────────────┘"))
        print("\n\n\n")

        input(csh("[Enter] for back... "))
    except KeyboardInterrupt:
        pass