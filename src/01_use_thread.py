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