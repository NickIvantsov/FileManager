import os


class FileManager:
    parent_dir = ""
    file_type = ""
    final_dir = "."
    count_found_files = 0
    count_found_files_by_type = 0
    file_list = list()
    found_file_list = list()

    def __init__(self):
        pass

    def get_all_files_form_dir(self) -> list:
        # чтение записей
        if self.parent_dir != '':
            try:
                with os.scandir(self.parent_dir) as listOfEntries:
                    for entry in listOfEntries:
                        # печать всех записей, являющихся файлами
                        if entry.is_file():
                            self.count_found_files += 1
                            print(entry.name)
                            self.file_list.append(entry.name)
            except FileNotFoundError:
                self.count_found_files = 0
                self.count_found_files_by_type = 0
                print("No such file or directory!")
        return self.file_list
