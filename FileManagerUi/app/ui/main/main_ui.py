from PyQt5 import QtWidgets, sip
from PyQt5.QtWidgets import QCheckBox
from PySide2 import QtCore

from app.res.MainWindow import Ui_MainWindow
from app.ui.main.main_view_model import MainViewModel
from app.util.config_parser_manager import ConfigParserManager
from app.util.string_util import get_str_res


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self._main_view_model = MainViewModel()
        self._config_parser = ConfigParserManager()

        self.check_box_list = {}
        self.setupUi(self)
        self.le_parent_path.textChanged.connect(self.parent_path_text_change_listener)
        self.le_parent_path.setText("/home/nick/Downloads/Telegram Desktop")

        self.le_end_path.textChanged.connect(self.end_path_text_change_listener)
        self.le_end_path.setText("/home/nick/Documents/books/newTMPFolder")

        self.pushButton.clicked.connect(self.the_button_moved_was_clicked)
        layout = self.gridLayout
        self.widget.setLayout(layout)

        self.scrollAreaWidgetContents.setLayout(layout)

    def _get_str_res(self, res_id: str) -> str:
        return get_str_res(self._config_parser.config_parser, self._config_parser.section, res_id)

    def parent_path_text_change_listener(self, parent_path):
        self._main_view_model.clear_all_types_file_list()
        print(self.check_box_list)
        for key in self.check_box_list.keys():
            self.gridLayout.removeWidget(self.check_box_list[key])
            sip.delete(self.check_box_list[key])
            print(key, '->', self.check_box_list[key])

        self.check_box_list.clear()

        self._main_view_model.parent_dir = parent_path
        self._main_view_model.get_all_files_form_dir()
        count_file = str(self._main_view_model.count_found_files)
        self.ln_found_files.display(count_file)

        file_type_list = self._main_view_model.get_all_types()
        print(file_type_list)
        clone_array = []
        for index, file_type in enumerate(file_type_list):
            clone_array.append(file_type)

        result_array = even_divide(clone_array)

        for i, array in enumerate(result_array):
            for j, element in enumerate(result_array[i]):
                check_box = QCheckBox(result_array[i][j])
                self.check_box_list[result_array[i][j]] = check_box
                self.gridLayout.addWidget(check_box, i, j)
        for key in self.check_box_list.keys():
            print(key, '->', self.check_box_list[key])
            print(key, '->', self.check_box_list[key].checkState())

    def end_path_text_change_listener(self, final_dir):
        self._main_view_model.final_dir = final_dir
        print("final_dir = {}".format(final_dir))

    def the_button_moved_was_clicked(self):
        type_list = []
        for key in self.check_box_list.keys():
            print(key, '->', self.check_box_list[key])
            print(key, '->', self.check_box_list[key].isTristate())
            print(key, '->', self.check_box_list[key].checkState())
            print(key, '->', self.check_box_list[key].checkState() == QtCore.Qt.Checked)

            if self.check_box_list[key].checkState() == QtCore.Qt.Checked:
                type_list.append(key)
        print("result type list: {}".format(type_list))
        self._main_view_model.get_all_files_by_type(type_list)
        self._main_view_model.move_file()
        self.parent_path_text_change_listener(self._main_view_model.parent_dir)
        print("clicked")


def even_divide(lst, num_piece=4):
    return [
        [lst[i] for i in range(len(lst)) if (i % num_piece) == r]
        for r in range(num_piece)
    ]
