# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Task_1.calling_psql_funtion import abhishek_return_dep_people

if __name__ == '__main__':
    print('Enter organazation id :')
    organazation_id = input()
    data = abhishek_return_dep_people(organazation_id)
    print(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
