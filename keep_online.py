import os
import time
import requests
import threading

RENDER_URL = os.getenv("RENDER_URL", "https://stay-in-vc.onrender.com")
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "600"))
PING_PATH = os.getenv("PING_PATH", "/ping")


def ping_service():
    url = f"{RENDER_URL.rstrip('/')}{PING_PATH}"
    while True:
        try:
            response = requests.get(url, timeout=10)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Pinged {url}: {response.status_code}")
        except Exception as e:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failed to ping {url}: {e}")
        time.sleep(PING_INTERVAL)


def start_pinger():
    thread = threading.Thread(target=ping_service, daemon=True)
    thread.start()


if __name__ == "__main__":
    ping_service()
