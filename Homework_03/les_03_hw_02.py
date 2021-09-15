def data(name, surname, date_of_birth, city_of_residence, e_mail, phone):
    """function - notebook"""

    print(f'name - {name}; '
          f'surname - {surname}; '
          f'date of birth - {date_of_birth}; '
          f'city of residence - {city_of_residence}; '
          f'e-mail - {e_mail}; '
          f'phone - {phone}'
          )


help(data)
# static test
print('start of the static test:')

big_data = {
    'phone': ['7-777-777-77-77', '7-555-555-55-55'],
    'date_of_birth': ['12.05.1984', '11.06.1986'],
    'name': ['Ivan', 'Maria'],
    'e-mail': ['i.ivanov@mail.com', 'm.ivanova@mail.com'],
    'surname': ['Ivanov', 'Ivanova'],
    'city_of_residence': ['Moscow', 'Tula']
}

for i in range(2):
    data(name=big_data.get('name')[i],
         surname=big_data.get('surname')[i],
         date_of_birth=big_data.get('date_of_birth')[i],
         city_of_residence=big_data.get('city_of_residence')[i],
         e_mail=big_data.get('e-mail')[i],
         phone=big_data.get('phone')[i]
         )

# manual test
print('\nstart of the manual test:')

data(name=input('input name: '),
     surname=input('input surname: '),
     date_of_birth=input('input date of birth: '),
     city_of_residence=input('input city fo residence: '),
     e_mail=input('input e-mail: '),
     phone=input('input phone: ')
     )
