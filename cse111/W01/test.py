def calculate_wind_chill(es_wind_speed, es_temperature):
wind_chill = 35.74 + (0.6215 * es_temperature) - (35.75 * (es_wind_speed ** 0.16)) + (0.4275 * es_temperature * (es_wind_speed ** 0.16))
return wind_chill  