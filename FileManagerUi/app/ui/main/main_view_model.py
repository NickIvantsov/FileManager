import os
import shutil
from pathlib import Path

from app.file_manager.file_manager import FileManager
from app.util.constants import DEFAULT_STR, DEFAULT_DIR_PATH, DEFAULT_INT, PATH_SEPARATOR


def make_dir(directory, mode=0o775, exist_ok=True):
    if not os.path.exists(directory):
        os.makedirs(directory, mode=mode, exist_ok=exist_ok)


class MainViewModel:

    def __init__(self):
        self._file_manager = FileManager()
        self._parent_dir = DEFAULT_STR
        self._file_type = DEFAULT_STR
        self._final_dir = DEFAULT_DIR_PATH
        self._count_found_files_by_type = DEFAULT_INT
        self._count_found_files = DEFAULT_INT
        pass

    def get_all_files_form_dir(self):
        self._file_manager.parent_dir = self._parent_dir
        result_list = self._file_manager.get_all_files_form_dir()
        self._count_found_files = self._file_manager.count_found_files
        return result_list

    def get_all_files_by_type(self, file_types) -> list:
        self._file_manager.found_file_by_type_list.clear()
        for file_type in file_types:
            for fileName in self._file_manager.all_types_file_list:
                name = os.path.basename(fileName)
                if Path(name).suffix == file_type:
                    self._file_manager.found_file_by_type_list.append(name)

        return self._file_manager.found_file_by_type_list

    def count_all_files_by_type(self) -> int:
        self._file_manager.found_file_by_type_list.clear()
        self._file_manager.file_type = self._file_type
        for fileName in self._file_manager.all_types_file_list:
            name = os.path.basename(fileName)
            if Path(name).suffix == "." + self._file_manager.file_type:
                self._file_manager.found_file_by_type_list.append(name)
        return len(self._file_manager.found_file_by_type_list)

    def move_file(self):
        make_dir(self._file_manager.final_dir)
        for fileName in self._file_manager.found_file_by_type_list:
            path = self._file_manager.parent_dir + PATH_SEPARATOR + fileName
            move = self._file_manager.final_dir + PATH_SEPARATOR + fileName
            shutil.move(path, move)
        self._file_manager.found_file_by_type_list.clear()
        self._file_manager.all_types_file_list.clear()

    def add_file_by_type(self, value):
        self._file_manager.found_file_by_type_list.append(value)

    def get_all_types(self):
        return self._file_manager.get_all_types()

    def clear_all_types_file_list(self):
        self._file_manager._all_types_file_list.clear()

    @property
    def parent_dir(self):
        return self._parent_dir

    @parent_dir.setter
    def parent_dir(self, value):
        self._file_manager.parent_dir = value
        self._parent_dir = value

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_manager.file_type = value
        self._file_type = value

    @property
    def final_dir(self):
        return self._final_dir

    @final_dir.setter
    def final_dir(self, value):
        self._file_manager.final_dir = value
        self._final_dir = value

    @property
    def count_found_files(self):
        return self._count_found_files
