import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pytube import YouTube, Playlist


class Downloader(QDialog):
    def __init__(self, parent=None):
        super(Downloader, self).__init__(parent)

        self.setStyleSheet("background-image: rgba(255, 255, 200, 0.5);")

        self.urlLabel = QLabel('YouTube URL: ')
        self.urtwolLabel = QLabel('PlayList URL: ')
        self.urthreelLabel = QLabel('Download Location: ')

        self.urlEdit = QLineEdit()
        self.urtwolEdit = QLineEdit()
        self.urthreelEdit = QLineEdit()

        self.showMenuButton = QPushButton('Download Now')

        self.BrowseButton = QPushButton('Choose location')

        layout = QGridLayout()
        layout.addWidget(self.urlLabel, 0, 0)
        layout.addWidget(self.urtwolLabel, 1, 0)
        layout.addWidget(self.urthreelLabel, 2, 0)

        layout.addWidget(self.urlEdit, 0, 1)
        layout.addWidget(self.urtwolEdit, 1, 1)
        layout.addWidget(self.urthreelEdit, 2, 1)

        layout.addWidget(self.BrowseButton, 3, 0)

        layout.addWidget(self.showMenuButton, 3, 1)

        self.setLayout(layout)
        self.setWindowTitle('YouTube GOLD')

        self.BrowseButton.clicked.connect(self.Browse)
        self.showMenuButton.clicked.connect(self.showMenuDialog)
        self.videoQualityComboBox = QComboBox()
        self.videoQualityComboBoxx = QComboBox()

        self.videoQualityComboBox.addItems(
            ['Highest', '1080p', '720p', '480p', '360p', '240p', '144p'])
        self.videoQualityComboBoxx.addItems(
            ['Highest', '1080p', '720p', '480p', '360p', '240p', '144p'])

        self.BrowseButton.setFixedSize(200, 50)
        self.showMenuButton.setFixedSize(300, 50)
        self.urlEdit.setFixedSize(300, 50)
        self.urtwolEdit.setFixedSize(300, 50)
        self.urthreelEdit.setFixedSize(300, 50)

        button_style = """
            QPushButton {
                background-color: #FFD95A;
                color: black;
                font-size:15px;
                padding: 1rem;
                border-radius: 5px;
                font-weight:bold;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #C07F00;
            }
        """

        label_style = """
            QLabel {
                font-size: 14px;
                font-weight:bold;
                color:#222;
            }
    """
        edit_style = """
            QLineEdit {
                padding-left: 20px;
                border-radius: 5px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                font-size: 16px;
            }
    """

        self.BrowseButton.setStyleSheet(button_style)
        self.showMenuButton.setStyleSheet(button_style)

        self.urlLabel.setStyleSheet(label_style)
        self.urtwolLabel.setStyleSheet(label_style)
        self.urthreelLabel.setStyleSheet(label_style)

        self.urlEdit.setStyleSheet(edit_style)
        self.urtwolEdit.setStyleSheet(edit_style)
        self.urthreelEdit.setStyleSheet(edit_style)
        self.download_Folder = ''

    def download(self):
        url = self.urlEdit.text()
        yt = YouTube(url)
        video_quality = self.videoQualityComboBox.currentText()
        if video_quality == 'Highest':
            stream = yt.streams.get_highest_resolution()
        elif video_quality == '1080p':
            stream = yt.streams.filter(res='1080p').first()
        elif video_quality == '720p':
            stream = yt.streams.filter(res='720p').first()
        elif video_quality == '480p':
            stream = yt.streams.filter(res='480p').first()
        elif video_quality == '360p':
            stream = yt.streams.filter(res='360p').first()
        elif video_quality == '240p':
            stream = yt.streams.filter(res='240p').first()
        elif video_quality == '144p':
            stream = yt.streams.filter(res='144p').first()
        else:
            QMessageBox.warning(self, "Error", "Invalid quality option")
            return
        if self.download_Folder:
            stream.download(output_path=self.download_Folder)
            QMessageBox.information(
                self, "Download Completed", "Download has been completed successfully!")
        else:
            QMessageBox.warning(
                self, "Error", "Please select download location before download starts")

    def downloadPlaylist(self):
        playlist_url = self.urtwolEdit.text()
        playlist = Playlist(playlist_url)
        videos = playlist.video_urls
        video_quality = self.videoQualityComboBoxx.currentText()
        for video_url in videos:
            yt = YouTube(video_url)
            if video_quality == 'Highest':
                stream = yt.streams.get_highest_resolution()
            elif video_quality == '1080p':
                stream = yt.streams.filter(res='1080p').first()
            elif video_quality == '720p':
                stream = yt.streams.filter(res='720p').first()
            elif video_quality == '480p':
                stream = yt.streams.filter(res='480p').first()
            elif video_quality == '360p':
                stream = yt.streams.filter(res='360p').first()
            elif video_quality == '240p':
                stream = yt.streams.filter(res='240p').first()
            elif video_quality == '144p':
                stream = yt.streams.filter(res='144p').first()
            else:
                QMessageBox.warning(self, "Error", "Invalid quality option")
                return
            if self.download_Folder:
                stream.download(output_path=self.download_Folder)
        QMessageBox.information(
            self, "Download Completed", "Download has been completed successfully!")

    def downloader(self):
        url = self.urlEdit.text()
        yt = YouTube(url)
        stream = yt.streams.get_by_itag(251)
        if self.download_Folder:
            stream.download(output_path=self.download_Folder)
            QMessageBox.information(
                self, "Download Completed", "Download has been completed successfully!")
        else:
            QMessageBox.warning(
                self, "Error", "Please select download location before download starts")

    def Browse(self):
        global download_Path
        download_Path = QFileDialog.getExistingDirectory(
            self, "Select Directory")
        self.urthreelEdit.setText(download_Path)
        self.download_Folder = download_Path

    def showMenuDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Menu')

        videoButton = QPushButton('Download Video (mp4)')
        audioButton = QPushButton('Download Audio (mp3)')
        playlistButton = QPushButton('Download Playlist')

        self.videoQualityComboBox = QComboBox()
        self.videoQualityComboBox.addItems(
            ['Highest', '1080p', '720p', '480p', '360p', '240p', '144p'])

        self.videoQualityComboBoxx = QComboBox()
        self.videoQualityComboBoxx.addItems(
            ['Highest', '1080p', '720p', '480p', '360p', '240p', '144p'])

        layout = QVBoxLayout()
        layout.addWidget(videoButton)
        layout.addWidget(self.videoQualityComboBox)
        layout.addWidget(audioButton)
        layout.addWidget(playlistButton)
        layout.addWidget(self.videoQualityComboBoxx)

        dialog.setLayout(layout)

        videoButton.clicked.connect(self.download)
        audioButton.clicked.connect(self.downloader)
        playlistButton.clicked.connect(self.downloadPlaylist)

        button_d = """
            QPushButton {
                background-color: #FFD95A;
                color: black;
                font-size:15px;
                font-weight: bold;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #C07F00;
            }
        """
        button_c = """
            QComboBox {
                background-color: #FFF7D4; 
                color: black;
                padding-left: 20px;
                border: 2px solid #C07F00;
                font-weight:bold;
                border-radius: 5px;
                outline: none;
                font-size:15px;
            }

            QComboBox:hover {
                background-color: #C07F00;
            }
        """

        videoButton.setStyleSheet(button_d)

        audioButton.setStyleSheet(button_d)

        playlistButton.setStyleSheet(button_d)

        self.videoQualityComboBoxx.setStyleSheet(button_c)
        self.videoQualityComboBox.setStyleSheet(button_c)

        videoButton.setFixedSize(300, 50)
        audioButton.setFixedSize(300, 50)
        playlistButton.setFixedSize(300, 50)
        self.videoQualityComboBox.setFixedSize(300, 50)
        self.videoQualityComboBoxx.setFixedSize(300, 50)

        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    current_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_path,'iconn\\youtubeGOLD.png')
    icon = QIcon(image_path)
    downloader = Downloader()
    downloader.setWindowIcon(icon)
    downloader.show()
    sys.exit(app.exec_())