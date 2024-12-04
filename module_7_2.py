def custom_write(file_name: str, strings: list):

    string_position: dict = {}
    number_str = 1
    file_name_text = open(file_name, 'w', encoding='utf-8') # для записи символов которых нет в ASCII
    for string in strings:
        number_byte = file_name_text.tell()
        file_name_text.write(f'{string}\n')
        string_position[(number_str, number_byte)] = string
        number_str += 1
    file_name_text.close()
    return string_position



if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    # print(result)
    for elem in result.items():
        print(elem)

