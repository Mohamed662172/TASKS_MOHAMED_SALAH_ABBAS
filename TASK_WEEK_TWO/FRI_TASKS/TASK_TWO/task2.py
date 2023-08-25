import requests

class ActivitySuggestor:
    def __init__(self):
        self.activity_url = "https://www.boredapi.com/api/activity"
        self.ip_url = "https://api.ipify.org/?format=json"
        self.location_url = "https://ipinfo.io"

    def fetch_activity(self):
        
            response = requests.get(self.activity_url)
            if response.status_code == 200:
                data = response.json()
                activity = data.get("activity")
                if activity:
                    return activity
                else:
                    return "No activity suggestion available."
            else:
                return "Failed to retrieve activity suggestion."
       

    def fetch_public_ip(self):
       
            response = requests.get(self.ip_url)
            if response.status_code == 200:
                data = response.json()
                public_ip = data.get("ip")
                if public_ip:
                    return f"Your Public IP Address: {public_ip}"
                else:
                    return "Unable to retrieve public IP."
            else:
                return "Failed to retrieve public IP."
        

    def fetch_location(self):
        
            response = requests.get(self.location_url)
            if response.status_code == 200:
                data = response.json()
                location = data.get("city")
                if location:
                    return f"Your Location: {location}"
                else:
                    return "Unable to retrieve location."
            else:
                return "Failed to retrieve location."
       

if __name__ == "__main__":
    activity_suggestor = ActivitySuggestor()

    suggested_activity = activity_suggestor.fetch_activity()
    print("Suggested Activity:", suggested_activity)

    public_ip = activity_suggestor.fetch_public_ip()
    print(public_ip)

    location = activity_suggestor.fetch_location()
    print(location)
