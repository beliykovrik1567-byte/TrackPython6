# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, a=','):
    participants_list_1 = participants1.split(a)
    participants_list_2 = participants2.split(a)
    obshie_participants = list(set(participants_list_1).intersection(participants_list_2))
    obshie_participants.sort()
    return obshie_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)
