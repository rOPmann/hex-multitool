import requests, threading, queue, os, sys
from core.display import csh, print_banner, clear_all

def dir_scanner():

    try:
        clear_all()
        print_banner()
        print("\n\n")
        print(csh("┌────────────────────────────┐"))
        print(csh("│        VULN SCANNER        │"))
        print(csh("└────────────────────────────┘"))
        print()

        url = input(csh("  URL      : ")).strip()
        if not url.startswith("http"):
            url = "https://" + url


        
        threads = int(input(csh("  Threads  : ")).strip())
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        wordlist_path = os.path.join(ROOT_DIR, "..", "core", "wordlist.txt")
        print()
        print(csh(" (01) > Small Wordlist (200 Words)"))
        print(csh(" (02) > Big Wordlist (2000 Words)"))
        try:
            print()
            c = int(input(csh("(1/2) Small or Big Wordlist (default: small): ")).strip())
        except ValueError:
            print(csh(" [!] Error please enter a number"))
        except KeyboardInterrupt:
            return
        
        if c == 1:
            wordlist_path = os.path.join(ROOT_DIR, "..", "core", "wordlist.txt")
        elif c == 2:
            wordlist_path = os.path.join(ROOT_DIR, "..", "core", "wordlist2.txt")
        else:
            print(csh(" [!] Error please enter 1 or 2"))
            return

        q = queue.Queue()
        found = []
        count = [0]
        stop = threading.Event()

        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip()
                if word:
                    q.put(word)

        total = q.qsize()
        clear_all()
        print_banner()
        print("\n\n")
        print(csh(f"  Wordlist  : {total} entries loaded"))
        print(csh(f"  Target    : {url}"))
        print(csh(f"  Threads   : {threads}"))
        print()

        def worker():
            while not stop.is_set() and not q.empty():
                word = q.get()
                try:
                    r = requests.get(f"{url}/{word}", timeout=3)
                    count[0] += 1
                    if r.status_code == 200:
                        sys.stdout.write(f"\n{csh(f'  [+] FOUND  » {url}/{word}')}\n")
                        found.append(f"{url}/{word}")
                    else:
                        sys.stdout.write(f"\r{csh(f'  [-] {count[0]}/{total} » {word:<30}')}")
                        sys.stdout.flush()
                except:
                    pass

        thread_list = []
        for i in range(threads):
            t = threading.Thread(target=worker, daemon=True)
            t.start()
            thread_list.append(t)

        try:
            for t in thread_list:
                t.join()
        except KeyboardInterrupt:
            stop.set()

        print()
        print()
        print(csh(f"  ─────────────────────────────"))
        print(csh(f"  Gefunden : {len(found)}"))
        for item in found:
            print(csh(f"  [+] {item}"))
        print(csh(f"  ─────────────────────────────"))
        print()
        input(csh("  [Enter] back ..."))
    except KeyboardInterrupt:
        pass