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
    """ฟังก์ชันดึงข้อมูลสภาพอากาศ 1 เมือง"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&current_weather=true&timezone=auto"
    
    # เริ่มจับเวลาเฉพาะของเมืองนี้
    start_req = time.time() 
    
    response = requests.get(url)
    data = response.json()
    
    # จบจับเวลา
    end_req = time.time()
    fetch_time = end_req - start_req
    
    temp = data["current_weather"]["temperature"]
    local_time = data["current_weather"]["time"].replace("T", " ") 
    
    print(f"[Thread] {city['name']:<10} อุณหภูมิ: {temp}°C (เวลา: {local_time}) | ดึงข้อมูลเสร็จใน: {fetch_time:.4f} วินาที")

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