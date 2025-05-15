<h1 align="center">🌍 IP Changer - v1.0</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green?style=for-the-badge&logo=linux" />
  <img src="https://img.shields.io/badge/Made%20With-Tor-orange?style=for-the-badge&logo=tor" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=2000&color=00FF00&center=true&vCenter=true&width=500&lines=AutoIPchange+Tool;by+Ariyan+Rabbi+(Dʌʀĸ-Nɘt);IP+Sensor+Activated;Live+IP+Switching;Stay+Anonymous;Change+Your+IP+Every+X+Minutes" alt="Typing SVG" />
</p>

---

# ⚙️ AutoIPchange.py – Tor-Based Auto IP Changer

**Change your IP address automatically every X minutes using the TOR network.**  
Ideal for ethical hackers, privacy-lovers, and anonymity fans. Use responsibly.

---

## 🧠 Features:
- ✅ Automatically changes IP address using TOR
- ⏱️ You choose the interval (e.g. every 2, 5, or 10 minutes)
- 🌐 Shows IP before and after change
- 💻 Works on Termux & Linux
- 🎨 Stylish terminal interface with colors
- 🧩 Light, fast, and efficient

---

## ⚙️ Installation & Usage

### 📱 Termux Commands:

```bash
pkg update && pkg upgrade -y
pkg install python tor -y
pip install stem requests colorama pyfiglet
git clone https://github.com/DARK-NET-403/AutoIPchange
cd AutoIPchange
nano torrc
```

> Paste this in `torrc`:
```
ControlPort 9051
HashedControlPassword <your_hashed_password>
```

> Generate hashed password:
```bash
tor --hash-password yourpassword
```

```bash
tor &
python AutoIPchange.py
```

---

### 💻 Linux (Ubuntu/Kali) Commands:

```bash
sudo apt update && sudo apt install python3 tor -y
pip install stem requests colorama pyfiglet
git clone https://github.com/DARK-NET-403/AutoIPchange
cd AutoIPchange
sudo nano /etc/tor/torrc
```

> Add this at the end of the file:
```
ControlPort 9051
HashedControlPassword <your_hashed_password>
```

```bash
sudo service tor start
python3 AutoIPchange.py
```

---

## 👨‍💻 Developer Info:
**Ariyan Rabbi (Dʌʀĸ-Nɘt)**  
- [Facebook](https://facebook.com/share/12Ju91Lznxb/)  
- [Telegram](https://t.me/DARK_NET_40)  
- [GitHub](https://github.com/DARK-NET-403)

---

## ⚠️ Disclaimer:
> This tool is for **educational purposes only**. Misuse is strictly prohibited. Use it responsibly and legally.

---

## ⭐ Star this repo to support my work!
