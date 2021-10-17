from PySide2.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QWidget, QLabel, QHBoxLayout, \
    QSpacerItem, QCheckBox

from app.file_manager.file_manager import FileManager
from app.ui.main.main_view_model import MainViewModel
from app.util.config_parser_manager import ConfigParserManager
from app.util.string_util import get_str_res


class MainWindow(QMainWindow):
    _DEFAULT_MAX_LENGTH = 100
    _DEFAULT_WIDTH = 500
    _PARENT_PATH_HINT_ID = "parent_path_hint"
    _FILE_TYPE_HINT = "file_type_hint"
    _END_DIR_PATH_HINT = "end_dir_path_hint"
    _MOVE_FILE_NAME = "move_btn"
    _FOUND_FILES = "found_files"
    _FOUND_FILES_TEXT = "found_files_text"

    def __init__(self):
        super().__init__()
        self._main_view_model = MainViewModel()

        self._config_parser = ConfigParserManager()

        layout = QVBoxLayout()

        parent_path_and_count_qhbox_layout = QHBoxLayout()
        file_type_and_count_qhbox_layout = QHBoxLayout()

        # enter parent path
        parent_path_line_edit = QLineEdit()
        parent_path_line_edit.setMaxLength(MainWindow._DEFAULT_MAX_LENGTH)
        parent_path_line_edit.setPlaceholderText(self._get_str_res(MainWindow._PARENT_PATH_HINT_ID))
        parent_path_line_edit.setText(FileManager.DEFAULT_PARENT_PATH)
        print("Step 1")
        parent_path_line_edit.textChanged.connect(self.parent_path_text_change_listener)

        # enter file type
        file_type_line_edit = QLineEdit()
        file_type_line_edit.setMaxLength(MainWindow._DEFAULT_MAX_LENGTH)
        file_type_line_edit.setPlaceholderText(self._get_str_res(MainWindow._FILE_TYPE_HINT))
        file_type_line_edit.textChanged.connect(self.file_type_text_changed)

        # enter end file dir path
        path_to_final_dir_line_edit = QLineEdit()
        path_to_final_dir_line_edit.setMaxLength(MainWindow._DEFAULT_MAX_LENGTH)
        path_to_final_dir_line_edit.setPlaceholderText(self._get_str_res(MainWindow._END_DIR_PATH_HINT))
        path_to_final_dir_line_edit.setText(FileManager.DEFAULT_END_PATH)
        path_to_final_dir_line_edit.textChanged.connect(self.end_file_directory_text_changed)

        default_found_files = self._get_str_res(MainWindow._FOUND_FILES)
        found_files_text = self._get_str_res(MainWindow._FOUND_FILES_TEXT)

        self.count_all_file_q_label = QLabel()
        self.count_all_file_q_label.setText(default_found_files)

        self.found_files_all_files_q_label = QLabel()
        self.found_files_all_files_q_label.setText(found_files_text)

        self.count_all_file_with_type_q_label = QLabel()
        self.count_all_file_with_type_q_label.setText(default_found_files)

        self.count_all_file_with_type_text_q_label = QLabel()
        self.count_all_file_with_type_text_q_label.setText(found_files_text)

        parent_path_and_count_qhbox_layout.addWidget(parent_path_line_edit)
        parent_path_and_count_qhbox_layout.addItem(QSpacerItem(10, 0))
        parent_path_and_count_qhbox_layout.addWidget(self.count_all_file_with_type_text_q_label)
        parent_path_and_count_qhbox_layout.addWidget(self.count_all_file_q_label)

        file_type_and_count_qhbox_layout.addWidget(file_type_line_edit)
        file_type_and_count_qhbox_layout.addItem(QSpacerItem(10, 0))
        file_type_and_count_qhbox_layout.addWidget(self.found_files_all_files_q_label)
        file_type_and_count_qhbox_layout.addWidget(self.count_all_file_with_type_q_label)

        widget = QWidget()
        widget.setLayout(layout)

        self._check_box_layout = QVBoxLayout()
        # button
        btn_move_name = self._get_str_res(MainWindow._MOVE_FILE_NAME).upper()
        button = QPushButton(btn_move_name)
        button.clicked.connect(self.the_button_moved_was_clicked)
        default_width = 0
        default_height = 10
        layout.addItem(QSpacerItem(default_width, default_height))
        layout.addLayout(parent_path_and_count_qhbox_layout)
        layout.addItem(QSpacerItem(default_width, default_height))
        layout.addLayout(self._check_box_layout)
        layout.addLayout(file_type_and_count_qhbox_layout)
        layout.addItem(QSpacerItem(default_width, default_height))
        layout.addWidget(path_to_final_dir_line_edit)
        layout.addItem(QSpacerItem(default_width, default_height))
        layout.addWidget(button)

        self.setMinimumWidth(MainWindow._DEFAULT_WIDTH)
        self.setCentralWidget(widget)

    def _get_str_res(self, res_id: str) -> str:
        return get_str_res(self._config_parser.config_parser, self._config_parser.section, res_id)

    def parent_path_text_change_listener(self, parent_path):
        self._main_view_model.parent_dir = parent_path
        self._main_view_model.get_all_files_form_dir()
        count_file = str(self._main_view_model.count_found_files)
        self.count_all_file_q_label.setText(count_file)
        print("Step 2")
        file_type_list = self._main_view_model.get_all_types()
        print("Step 3")

        file_type_check_box_layout_h = QHBoxLayout()
        self._check_box_layout.addLayout(file_type_check_box_layout_h)
        for index, file_type in enumerate(file_type_list):
            if index % 5 == 0 and index != 0:
                file_type_check_box_layout_h = QHBoxLayout()
                self._check_box_layout.addLayout(file_type_check_box_layout_h)
            file_type_check_box_layout_h.addWidget(QCheckBox(file_type))

    def file_type_text_changed(self, file_type):
        self._main_view_model.file_type = file_type
        found_numb_txt = str(self._main_view_model.count_all_files_by_type())
        self.count_all_file_with_type_q_label.setText(found_numb_txt)

    def end_file_directory_text_changed(self, final_dir):
        self._main_view_model.final_dir = final_dir

    def the_button_moved_was_clicked(self):
        self._main_view_model.move_file()
