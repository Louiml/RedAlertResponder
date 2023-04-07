import random
import time

def get_alarm_data():
    cities = ['Tel Aviv', 'Alumim', 'Yated', 'Jerusalem', 'Haifa', 'Be\'ersheba', 'Ashdod', 'Eilat', 'Ashkelon', 'Netanya', 'Sderot', 'Herzliya', 'Kiryat Gat']
    
    if random.random() < 0.1:
        alarm_data = {
            'city': random.choice(cities),
            'time': int(time.time()),
            'duration': random.randint(30, 120)
        }
        return alarm_data
    else:
        return None
