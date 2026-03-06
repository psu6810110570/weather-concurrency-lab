import requests
import time
import threading

# ข้อมูลพิกัดเมือง 5 เมืองสำหรับดึงอุณหภูมิ
CITIES = [
    {"name": "Bangkok", "lat": 13.75, "lon": 100.50},
    {"name": "Tokyo", "lat": 35.68, "lon": 139.69},
    {"name": "London", "lat": 51.50, "lon": -0.12},
    {"name": "New York", "lat": 40.71, "lon": -74.00},
    {"name": "Sydney", "lat": -33.86, "lon": 151.20}
]

def fetch_weather(city):
    # ฟังก์ชันดึงข้อมูลสภาพอากาศ 1 เมือง
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&current_weather=true"
    
    response = requests.get(url)
    data = response.json()
    
    temp = data["current_weather"]["temperature"]
    print(f"[Thread] {city['name']} อุณหภูมิ: {temp}°C")

def main():
    print("เริ่มดึงข้อมูลด้วย Threading...")
    start_time = time.time()
    
    threads = []
    
    # Thread สำหรับแต่ละเมือง
    for city in CITIES:
        t = threading.Thread(target=fetch_weather, args=(city,))
        threads.append(t)
        t.start()
        
    #รอให้ทุก Thread ทำงานเสร็จ
    for t in threads:
        t.join()
        
    end_time = time.time()
    print(f"ใช้เวลาทั้งหมด: {end_time - start_time:.4f} วินาที")

if __name__ == "__main__":
    main()