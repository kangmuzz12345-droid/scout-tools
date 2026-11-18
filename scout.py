import os
import subprocess
import platform
import random
import string
import urllib.request
import hashlib
import shutil

def clear_screen():
    os.system('clear')

def cek_sistem():
    print("\n--- [ Cek Sistem & IP Info ] ---")
    print(f"[+] Sistem Operasi : {platform.system()} {platform.release()}")
    print(f"[+] Arsitektur     : {platform.machine()}")
    print(f"[+] Python Version : {platform.python_version()}")
    try:
        external_ip = urllib.request.urlopen('https://api.ipify.org', timeout=5).read().decode('utf8')
        print(f"[+] IP Publik Anda : {external_ip}")
    except Exception:
        print("[-] Gagal mendeteksi IP Publik (Cek koneksi internet)")

def speedtest_dummy():
    print("\n--- [ Run Network Speedtest ] ---")
    print("[*] Menjalankan ping test ke 8.8.8.8...")
    os.system('ping -c 4 8.8.8.8')

def whois_lookup():
    print("\n--- [ Target WHOIS & IP Lookup ] ---")
    target = input("Masukkan IP/Domain target: ").strip()
    if target:
        os.system(f"whois {target}")

def ssl_checker():
    print("\n--- [ Check SSL/TLS Certificate ] ---")
    domain = input("Masukkan domain (cth: google.com): ").strip()
    if domain:
        os.system(f"openssl s_client -connect {domain}:443 -servername {domain}")

def pass_generator():
    print("\n--- [ Password & API Key Generator ] ---")
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(chars) for _ in range(16))
    print(f"[+] Generated Password: {pwd}")

def subdomain_finder():
    print("\n--- [ Subdomain Finder (Recon) ] ---")
    print("[*] Fitur placeholder subdomain finder.")

def web_header():
    print("\n--- [ Web Status & Header Checker ] ---")
    url = input("Masukkan URL (cth: https://google.com): ").strip()
    if url:
        os.system(f"curl -I {url}")

def text_binary_converter():
    print("\n--- [ Text to Binary & Binary to Text Converter ] ---")
    print("1. Text ke Biner (ASCII)")
    print("2. Biner ke Text")
    pilih = input("Pilih (1/2): ").strip()
    if pilih == '1':
        teks = input("Masukkan teks: ")
        biner = ' '.join(format(ord(char), '08b') for char in teks)
        print(f"Hasil Biner:\n{biner}")
    elif pilih == '2':
        biner = input("Masukkan kode biner (pisahkan spasi): ").strip()
        try:
            teks = ''.join([chr(int(b, 2)) for b in biner.split()])
            print(f"Hasil Teks:\n{teks}")
        except Exception as e:
            print(f"[-] Format biner tidak valid! ({e})")
    else:
        print("[-] Pilihan tidak valid.")

def port_scanner():
    print("\n--- [ Security Port Scanner ] ---")
    host = input("Masukkan IP/Host target: ").strip()
    if host:
        os.system(f"nmap -F {host}")

def hash_generator():
    print("\n--- [ Hash & Base64 Generator ] ---")
    text = input("Masukkan teks untuk di-hash: ").encode()
    if text:
        print(f"MD5    : {hashlib.md5(text).hexdigest()}")
        print(f"SHA256 : {hashlib.sha256(text).hexdigest()}")

def ram_analyzer():
    print("\n--- [ Process & RAM Analyzer (Native Termux) ] ---")
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
        mem_info = {}
        for line in lines:
            parts = line.split(':')
            if len(parts) == 2:
                key = parts[0].strip()
                val = parts[1].strip().split()[0]
                mem_info[key] = int(val)
        
        total_kb = mem_info.get('MemTotal', 0)
        free_kb = mem_info.get('MemFree', 0)
        buffers_kb = mem_info.get('Buffers', 0)
        cached_kb = mem_info.get('Cached', 0)
        
        available_kb = free_kb + buffers_kb + cached_kb
        used_kb = total_kb - available_kb
        
        total_mb = total_kb / 1024
        used_mb = used_kb / 1024
        available_mb = available_kb / 1024
        
        print(f"[+] Total RAM : {total_mb:.2f} MB")
        print(f"[+] Terpakai  : {used_mb:.2f} MB ({(used_mb/total_mb)*100:.1f}%)")
        print(f"[+] RAM Bebas : {available_mb:.2f} MB")
    except Exception as e:
        print(f"[-] Gagal membaca data RAM: {e}")

    try:
        print("\n[*] 10 Proses Teratas di Termux/Android:")
        result = subprocess.run(['ps', '-ef'], stdout=subprocess.PIPE, text=True)
        lines_ps = result.stdout.splitlines()
        for l in lines_ps[:11]:
            print(l)
            
        pilih_kill = input("\nIngin mematikan PID proses tertentu? (y/n): ").strip().lower()
        if pilih_kill == 'y':
            target_pid = input("Masukkan PID target: ").strip()
            if target_pid.isdigit():
                os.system(f"kill -9 {target_pid}")
                print(f"[+] Sinyal kill dikirim ke PID {target_pid}")
            else:
                print("[-] PID tidak valid!")
    except Exception as e:
        print(f"[-] Gagal membaca proses: {e}")

def file_manager():
    print("\n--- [ File Manager Utility (Copy, Move, Delete) ] ---")
    print("1. Salin / Copy (File atau Folder)")
    print("2. Pindah / Move (File atau Folder)")
    print("3. Hapus / Delete (File atau Folder)")
    pilih = input("Pilih Sub-Menu (1-3): ").strip()
    
    if pilih == '1':
        src = input("[?] Path asal (File/Folder): ").strip()
        dst = input("[?] Path tujuan (File/Folder): ").strip()
        if os.path.exists(src):
            try:
                if os.path.isdir(src):
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    shutil.copy2(src, dst)
                print(f"[+] Berhasil menyalin: {src} -> {dst}")
            except Exception as e:
                print(f"[-] Gagal menyalin: {e}")
        else:
            print("[-] Path asal tidak ditemukan!")
            
    elif pilih == '2':
        src = input("[?] Path asal (File/Folder): ").strip()
        dst = input("[?] Path tujuan: ").strip()
        if os.path.exists(src):
            try:
                shutil.move(src, dst)
                print(f"[+] Berhasil memindahkan: {src} -> {dst}")
            except Exception as e:
                print(f"[-] Gagal memindahkan: {e}")
        else:
            print("[-] Path asal tidak ditemukan!")
            
    elif pilih == '3':
        target = input("[?] Path file/folder yang mau dihapus: ").strip()
        if os.path.exists(target):
            try:
                if os.path.isdir(target):
                    shutil.rmtree(target)
                    print(f"[+] Berhasil menghapus folder beserta isinya: {target}")
                else:
                    os.remove(target)
                    print(f"[+] Berhasil menghapus file: {target}")
            except Exception as e:
                print(f"[-] Gagal menghapus: {e}")
        else:
            print("[-] Path tidak ditemukan!")
    else:
        print("[-] Pilihan tidak valid!")

def main():
    while True:
        clear_screen()
        print("==================================================")
        print("     SCOUT INTERACTIVE TOOL v10.3 (Termux Edition)")
        print("       System & Network Utility Script by Bro Scout")
        print("==================================================")
        print("1. Cek Sistem & IP Info")
        print("2. Run Network Speedtest")
        print("3. Target WHOIS & IP Lookup")
        print("4. Check SSL/TLS Certificate")
        print("5. Password & API Key Generator")
        print("6. Subdomain Finder (Recon)")
        print("7. Web Status & Header Checker")
        print("8. Converter Text <-> Binary")
        print("9. Security Port Scanner")
        print("10. Hash & Base64 Generator")
        print("11. Background Process & RAM Analyzer")
        print("12. File Manager (Copy, Move, Delete)")
        print("0. Keluar")
        print("--------------------------------------------------")
        
        pilihan = input("Pilih Menu (0-12): ").strip()
        
        if pilihan == '1':
            cek_sistem()
        elif pilihan == '2':
            speedtest_dummy()
        elif pilihan == '3':
            whois_lookup()
        elif pilihan == '4':
            ssl_checker()
        elif pilihan == '5':
            pass_generator()
        elif pilihan == '6':
            subdomain_finder()
        elif pilihan == '7':
            web_header()
        elif pilihan == '8':
            text_binary_converter()
        elif pilihan == '9':
            port_scanner()
        elif pilihan == '10':
            hash_generator()
        elif pilihan == '11':
            ram_analyzer()
        elif pilihan == '12':
            file_manager()
        elif pilihan == '0':
            print("\nKeluar dari program. Sampai jumpa!")
            break
        else:
            print("[-] Pilihan tidak valid!")
        
        input("\nTekan [ENTER] untuk kembali ke menu utama...")

if __name__ == "__main__":
    main()
import socket
from datetime import datetime

# Fungsi Port Scanner untuk disematkan ke menu scout.py
def jalankan_port_scanner():
    print("-" * 50)
    print("=== SECURITY PORT SCANNER (SCOUT TOOLS) ===")
    print("-" * 50)
    
    target_host = "127.0.0.1" # Bisa diubah sesuai target IP
    print(f"[*] Target Pemindaian : {target_host}")
    print(f"[*] Waktu Dimulai     : {str(datetime.now())}")
    print("-" * 50)

    try:
        port_umum = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]
        
        for port in port_umum:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            hasil = s.connect_ex((target_host, port))
            
            if hasil == 0:
                print(f"[+] Port {port} : TERBUKA (OPEN)")
            else:
                print(f"[-] Port {port} : Tertutup")
            s.close()
            
    except Exception as e:
        print(f"\n[!] Terjadi kesalahan: {e}")

    print("-" * 50)
    input("Tekan Enter untuk kembali ke menu utama...")
