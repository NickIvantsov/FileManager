import os
from pathlib import Path

from app.util.constants import DEFAULT_STR, DEFAULT_INT, DEFAULT_DIR_PATH


class FileManager:
    DEFAULT_PARENT_PATH = "/home/nick/Downloads/Telegram Desktop"
    DEFAULT_END_PATH = "/home/nick/Documents/books/newTMPFolder"

    def __init__(self):
        self._parent_dir = DEFAULT_STR
        self._file_type = DEFAULT_STR
        self._final_dir = DEFAULT_DIR_PATH
        self._count_found_files_by_type = DEFAULT_INT
        self._count_found_files = DEFAULT_INT
        self._all_types_file_list = list()
        self._found_file_by_type_list = list()
        pass

    def __str__(self):
        return "Parent dir = %s," \
               " File type = %s," \
               " Final dir = %s," \
               " Count found files by type = %s," \
               " Count found files = %s," \
               " File list = %s," \
               " Found file list = %s," % (
                   self._parent_dir, self._file_type, self._final_dir, self._count_found_files_by_type,
                   self._count_found_files, self._all_types_file_list, self._found_file_by_type_list)

    def get_all_files_form_dir(self) -> list:
        self._count_found_files = 0
        if self._parent_dir != '':
            try:
                with os.scandir(self._parent_dir) as listOfEntries:
                    for entry in listOfEntries:
                        # печать всех записей, являющихся файлами
                        if entry.is_file():
                            self._count_found_files += 1
                            self._all_types_file_list.append(entry.name)
            except FileNotFoundError:
                self._count_found_files = 0
                self._count_found_files_by_type = 0
        return self._all_types_file_list

    def get_all_types(self):
        list_of_type = []
        for fileName in self.all_types_file_list:
            name = os.path.basename(fileName)
            list_of_type.append(Path(name).suffix)
        return set(list_of_type)

    @property
    def parent_dir(self):
        return self._parent_dir

    @parent_dir.setter
    def parent_dir(self, value):
        self._parent_dir = value

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value

    @property
    def final_dir(self):
        return self._final_dir

    @final_dir.setter
    def final_dir(self, value):
        self._final_dir = value

    @property
    def all_types_file_list(self):
        return self._all_types_file_list

    @all_types_file_list.setter
    def all_types_file_list(self, value):
        self._all_types_file_list = value

    @property
    def found_file_by_type_list(self):
        return self._found_file_by_type_list

    @found_file_by_type_list.setter
    def found_file_by_type_list(self, value):
        self._found_file_by_type_list = value

    @property
    def count_found_files_by_type(self):
        return self._count_found_files_by_type

    @property
    def count_found_files(self):
        return self._count_found_files
