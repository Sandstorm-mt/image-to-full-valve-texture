import sys
from PIL import Image

def find_closest_power_of_two(value):
    power = 0
    while value > 1:
        value //= 2
        power += 1
    
    return 2 ** power

def resize_image_to_nearest_power_of_two(image_path):
    # Открываем изображение
    try:
        image = Image.open(image_path)
    except FileNotFoundError as e:
        print(f"Ошибка: Файл {image_path} не найден.")
        return
    except Exception as e:
        print(f"Произошла ошибка при открытии файла: {e}")
        return
    
    # Получаем текущие размеры изображения
    width, height = image.size
    
    # Находим ближайшие степени двойки для ширины и высоты
    new_width = find_closest_power_of_two(width)
    new_height = find_closest_power_of_two(height)
    
    # Изменяем размер изображения
    resized_image = image.resize((new_width, new_height), resample=Image.LANCZOS)
    
    # Сохраняем измененное изображение
    output_path = f"{image_path.split('.')[0]}_resized.png"
    resized_image.save(output_path)
    
    print(f"Изменение размеров завершено! Новое разрешение: {new_width}x{new_height}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py путь_к_изображению")
    else:
        image_path = sys.argv[1]
        resize_image_to_nearest_power_of_two(image_path)