import qrcode, os
from core.display import csh, clear_all, print_banner

def generate_qrcode():
    clear_all()
    print_banner()
    print("\n\n")

    print(csh("┌────────────────────────────┐"))
    print(csh("│      QR CODE GENERATOR     │"))
    print(csh("└────────────────────────────┘"))
    print()

    try:
        data = input(csh("Text/URL: ")).strip()
        if not data:
            return
        
        filename = input(csh("Filename (default 'qrcode'): ")).strip()
        if not filename: filename = "qrcode"
        if not filename.endswith(".png"): filename += ".png"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        image = qr.make_image(fill_color="black", back_color="white")
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ROOT_DIR = os.path.dirname(BASE_DIR)
        output_path = os.path.join(ROOT_DIR, "output", filename)

        # output ordner erstellen falls nicht vorhanden
        os.makedirs(os.path.join(ROOT_DIR, "output"), exist_ok=True)

        image.save(output_path)
        print()
        print(csh("──────────────────────────────────────────"))
        print(csh(f"  QRCode saved as: {filename}"))
        print(csh(f"  Saved in: {output_path}"))
        print(csh("──────────────────────────────────────────"))
    except KeyboardInterrupt:
        return
    except Exception as e:
        print(csh(f" [!] Error: {e}"))

    print()
    input(csh("[Enter] back... "))
