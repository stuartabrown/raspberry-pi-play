# import dateutil.parser
import untangle
# from datetime import datetime, timedelta
data = untangle.parse('forecast.xml')
# print(data.weatherdata.location.name.cdata.strip())

for forecast in data.weatherdata.forecast.tabular:
#   print (data.weatherdata.forecast.tabular.time.temperature['value'])
#   print (forecast.temperature['value'])
  print (forecast.time['from'])

    # forecast_data = { 'from' : int(time.mktime(dateutil.parser.parse(forecast['from']).timetuple())),
    #                     'to' : int(time.mktime(dateutil.parser.parse(forecast['to']).timetuple())),
    #                     'weather' : forecast.symbol['name'],
    #                     'rain' : float(forecast.precipitation['value']),
    #                     'humidity' : 0.0,
    #                     'wind_direction' : forecast.windDirection['name'],
    #                     'wind_speed' : float(forecast.windSpeed['mps']),
    #                     'temperature' : float(forecast.temperature['value']),
    #                     'pressure' : float(forecast.pressure['value'])
    #                 }

# book = data.book
# print (book)

# chapter = data.book.chapter
# print (chapter)

# print (data.book.chapter['id'])
# print (data.book.chapter[0].title.cdata.strip())
# print (data.book.chapter[1].title)

# title = data.book.chapter.title
# print (title)

# COUNT = [0,1]
# for TICK in COUNT:
#   print(data.book.chapter[TICK])