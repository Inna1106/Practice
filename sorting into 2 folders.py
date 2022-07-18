# Быстрое перемещение файла из папки в папку

# Устанавливаем библиотеку watchdog - следящая собака
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        # перебираем все файлы в папке из переменной folder_track
        # и переносим файлы в папкку в переменной folder_dest
        for filename in os.listdir(folder_track):
            extension = filename.split('.')
            if len(extension) > 1 and (extension[1].lower() == 'py'):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/" + filename
                os.rename(file, new_path)   # переименовка
            if len(extension) > 1 and (extension[1].lower() == 'txt'):
                file = folder_track + "/" + filename
                new_path = folder_dest_1 + "/" + filename
                os.rename(file, new_path)   # переименовка

folder_track = 'D:\Project folder sorter\sort\sorter'
folder_dest = 'D:\Project folder sorter\sort\d_py'
folder_dest_1 = 'D:\Project folder sorter\sort\d_txt'

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)   # сон в 1 секунду
except KeyboardInterrupt:
    observer.stop()

observer.join()