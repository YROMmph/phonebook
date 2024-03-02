main_menu = ['Глваное меню',
             'Открыть телефонную книгу',
             'Сохранить телефонную книгу',
             'Показать контанкт',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход'] # без "," будет выводить в строку слитно

choice_main_menu = f'Выберите пункт меню ({1}-{len(main_menu)-1}):'
choice_main_menu_error = f'Нужно ввести ячисло от 1 до {len(main_menu)-1}'

phone_book_opened_successful = 'Телефонная книга открыта успешно'
phone_book_saved_successful = 'Телефонная книга сохранена успешно'

empty_phone_book_error = 'Телефонная книга не открыта или пуста '

input_new_contact =['Введите имя контакта: ',
                    'Введите номер контакта: ',
                    'Введите фамилию контакта: ']

no_changes = 'Или ENTER, чтобы оставить без изменений'

edit_contact = [f'Введите новое имя ({no_changes}): ',
                f'Введите новый телефон ({no_changes}): ',
                f'Введите новую Фамилию ({no_changes}): ']

input_search_word = 'Введите слово для поиска: '
input_search_word_for_edit = 'Введите слово для поиска, который хотите изменить:'
input_search_word_for_delete = 'Введите слово для поиска, который хотите удалить: '
input_id_for_edit = 'Введите 10 контакта, который хотите изменить: '
input_id_for_delete = 'Введите ID контакта, который хотите удалить:'

def new_contact_added_successful(name: str) -> str:
    return f'Контакт "{name}" успешно добавлен!'

def find_contact_no_result(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены'

def edit_contact_successful(name) -> str:
    return f'Контакт "{name}" успешно изменен'

def delete_contact_successful(name) -> str:
    return f'Контакт "{name}" успешно удален'
    