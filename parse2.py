# import dateutil.parser
import untangle
# from datetime import datetime, timedelta
data = untangle.parse('forecast.xml')
# print(data.weatherdata.location.name.cdata.strip())

# for forecast in data.weatherdata.forecast.tabular.time:
# #   print (data.weatherdata.forecast.tabular.time.temperature['value'])
#   print (forecast.temperature['value'])
for forecast in data.weatherdata.forecast.tabular.time: 
#   print (forecast['from'], forecast.temperature['value'])
  print ("time is " + forecast['from'] + " and temperature  is " + forecast.temperature['value'])

# for forecast in data.weatherdata.forecast.tabular:
#   print (data.weatherdata.forecast.tabular.time.temperature['value'])
#   print(type(forecast))
#   print ("time is " + forecast.time[0]['from'])
#   print ("time is " + forecast.time['from'] + "and temperature  is " + forecast.time.temperature['value'])

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