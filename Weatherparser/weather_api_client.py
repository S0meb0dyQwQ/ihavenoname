import requests
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: Optional[float] = None
    temp_max: Optional[float] = None
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None


class Wind(BaseModel):
    speed: float
    deg: int
    gust: Optional[float] = None


class Clouds(BaseModel):
    all: int


class Rain(BaseModel):
    one_h: Optional[float] = Field(None, alias="1h")
    three_h: Optional[float] = Field(None, alias="3h")

    model_config = {"populate_by_name": True}


class Snow(BaseModel): 
    one_h: Optional[float] = Field(None, alias="1h")
    three_h: Optional[float] = Field(None, alias="3h")

    model_config = {"populate_by_name": True}


class Sys(BaseModel):
    type: Optional[int] = None
    id: Optional[int] = None
    country: Optional[str] = None
    sunrise: Optional[int] = None
    sunset: Optional[int] = None


class Coord(BaseModel):
    lon: float
    lat: float


class WeatherResponse(BaseModel):
    coord: Coord
    weather: List[Weather]
    base: Optional[str] = None
    main: Main
    visibility: Optional[int] = None
    wind: Wind
    clouds: Clouds
    rain: Optional[Rain] = None
    snow: Optional[Snow] = None
    dt: int
    sys: Sys
    timezone: Optional[int] = None
    id: int
    name: str
    cod: int

class Client:
    BASE_URL = "https://api.openweathermap.org/data/2.5"

    def __init__(self, api_key: str, units: str = "metric", lang: str = "ru"):
        
        if not api_key:
            raise ValueError("API cannot be empty")
        self.api_key = api_key
        self.units = units
        self.lang = lang
        self.session = requests.Session()

    def _get(self, endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
        
        params.update({
        "appid": self.api_key,
        "units": self.units,
        "lang": self.lang,
        })
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def get_current_weather(self,
        city: Optional[str] = None,
        lat: Optional[float] = None,
        lon: Optional[float] = None) -> WeatherResponse:
        
        params: Dict[str, Any] = {}
        if city:
            params["q"] = city
        elif lat is not None and lon is not None:
            params["lat"] = lat
            params["lon"] = lon
        else:
            raise ValueError("Give me 'city' or 'lat/lon'")
        data = self._get("weather", params)
        return WeatherResponse(**data)

API_KEY = input("Enter ur key (do not tell ur key to strangers)")
city = input("Where do u want to know weather now?")
client = Client(API_KEY,"metric","ru")
weather = client.get_current_weather(city)
print(f"City: {weather.name}, {weather.sys.country}")
print(f"Temp: {weather.main.temp} °C")
print(f"Feels like (hell): {weather.main.feels_like} °C")
print(f"Description: {weather.weather[0].description}")
print(f"Humidity: {weather.main.humidity}%")
print(f"Wind: {weather.wind.speed} м/с, {weather.wind.deg}°")
