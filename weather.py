import pyowm
from pyowm.utils.config import get_default_config

class weather_information:

    def get_info(self, place):

        config_dict = get_default_config()
        config_dict['language'] = 'ru'  # your language here, eg. Portuguese

        owm = pyowm.OWM('53e1dec3517a7f5e30251ccbb9049d18', config_dict)
        mgr = owm.weather_manager()

        # place = input ("Введите название вашего местоположения(город): ")

        observation = mgr.weather_at_place(place)
        w = observation.weather

        temp = w.temperature('celsius')["temp"]
        hum = w.humidity
        wind = w.wind()["speed"]

        # print ("В городе " + place + " сейчас " + w.detailed_status)

        # На кой хуй надо непонятно
        '''w.get_detailed_status()
        w.wind()
        w.humidity()
        w.temperature('celsius')
        observation.get_weather()
        '''

        result = ''

        result += 'В этом городе сейчас ' + str(temp) + ' градусов Цельсия.\n' 
        result += 'Влажность равна ' + str(hum) + '\n'
        result += 'Скорость ветра ' + str(wind) + ' м/с\n'

        if temp > 40:
            result += 'Очень жарко. Советую не выходить сегодня на улицу. Но если есть необходимость наденьте легкую одежду, например тонкую майку с шортами. Также нужно много пить, дабы избежать обезвоживания.'
        elif 40 >= temp > 25:
            result += 'Очень тепло. Было бы неплохо провести день на пляже. Шорты и майка сейчас в самый раз.'
        elif 25 >= temp > 15:
            result += 'Умеренно тепло. Шорты и майка все еще актуальны, но на вечер было бы неплохо взять теплые вещи.'
        elif 15 >= temp > 0:
            result += 'Холодновато. Без осенней куртки выходить на улицу не советую, так как можно заболеть.'
        elif 0 >= temp > -15:
            result += 'Легкий мороз. Можно уже использовать зимние сапоги. Зимняя куртка также должна стать неотъемлемой частью гардероба.'
        elif -15 >= temp > -25:
            result += 'Достаточно холодно. Подштанники уже необходимы. В остальном придерживайтесь зимнего стиля одежды.'
        elif -25 >= temp > -40:
            result += 'Холодно. Нужно надеть теплые шерстяные носки и теплый шерстяной свитер. Долго гулять не рекомендуется.'
        else:
            result += 'Очень холодно. Нужно надеть несколько свитеров и носков. Пребывание на улице по возможности сокращать.'

        # input()

        return result