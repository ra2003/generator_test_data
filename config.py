# -- coding utf-8 --
token = '###################################'

from returns import \
    inn_entity, inn_individual, ogrn_entity, ogrn_individual, \
    snils, full_name, birdthay, login, mail, phone, uuid, guid

actions = {
    'ИНН': inn_entity,
    'ИНН ФЛ': inn_individual,
    'ОГРН': ogrn_entity,
    'ОГРН ИП': ogrn_individual,
    'СНИЛС': snils,
    'ФИО': full_name,
    'Дата рождения': birdthay,
    'Логин': login,
    'E-mail': mail,
    'Телефон': phone,
    'GUID': guid,
    'UUID': uuid,
}