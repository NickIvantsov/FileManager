import os
import shutil
from pathlib import Path

from PySide2.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QWidget, QLabel, QHBoxLayout

from helloApp.fileManager.FileManager import FileManager


class MainWindow(QMainWindow):
    fileManager = FileManager()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        parent_path_and_count_qhbox_layout = QHBoxLayout()
        file_type_and_count_qhbox_layout = QHBoxLayout()

        parent_path_line_edit = QLineEdit()
        parent_path_line_edit.setMaxLength(100)
        parent_path_line_edit.setPlaceholderText("Enter parent path")
        parent_path_line_edit.setText("/home/nick/Downloads/Telegram Desktop")
        parent_path_line_edit.textChanged.connect(self.parent_path_text_changed)

        file_type_line_edit = QLineEdit()
        file_type_line_edit.setMaxLength(100)
        file_type_line_edit.setPlaceholderText("Enter file type")
        file_type_line_edit.textChanged.connect(self.file_type_text_changed)

        path_to_final_dir_line_edit = QLineEdit()
        path_to_final_dir_line_edit.setMaxLength(100)
        path_to_final_dir_line_edit.setPlaceholderText("Enter path to final dir")
        path_to_final_dir_line_edit.setText("/home/nick/Documents/books/newTMPFolder")
        path_to_final_dir_line_edit.textChanged.connect(self.end_file_directory_text_changed)

        self.count_all_file_q_label = QLabel()
        self.count_all_file_q_label.setText("0")

        self.count_all_file_with_type_q_label = QLabel()
        self.count_all_file_with_type_q_label.setText("0")

        parent_path_and_count_qhbox_layout.addWidget(parent_path_line_edit)
        parent_path_and_count_qhbox_layout.addWidget(self.count_all_file_q_label)

        file_type_and_count_qhbox_layout.addWidget(file_type_line_edit)
        file_type_and_count_qhbox_layout.addWidget(self.count_all_file_with_type_q_label)

        widget = QWidget()
        widget.setLayout(layout)

        button = QPushButton("MOVE FILES")
        button.clicked.connect(self.the_button_moved_was_clicked)

        layout.addLayout(parent_path_and_count_qhbox_layout)
        layout.addLayout(file_type_and_count_qhbox_layout)
        layout.addWidget(path_to_final_dir_line_edit)
        layout.addWidget(button)

        self.setCentralWidget(widget)

    def parent_path_text_changed(self, parent_path):
        print("Text changed...")
        self.fileManager.parent_dir = parent_path
        self.fileManager.get_all_files_form_dir()
        self.count_all_file_q_label.setText(str(self.fileManager.count_found_files))
        print(parent_path)

    def file_type_text_changed(self, file_type):
        print("Text changed...")
        self.fileManager.file_type = file_type
        self.fileManager.count_found_files_by_type = 0
        file_count = 0
        print(self.fileManager.file_list)
        for fileName in self.fileManager.file_list:
            name = os.path.basename(fileName)
            if Path(name).suffix == "." + self.fileManager.file_type:
                print("file:" + name)
                self.fileManager.found_file_list.append(name)
                file_count += 1
        self.fileManager.count_found_files_by_type = file_count
        self.count_all_file_with_type_q_label.setText(str(self.fileManager.count_found_files_by_type))
        print(file_type)

    def end_file_directory_text_changed(self, final_dir):
        print("Text changed end_file_directory_text_changed ...")
        self.fileManager.final_dir = final_dir
        print(final_dir)

    def text_edited(self, file_type):
        print("Text edited...")
        self.fileManager.file_type = file_type
        file_count = 0
        for fileName in self.fileManager.file_list:
            if Path(fileName).suffix == "." + self.fileManager.file_type:
                self.fileManager.found_file_list.append(fileName)
                file_count += 1
        print(self.fileManager.found_file_list)
        self.fileManager.count_found_files_by_type = file_count
        self.count_all_file_with_type_q_label.setText(str(self.fileManager.count_found_files_by_type))
        print(file_type)

    def the_button_moved_was_clicked(self):
        print("Clicked!")
        os.makedirs(self.fileManager.final_dir, exist_ok=True)
        print(self.fileManager.found_file_list)
        for fileName in self.fileManager.found_file_list:
            path = self.fileManager.parent_dir + "/" + fileName
            move = self.fileManager.final_dir + "/" + fileName
            print("path: " + path)
            print("move: " + move)
            shutil.move(path, move)
        self.fileManager.found_file_list.clear()

    def move_all_files(self):
        # self.fileManager.parent_dir = input("Enter parent directory: ").strip()  # /home/nick/Downloads/Telegram Desktop /home/nick/Documents/books/newTMPFolder
        if self.fileManager.parent_dir != '':
            file_list = self.fileManager.get_all_files_form_dir()

            self.count_all_file_q_label.setText(str(self.fileManager.count_found_files))
            # self.fileManager.file_type = input("Enter file type: ")  #
            for fileName in file_list:
                if Path(fileName).suffix == "." + self.fileManager.file_type:
                    print(fileName)
        else:
            print("You need enter the path for parent directory!")
