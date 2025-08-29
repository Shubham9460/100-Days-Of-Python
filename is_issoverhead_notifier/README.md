# 🚀 ISS Overhead Notifier

This Python project sends you an **email notification** when the **International Space Station (ISS)** is passing overhead your location **at night** 🌌.  

---

## 📌 Features
- Tracks real-time ISS position using the [Open Notify API](http://api.open-notify.org/iss-now.json).  
- Checks if ISS is **within ±5° latitude/longitude** of your location.  
- Uses [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine **day or night**.  
- Sends an **email alert** when ISS is above and it’s night.  

---

## 🛠️ Tech Stack
- **Python 3**
- [requests](https://pypi.org/project/requests/) – for API calls  
- [smtplib](https://docs.python.org/3/library/smtplib.html) – for sending emails  
- [datetime](https://docs.python.org/3/library/datetime.html) – for time handling  

---

## ⚙️ Setup & Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/Shubham9460/100-Days-Of-Python/tree/main/issoverhead
   cd is_soverhead_notifier