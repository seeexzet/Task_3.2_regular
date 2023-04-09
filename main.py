from pprint import pprint
import re
import csv
## Читаем адресную книгу в формате CSV в список contacts_list:

with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
correct_list = []
for contact in contacts_list[0:]:
    name = ' '.join(contact[0:3]).split(' ')
    contact[0:3] = name[0:3]
    pattern_num = r'(\+7|8)?(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\-*)(\d{2})(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    substitusion_num = r'+7(\4)\8-\10-\12\13\15\16\18'
    result = re.sub(pattern_num, substitusion_num, contact[5])
    contact[5] = result
    correct_list.append(contact)

contacts = {}
for i in correct_list:
    if i[0] not in contacts:
        contacts[i[0]] = i[1:]
    else:
        list1 = contacts.get(i[0])
        for j in range(1, 6):
            if (list1[j-1] == '' and i[j] != ''):
                list1[j-1] = i[j]
        contacts[i[0]] = list1[1:]

final_list=[]
for key, value in contacts.items():
    value.insert(0, key)
    final_list.append(value)

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w", newline='', encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(final_list)