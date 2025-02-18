import requests
import json

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1/current.json"
        self.favorites = []

    def get_weather(self, city):
        params = {
            'key': self.api_key,
            'q': city
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def add_favorite(self, city):
        self.favorites.append(city)
        return

    def view_favorite(self):
        if not self.favorites:
            print("No Favorites yet")
            return
        else:
            for i in range (0, len(self.favorites)):
                print(f"{self.favorites[i]}")
            return

    def save_favorite(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.favorites, file)
        print(f"Successfully saved to {filename}")

    def load_favorite(self, filename):
        try:
            with open (filename, 'r') as file:
                self.favorites = json.load(file)
            print(f"Favorites loaded from {filename}")
        except FileNotFoundError:
            print(f"No File Found with the name {filename}")

    def ui(self):
        while True:
            print(f"\n Welcome To Weather Application\n"
                f"\n [1]. Get Weather for City: "
                f"\n [2]. Add Favorite City: "
                f"\n [3]. View Favorite Cities: "
                f"\n [4]. Save Favorite Cities to File: "
                f"\n [5]. Load Favorite Cities From File: "
                f"\n [6]. Exit")
            choice = input("Enter Your Choice: ")
            if choice == "1":
                city = input("Enter A City: ")
                current_weather = self.get_weather(city)
                print(f"Current Temperature: {current_weather['current']['temp_c']}"
                      f"\nCurrent Condition: {current_weather['current']['condition']['text']}"
                      f"\n")
            elif choice == "2":
                city = input("Enter a City: ")
                weather.add_favorite(city)
                print(f"Succesfully Added to favorite: {city}")
            elif choice == "3":
                weather.view_favorite()
            elif choice == "4":
                filename = input("Enter Filename: ")
                weather.save_favorite(filename)
            elif choice == "5":
                filename = input("Enter Filename: ")
                weather.load_favorite(filename)
            elif choice == "6":
                print("Thank you!")
                pass
                break
            else:
                "Invalid Choice:"
                

    def main(self):
        weather.ui()
        # city = input("Enter A City")
        # weather_data = self.get_weather(city)
        # if weather_data:
        #     print(f"{weather_data['current']['temp_c']}")
        



if __name__ == "__main__":
    api_key = "5508cba1c0d343dfa2373257251802"
    weather = Weather(api_key)
    weather.main()