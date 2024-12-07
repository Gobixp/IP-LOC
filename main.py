import requests
import time
import sys
import os

# Warna ANSI untuk teks di terminal
COLORS = {
    "HEADER": "\033[95m",
    "OKBLUE": "\033[94m",
    "OKCYAN": "\033[96m",
    "OKGREEN": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
    "WHITE": "\033[97m",
    "GREY": "\033[90m",
}

# API Key untuk ipinfo.io
IPINFO_API_KEY = "8b72e48f3c346a"  # Pastikan API Key ini valid

# Fungsi untuk membersihkan layar terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan banner awal
def show_banner():
    banner = f"""{COLORS['OKGREEN']}\n
██╗██████╗       ██╗      ██████╗  ██████╗
██║██╔══██╗      ██║     ██╔═══██╗██╔════╝
██║██████╔╝█████╗██║     ██║   ██║██║     
██║██╔═══╝ ╚════╝██║     ██║   ██║██║     
██║██║           ███████╗╚██████╔╝╚██████╗
╚═╝╚═╝           ╚══════╝ ╚═════╝  ╚═════╝
                                           
{COLORS['ENDC']}"""

    # Media sosial dalam format tabel
    info = f"""{COLORS['OKCYAN']}
╔══════════════════════════════════════════════╗
║ Github   : https://github.com/wanzxploit     ║
║ Instagram: https://instagram.com/wanz_xploit ║
║ YouTube  : https://youtube.com/wanzxploit    ║
╚══════════════════════════════════════════════╝
{COLORS['ENDC']}"""

    print(banner)
    print(info)
    print("\n")

# Fungsi untuk mendapatkan data IP dari ipinfo.io
def get_ip_info(ip):
    try:
        url = f"https://ipinfo.io/{ip}?token={IPINFO_API_KEY}"
        response = requests.get(url)
        ip_data = response.json()

        if "error" in ip_data:
            return f"Error: {ip_data['error']}"

        return ip_data
    except Exception as e:
        return f"Error: Gagal mengambil data IP. Detail: {str(e)}"

# Fungsi untuk mencetak hasil IP dengan format tabel
def print_ip_info(ip_data):
    print(f"{COLORS['OKBLUE']}╔════════════════════════════════════════════╗")
    print(f"║            HASIL PELACAKAN IP              ║")
    print(f"╚════════════════════════════════════════════╝{COLORS['ENDC']}")

    print(f"{COLORS['OKCYAN']}KATEGORI{' ' * 6}INFORMASI")
    print(f"{COLORS['OKCYAN']}-----------------------------------------------{COLORS['ENDC']}")

    # Menyusun tabel dengan format sederhana
    table = f"""
 IP                  {COLORS['OKGREEN']}{ip_data.get('ip', 'N/A')}{COLORS['ENDC']}
 Negara              {COLORS['OKGREEN']}{ip_data.get('country', 'N/A')}{COLORS['ENDC']}
 Provinsi            {COLORS['OKGREEN']}{ip_data.get('region', 'N/A')}{COLORS['ENDC']}
 Kota/Kabupaten      {COLORS['OKGREEN']}{ip_data.get('city', 'N/A')}{COLORS['ENDC']}
 Hostname            {COLORS['OKGREEN']}{ip_data.get('hostname', 'N/A')}{COLORS['ENDC']}
 ISP                 {COLORS['OKGREEN']}{ip_data.get('org', 'N/A')}{COLORS['ENDC']}
 Timezone            {COLORS['OKGREEN']}{ip_data.get('timezone', 'N/A')}{COLORS['ENDC']}
 Lokasi Geografis    {COLORS['OKGREEN']}{ip_data.get('loc', 'N/A')}{COLORS['ENDC']}
    """
    print(f"{COLORS['WHITE']}{table}{COLORS['ENDC']}")
    print(f"{COLORS['OKCYAN']}-----------------------------------------------{COLORS['ENDC']}")

# Fungsi untuk menampilkan animasi loading
def loading_animation():
    animation = ["|", "/", "-", "\\"]
    for _ in range(10):  # Ulangi animasi 10 kali
        for frame in animation:
            sys.stdout.write(f"\r{COLORS['GREY']} Melacak IP... {frame}{COLORS['ENDC']}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

# Fungsi utama untuk menjalankan program
def main():
    # Membersihkan layar terminal sebelum menjalankan program
    clear()

    # Menampilkan banner awal
    show_banner()

    # Meminta pengguna memasukkan IP
    ip = input(f"{COLORS['OKCYAN']}{COLORS['BOLD']}Masukkan IP yang ingin dilacak: {COLORS['ENDC']}").strip()
    print("\n")

    # Menampilkan animasi loading
    loading_animation()

    # Ambil informasi IP dan tampilkan hasil
    ip_data = get_ip_info(ip)
    if isinstance(ip_data, dict):
        print_ip_info(ip_data)
    else:
        print(f"{COLORS['FAIL']}{ip_data}{COLORS['ENDC']}")
    
    print(f"{COLORS['OKGREEN']} Tools IP-LOC By Wanz Xploit.{COLORS['ENDC']}")
    print("\n")

if __name__ == "__main__":
    main()