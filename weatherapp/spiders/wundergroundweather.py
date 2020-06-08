# -*- coding: utf-8 -*-
import scrapy
import json
import ast


class WundergroundweatherSpider(scrapy.Spider):
    name = 'wundergroundweather'
    allowed_domains = ['www.wunderground.com']

    def __init__(self, geocode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geocodes = ast.literal_eval(geocode)
        

    def start_requests(self):
        for geocode in self.geocodes:
            yield scrapy.Request(
                url="https://api.weather.com/v3/wx/forecast/hourly/15day?apiKey=6532d6454b8aa370768e63d6ba5a832e&geocode={0}{1}{2}&units=e&language=en-US&format=json".format(geocode[0],"%2C",geocode[1]))
    
    def parse(self, response):
        tree = json.loads(response.body)
        yield { 
            'validTimeLocal' : tree.get('validTimeLocal'),
            'cloudCover' : tree.get('cloudCover'),
            'dayOfWeek' : tree.get('dayOfWeek'),
            'dayOrNight' : tree.get('dayOrNight'),
            'pressureMeanSeaLevel' : tree.get('pressureMeanSeaLevel'),
            'qpf' : tree.get('qpf'),
            'qpfSnow' : tree.get('qpfSnow'),
            'relativeHumidity' : tree.get('relativeHumidity'),
            'temperature' : tree.get('temperature'),
            'temperatureDewPoint' : tree.get('temperatureDewPoint'),
            'visibility' : tree.get('visibility'),
            'windSpeed' : tree.get('windSpeed'),
            'windDirection' : tree.get('windDirection'),
            'windGust' : tree.get('windGust'),
            'wxPhraseLong' : tree.get('wxPhraseLong'),
            'pressureMeanSeaLevel' : tree.get('pressureMeanSeaLevel'),
            'precipChance' : tree.get('precipChance'),
            'precipType' : tree.get('precipType'),
            'geocode' : self.geocodes
            }


