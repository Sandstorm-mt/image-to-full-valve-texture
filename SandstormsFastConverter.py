import os
import subprocess
import sys


def create_vmt_file(input_path):
    # Получаем имя файла без расширения
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    
    # Формируем имя нового файла с расширением .vmt
    output_path = f"{base_name}.vmt"
    
    # Убираем расширение из пути до файла
    base_texture_path = os.path.join(os.path.dirname(input_path), base_name)
    
    # Создаем содержимое для нового файла
    content = f"""LightmappedGeneric
{{
\t$basetexture {base_texture_path}
}}"""
    
    # Записываем содержимое в новый файл
    parent_folder = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    final_output_path = os.path.join(parent_folder, output_path)
    
    with open(final_output_path, 'w') as file:
        file.write(content)
        
    print(f"Файл {final_output_path} успешно создан.")


def main():
    # Получаем путь к перетащенному файлу из аргументов командной строки
    file_path = os.path.abspath(sys.argv[1])
    
    # Путь к папке с программой
    program_folder = os.path.dirname(os.path.realpath(__file__))
    
    # Сначала создаем VMT файл
    create_vmt_file(file_path)
    
    # Затем выполняем команду vtfcmd
    parent_folder = os.path.dirname(program_folder)
    command_vtfcmd = f'vtfcmd.exe -folder "{file_path}" -output "{parent_folder}" -recurse -pause'
    
    # Выполняем команду
    result_vtfcmd = subprocess.run(command_vtfcmd, shell=True, capture_output=True, text=True)
    
    if result_vtfcmd.returncode == 0:
        print("Команда vtfcmd выполнена успешно.")
    else:
        print(f"Ошибка выполнения команды vtfcmd. Код ошибки: {result_vtfcmd.returncode}")
        print(result_vtfcmd.stderr)


if __name__ == "__main__":
    main()