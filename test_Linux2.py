import subprocess
import string


def execute_command(command, text, word_mode=False):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)

        # Проверка в режиме поиска текста в полном выводе
        if not word_mode:
            if text in output:
                return True
            else:
                return False

        # Режим разбиения вывода на слова с удалением знаков пунктуации
        else:
            # Удаление знаков пунктуации из вывода
            output_cleaned = output.translate(str.maketrans('', '', string.punctuation))
            # Разбиение вывода на слова
            words = output_cleaned.split()
            # Проверка наличия слова в полученном списке слов
            if text in words:
                return True
            else:
                return False

    except subprocess.CalledProcessError:
        return False