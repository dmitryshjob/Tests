


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}]

def citis ():
    for dictionaries in geo_logs[:]:
        for keys, value in dictionaries.items():       
            if 'Россия' != value[1]:
                geo_logs.remove(dictionaries)
    return geo_logs




ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def dictionaries ():
    list = ids.values()
    new_ids = []
    for value in list:
    
        for integer in value:
        
            new_ids.append(integer)

    return new_ids




queries = [
    'смотреть сериалы онлайн kkkf',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]
dict = dict()

def list_requests():
    for str in queries:        
        number = len(str.split(' '))
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1 

    count = len(queries)

    for number, query_count in sorted(dict.items()):
        s = 100 * query_count / count
    return s    




stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_val = max(stats.items()) 


