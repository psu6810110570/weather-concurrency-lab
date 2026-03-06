import asyncio
import httpx
import time

CITIES = [
    {"name": "Bangkok", "lat": 13.75, "lon": 100.50},
    {"name": "Tokyo", "lat": 35.68, "lon": 139.69},
    {"name": "London", "lat": 51.50, "lon": -0.12},
    {"name": "New York", "lat": 40.71, "lon": -74.00},
    {"name": "Sydney", "lat": -33.86, "lon": 151.20}
]

async def fetch_weather_async(client, city):
    # ฟังก์ชันดึงข้อมูลแบบ Asynchronous
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&current_weather=true&timezone=auto"
    
    start_req = time.time()
    # ใช้ await 
    response = await client.get(url)
    data = response.json()
    
    fetch_time = time.time() - start_req
    temp = data["current_weather"]["temperature"]
    local_time = data["current_weather"]["time"].replace("T", " ")
    
    print(f"[Async] {city['name']:<10} อุณหภูมิ: {temp}°C (เวลา: {local_time}) | ดึงเสร็จใน: {fetch_time:.4f} วินาที")

async def main():
    print("เริ่มดึงข้อมูลด้วย Asyncio...")
    start_time = time.time()
    
    async with httpx.AsyncClient() as client:
        tasks = [fetch_weather_async(client, city) for city in CITIES]
        await asyncio.gather(*tasks)
        
    print(f"ใช้เวลาทั้งหมด: {time.time() - start_time:.4f} วินาที")

if __name__ == "__main__":
    asyncio.run(main())