import asyncio
import io
from datetime import datetime
from os import listdir
from os.path import isfile, join

import yaml
import os
import socket
import sys
from contextlib import redirect_stdout

import logging  # for logs
from functools import partial

import requests
from PySide2 import QtGui
from PySide2.QtCore import Qt, QObject
from PySide2.QtGui import QIcon, QColor, QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit, QMessageBox, QSplashScreen, \
    QListWidgetItem, QFileDialog, QLabel, QWidget, QHBoxLayout, QLayout

import download
import gui.ui_united
import metadata
import updater
import utils
import wiiload

VERSION = updater.current_version()
BRANCH = updater.get_branch()
if BRANCH == "Stable":
    DISPLAY_VERSION = VERSION
else:
    DISPLAY_VERSION = VERSION + " " + BRANCH

HOST = "hbb1.oscwii.org"
HOST_NAME = "primary"


# Get resource when frozen with PyInstaller
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# Actions to perform only when the program is frozen:
if updater.is_frozen():
    logging.basicConfig(level=logging.DEBUG)
    logging.info(f"Open Shop Channel Downloader v{updater.current_version()} {updater.get_branch()}")
    logging.info(f"OSCDL, Open Source Software by dhtdht020. https://github.com/dhtdht020.\n\n\n")


# G U I
class MainWindow(gui.ui_united.Ui_MainWindow, QMainWindow):
    def __init__(self, test_mode=False):
        super(MainWindow, self).__init__()
        self.ui = gui.ui_united.Ui_MainWindow()
        self.ui.setupUi(self)

        self.test_mode = test_mode

        # Set title and icon of window
        self.setWindowTitle(f"Open Shop Channel Downloader v{DISPLAY_VERSION} - Library")
        app_icon = QIcon(resource_path("assets/gui/windowicon.png"))
        self.setWindowIcon(app_icon)

        self.current_category = "all"
        self.current_developer = ""
        self.repo_data = None

        # Set GUI Icons

        # ABOUT
        self.ui.actionAbout_OSC_DL.setIcon(QIcon(resource_path("assets/gui/icons/about-open-version.png")))
        # CLIENTS
        self.ui.menuHomebrew_Browser.setIcon(QIcon(resource_path("assets/gui/icons/hbb-icon.png")))
        self.ui.menuOpen_Shop_Channel_DL.setIcon(QIcon(resource_path("assets/gui/icons/oscdl-icon.png")))
        self.ui.actionDownload_HBB_Client_Latest.setIcon(QIcon(resource_path("assets/gui/icons/download.png")))
        self.ui.actionCheck_for_Updates.setIcon(QIcon(resource_path("assets/gui/icons/check-for-updates.png")))
        self.ui.actionRefresh.setIcon(QIcon(resource_path("assets/gui/icons/refresh.png")))
        # DEBUG
        self.ui.actionEnable_Log_File.setIcon(QIcon(resource_path("assets/gui/icons/enable-log.png")))
        self.ui.actionClear_Log.setIcon(QIcon(resource_path("assets/gui/icons/clear-log.png")))
        self.ui.actionClose_the_shop.setIcon(QIcon(resource_path("assets/gui/icons/close-shop.png")))
        self.ui.menuExperimental.setIcon(QIcon(resource_path("assets/gui/icons/experimental.png")))
        self.ui.actionSelect_Theme.setIcon(QIcon(resource_path("assets/gui/icons/theme.png")))
        # DEBUG -> EXPERIMENTAL
        self.ui.menuAnnouncement_Banner.setIcon(QIcon(resource_path("assets/gui/icons/announcement-banner.png")))
        # DEBUG -> EXPERIMENTAL -> ANNOUNCEMENT BANNER
        self.ui.actionDisplay_Banner.setIcon(QIcon(resource_path("assets/gui/icons/announcement-banner-reload.png")))

        # CATEGORIES COMBOBOX
        self.ui.CategoriesComboBox.setItemIcon(1, QIcon(resource_path("assets/gui/icons/category/utility.png")))
        self.ui.CategoriesComboBox.setItemIcon(2, QIcon(resource_path("assets/gui/icons/category/emulator.png")))
        self.ui.CategoriesComboBox.setItemIcon(3, QIcon(resource_path("assets/gui/icons/category/game.png")))
        self.ui.CategoriesComboBox.setItemIcon(4, QIcon(resource_path("assets/gui/icons/category/media.png")))
        self.ui.CategoriesComboBox.setItemIcon(5, QIcon(resource_path("assets/gui/icons/category/demo.png")))

        self.populate_stylesheets()
        self.populate()
        self.selection_changed()
        self.status_message("Ready to download")
        self.ui.progressBar.setHidden(False)
        self.ui.statusBar.addPermanentWidget(self.ui.progressBar)
        self.load_announcement_banner()

    # show given status message on bottom status bar
    def status_message(self, message):
        self.ui.statusBar.showMessage(message)

    # populate UI elements
    def populate(self):
        try:
            if not splash.isHidden():
                splash.showMessage(f"Loading contents..", color=splash_color)
        except NameError:
            pass
        self.ui.actionAbout_OSC_DL.setText(f"OSCDL v{VERSION} by dhtdht020")
        self.populate_repositories()
        self.populate_list()
        self.assign_initial_actions()

    # Populate list of repositories
    def populate_repositories(self):
        try:
            yaml_file = requests.get(
                "https://raw.githubusercontent.com/dhtdht020/oscdl-updateserver/master/v1/announcement"
                "/repositories.yml").text
            parsed_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)
            repos = parsed_yaml["repos"]
            n = 0
            for i in repos:
                display_name = parsed_yaml["repositories"][i]["name"]
                host = parsed_yaml["repositories"][i]["host"]
                description = parsed_yaml["repositories"][i]["description"]
                name = i
                self.ui.ReposComboBox.addItem(display_name)
                self.ui.ReposComboBox.setItemData(n, [display_name, host, description, name], Qt.UserRole)
                try:
                    if not splash.isHidden():
                        splash.showMessage(f"Loaded {n} repositories..", color=splash_color)
                except NameError:
                    pass
                n += 1

            index = self.ui.ReposComboBox.currentIndex()
            self.repo_data = self.ui.ReposComboBox.itemData(index, Qt.UserRole)

            self.ui.RepositoryNameLabel.setText(self.repo_data[0])
            self.ui.RepositoryDescLabel.setText(self.repo_data[2])
        except Exception:
            # Add base repos
            self.ui.ReposComboBox.addItem("Open Shop Channel")
            self.ui.ReposComboBox.addItem("Homebrew Channel Themes")
            self.ui.ReposComboBox.setItemData(0, ["Open Shop Channel",
                                                  "hbb1.oscwii.org",
                                                  "Built in: Open Shop Channel default repository.",
                                                  "primary"], Qt.UserRole)
            self.ui.ReposComboBox.setItemData(1, ["Homebrew Channel Themes",
                                                  "hbb3.oscwii.org",
                                                  "Built in: Open Shop Channel default theme repository.",
                                                  "themes"], Qt.UserRole)

    def assign_initial_actions(self):
        # Connect signals
        try:
            if not splash.isHidden():
                splash.showMessage(f"Finishing (1/3)..", color=splash_color)
        except NameError:
            pass
        # Buttons
        self.ui.CopyDirectLinkBtn.clicked.connect(self.copy_download_link_button)
        self.ui.ViewMetadataBtn.clicked.connect(self.download_button)
        self.ui.WiiLoadButton.clicked.connect(self.wiiload_button)
        self.ui.ReturnToMainBtn.clicked.connect(self.return_to_all_apps_btn)

        # Search Bar
        self.ui.SearchBar.textChanged.connect(self.search_bar)

        # Others
        self.ui.ReposComboBox.currentIndexChanged.connect(self.changed_host)
        self.ui.CategoriesComboBox.currentIndexChanged.connect(self.changed_category)
        self.ui.listAppsWidget.currentItemChanged.connect(self.selection_changed)
        self.ui.tabMetadata.currentChanged.connect(self.tab_changed)
        self.ui.developer_profile_btn.clicked.connect(self.developer_profile)

        # Actions
        # -- Debug
        self.ui.actionEnable_Log_File.triggered.connect(self.turn_log_on)
        self.ui.actionClose_the_shop.triggered.connect(self.close_the_shop)
        self.ui.actionDisplay_Banner.triggered.connect(self.load_announcement_banner)
        self.ui.actionSelect_Theme.triggered.connect(self.select_theme_action)
        # -- Clients
        # ---- Homebrew Browser
        self.ui.actionDownload_HBB_Client_Latest.triggered.connect(partial(self.download_latest_hbb_action))
        # ---- OSCDL
        self.ui.actionCheck_for_Updates.triggered.connect(partial(self.check_for_updates_action))
        self.ui.actionRefresh.triggered.connect(partial(self.repopulate))

    # When user switches to a different tab
    def tab_changed(self):
        if self.ui.tabMetadata.currentIndex() == 1:
            self.ui.longDescriptionBrowser.setText("Loading description..")
            self.repaint()
            app_name = self.ui.listAppsWidget.currentItem().data(Qt.UserRole)["internal_name"]
            self.ui.longDescriptionBrowser.setText(metadata.long_description(app_name, repo=HOST))

    # When user selects a different homebrew from the list
    def selection_changed(self):
        try:
            if not splash.isHidden():
                splash.showMessage(f"Finishing (2/3) - Loading first app..", color=splash_color)
        except NameError:
            pass
        try:
            data = self.ui.listAppsWidget.currentItem().data(Qt.UserRole)
            app_name = data["internal_name"]
        except Exception:
            app_name = None
        if app_name is not None:
            # Set active tab to first
            self.ui.tabMetadata.setCurrentIndex(0)

            # Hide icon
            self.ui.HomebrewIconLabel.hide()

            # Clear supported controllers listview:
            self.ui.SupportedControllersListWidget.clear()

            # Set data
            data = self.ui.listAppsWidget.currentItem().data(Qt.UserRole)

            # -- Get actual metadata
            # App Name
            self.ui.appname.setText(data["display_name"])
            self.ui.SelectionInfoBox.setTitle("Metadata: " + data["display_name"])
            self.ui.label_displayname.setText(data["display_name"])

            # File Size
            try:
                self.ui.filesize.setText(metadata.file_size(data["extracted"]))
            except KeyError:
                self.ui.filesize.setText("Unknown")

            # Category
            self.ui.HomebrewCategoryLabel.setText(metadata.category_display_name(data["category"]))

            # Release Date
            self.ui.releasedate.setText(datetime.fromtimestamp(int(data["release_date"])).strftime('%B %e, %Y at %R'))

            # Controllers
            controllers = metadata.parse_controllers(data["controllers"])
            # Add icons for Wii Remotes
            if controllers[0] > 1:
                item = QListWidgetItem()
                item.setText(f"{str(controllers[0])} Wii Remotes")
                item.setIcon(QIcon(resource_path(f"assets/gui/icons/controllers/{str(controllers[0])}WiiRemote.png")))
                item.setToolTip(f"This app supports up to {str(controllers[0])} Wii Remotes.")
                self.ui.SupportedControllersListWidget.addItem(item)
            elif controllers[0] == 1:
                item = QListWidgetItem()
                item.setText(f"1 Wii Remote")
                item.setIcon(QIcon(resource_path(f"assets/gui/icons/controllers/1WiiRemote.png")))
                item.setToolTip("This app supports a single Wii Remote.")
                self.ui.SupportedControllersListWidget.addItem(item)
            if controllers[1] is True:
                item = QListWidgetItem()
                item.setText(f"Nunchuk")
                item.setIcon(QIcon(resource_path(f"assets/gui/icons/controllers/Nunchuk.png")))
                item.setToolTip("This app can be used with a Nunchuk.")
                self.ui.SupportedControllersListWidget.addItem(item)
            if controllers[2] is True:
                item = QListWidgetItem()
                item.setText(f"Classic Controller")
                item.setIcon(QIcon(resource_path(f"assets/gui/icons/controllers/ClassicController.png")))
                item.setToolTip("This app can be used with a Classic Controller.")
                self.ui.SupportedControllersListWidget.addItem(item)
            if controllers[3] is True:
                item = QListWidgetItem()
                item.setText(f"GameCube Controller")
                item.setIcon(QIcon(resource_path(f"assets/gui/icons/controllers/GamecubeController.png")))
                item.setToolTip("This app can be used with a Gamecube Controller.")
                self.ui.SupportedControllersListWidget.addItem(item)
            if controllers[4] is True:
                item = QListWidgetItem()
                item.setText(f"Wii Zapper")
                item.setIcon(QIcon(resource_path(f"assets/gui/icons/controllers/WiiZapper.png")))
                item.setToolTip("This app can be used with a Wii Zapper.")
                self.ui.SupportedControllersListWidget.addItem(item)
            if controllers[5] is True:
                item = QListWidgetItem()
                item.setText(f"USB Keyboard")
                item.setIcon(QIcon(resource_path(f"assets/gui/icons/controllers/USBKeyboard.png")))
                item.setToolTip("This app can be used with a USB Keyboard.")
                self.ui.SupportedControllersListWidget.addItem(item)
            if controllers[6] is True:
                item = QListWidgetItem()
                item.setText(f"SDHC Card")
                item.setIcon(QIcon(resource_path(f"assets/gui/icons/controllers/SDHC.png")))
                item.setToolTip("This app is confirmed to support SDHC cards.")
                self.ui.SupportedControllersListWidget.addItem(item)

            # Version
            self.ui.version.setText(data["version"])

            # Coder
            self.ui.developer.setText(data["coder"])

            # Short Description
            if data["short_description"] == "":
                self.ui.label_description.setText("No description specified.")
            else:
                self.ui.label_description.setText(data["short_description"])

            # Long Description
            self.ui.longDescriptionBrowser.setText(data["long_description"])

            # File Name Line Edit
            self.ui.FileNameLineEdit.setText(app_name + ".zip")
            self.ui.DirectLinkLineEdit.setText(metadata.url(app_name, repo=HOST))
        self.ui.progressBar.setValue(0)
        self.repaint()
        # Load icon
        self.load_icon(app_name=app_name, repo=HOST)
        self.status_message("Ready to download")

    def view_metadata(self):
        data = self.ui.listAppsWidget.currentItem().data(Qt.UserRole)
        self.app_name = data["internal_name"]

    def trugh(self, text):
        return QObject.tr(self, text)

    def download_button(self, hbb=False):
        data = self.ui.listAppsWidget.currentItem().data(Qt.UserRole)
        self.app_name = data["internal_name"]
        self.status_message(f"Downloading {self.app_name} from Open Shop Channel..")

        if self.sender():
            object_name = self.sender().objectName()
        else:
            object_name = None

        # determine if should ask for path
        if (object_name != "WiiLoadButton") and not self.test_mode:
            if hbb:
                path_to_file, _ = QFileDialog.getSaveFileName(None, 'Save Homebrew Browser', "homebrew_browser_v0.3.9e.zip")
            else:
                path_to_file, _ = QFileDialog.getSaveFileName(None, 'Save Application', self.ui.FileNameLineEdit.text())
            output = path_to_file
        else:
            if hbb:
                output = f"homebrew_browser_v0.3.9e.zip"
            else:
                output = f"{self.app_name}.zip"
        self.ui.progressBar.setValue(0)
        if output != '':
            # get url to app
            if hbb:
                url = "https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip"
            else:
                url = download.get_url(app_name=self.app_name, repo=HOST)
            # stream file, so I can iterate
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            # set progress bar
            self.ui.progressBar.setMaximum(total_size)
            block_size = 1024
            if response.status_code == 200:
                # disable download button
                self.ui.ViewMetadataBtn.setEnabled(False)
                self.ui.WiiLoadButton.setEnabled(False)
                self.ui.ReposComboBox.setEnabled(False)
                # disable apps list
                self.ui.listAppsWidget.setEnabled(False)
                with open(output, "wb") as app_data_file:
                    for data in response.iter_content(block_size):
                        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1024)
                        if hbb:
                            self.status_message(f"Downloading Homebrew Browser from Open Shop Channel.. ({metadata.file_size(self.ui.progressBar.value())}/{metadata.file_size(total_size)})")
                        else:
                            self.status_message(f"Downloading {self.app_name} from Open Shop Channel.. ({metadata.file_size(self.ui.progressBar.value())}/{metadata.file_size(total_size)})")
                        try:
                            app.processEvents()
                        except NameError:
                            pass
                        app_data_file.write(data)

            self.ui.progressBar.setValue(100)
            self.ui.progressBar.setMaximum(100)
            self.ui.ViewMetadataBtn.setEnabled(True)
            self.ui.WiiLoadButton.setEnabled(True)
            self.ui.listAppsWidget.setEnabled(True)
            self.ui.ReposComboBox.setEnabled(True)
            self.status_message(f"Download success! Output: {output}")
            return output
        else:
            self.ui.progressBar.setValue(0)
            self.ui.ViewMetadataBtn.setEnabled(True)
            self.ui.WiiLoadButton.setEnabled(True)
            self.ui.listAppsWidget.setEnabled(True)
            self.ui.ReposComboBox.setEnabled(True)
            self.status_message("Cancelled Download.")

    def wiiload_button(self):
        data = self.ui.listAppsWidget.currentItem().data(Qt.UserRole)
        app_name = data["internal_name"]
        app_display_name = data["display_name"]

        ip, ok = QInputDialog.getText(self, 'Send to Wii: Enter IP address',
                                      'Enter the IP address of your Wii.\n'
                                      'The selected app will be sent through the network to your Wii.\n\n'
                                      f'App to send: {app_display_name}\n\n'
                                      'To find your Wii\'s IP address:\n'
                                      '1) Enter the Homebrew Channel.\n'
                                      '2) Press the home button on the Wii Remote.\n'
                                      '3) Copy the IP address written in the top left corner.\n\n'
                                      'IP address (e.g. 192.168.1...):',
                                      QLineEdit.Normal)
        if not ok:
            return

        ip_match = wiiload.validate_ip_regex(ip)

        if ip_match is None:
            logging.warning('Invalid IP Address: ' + ip)
            QMessageBox.warning(self, 'Invalid IP Address', 'This IP address is invalid.')
            return

        self.status_message("Downloading " + app_name + " from Open Shop Channel..")
        self.ui.progressBar.setValue(25)

        # get app
        path_to_app = self.download_button()

        with open(path_to_app, 'rb') as f:
            content = f.read()

        zipped_app = io.BytesIO(content)
        zip_buf = io.BytesIO()

        # Our zip file should only contain one directory with the app data in it,
        # but the downloaded file contains an apps/ directory. We're removing that here.
        wiiload.organize_zip(zipped_app, zip_buf)

        # preparing
        prep = wiiload.prepare(zip_buf)

        file_size = prep[0]
        compressed_size = prep[1]
        chunks = prep[2]

        # connecting
        self.status_message('Connecting to the HBC...')
        self.ui.progressBar.setValue(50)

        try:
            conn = wiiload.connect(ip)
        except socket.error as e:
            logging.error('Error while connecting to the HBC. Please check the IP address and try again.')
            QMessageBox.warning(self, 'Connection error',
                                'Error while connecting to the HBC. Please check the IP address and try again.')
            print(f'WiiLoad: {e}')
            self.ui.progressBar.setValue(0)
            self.status_message('Error: Could not connect to the Homebrew Channel. :(')

            # delete application zip file
            os.remove(path_to_app)

            return

        wiiload.handshake(conn, compressed_size, file_size)

        # Sending file
        self.status_message('Sending app...')

        chunk_num = 1
        for chunk in chunks:
            conn.send(chunk)

            chunk_num += 1
            progress = round(chunk_num / len(chunks) * 50) + 50
            self.ui.progressBar.setValue(progress)
            try:
                app.processEvents()
            except NameError:
                pass

        file_name = f'{app_name}.zip'
        conn.send(bytes(file_name, 'utf-8') + b'\x00')

        # delete application zip file
        os.remove(path_to_app)

        self.ui.progressBar.setValue(100)
        self.status_message('App transmitted!')
        logging.info(f"App transmitted to HBC at {ip}")

    def copy_download_link_button(self):
        data = self.ui.listAppsWidget.currentItem().data(Qt.UserRole)
        QApplication.clipboard().setText(metadata.url(data['internal_name'], repo=HOST))
        self.status_message(f"Copied the download link for \"{data['display_name']}\" to clipboard")

    def changed_host(self):
        global HOST
        global HOST_NAME
        index = self.ui.ReposComboBox.currentIndex()
        self.repo_data = self.ui.ReposComboBox.itemData(index, Qt.UserRole)
        HOST = self.repo_data[1]
        HOST_NAME = self.repo_data[3]
        self.ui.RepositoryNameLabel.setText(self.repo_data[0])
        self.ui.RepositoryDescLabel.setText(self.repo_data[2])
        self.status_message(f"Loading {HOST} repository..")
        logging.info(f"Loading {HOST}")
        self.repopulate()

    def repopulate(self):
        # Make sure everything is hidden / shown
        self.ui.ReturnToMainBtn.setHidden(True)
        self.ui.CategoriesComboBox.setHidden(False)
        self.ui.ReposComboBox.setHidden(False)
        self.ui.RepositoryLabel.setHidden(False)

        self.ui.SearchBar.setText("")

        self.status_message("Reloading list..")
        index = self.ui.ReposComboBox.currentIndex()
        repo_data = self.ui.ReposComboBox.itemData(index, Qt.UserRole)
        self.ui.RepositoryNameLabel.setText(repo_data[0])
        self.ui.RepositoryDescLabel.setText(repo_data[2])
        try:
            self.ui.CategoriesComboBox.currentIndexChanged.disconnect(self.changed_category)
        except Exception:
            pass
        self.ui.CategoriesComboBox.setCurrentIndex(0)
        self.ui.listAppsWidget.clear()
        self.populate_list()
        self.ui.CategoriesComboBox.currentIndexChanged.connect(self.changed_category)

    def populate_list(self, category="all", coder=None):
        try:
            try:
                if not splash.isHidden():
                    splash.showMessage(f"Connecting to server..", color=splash_color)
            except NameError:
                pass

            # Get apps json
            loaded_json = metadata.get_apps(host_name=HOST_NAME, category=category, coder=coder)
            i = 0

            for package in loaded_json:
                try:
                    self.ui.listAppsWidget.addItem(f"{package['display_name']}\n"
                                                   f"{metadata.file_size(package['extracted'])} | "
                                                   f"{package['version']} | "
                                                   f"{package['coder']} | "
                                                   f"{package['short_description']}")
                    list_item = self.ui.listAppsWidget.item(i)

                    list_item.setData(Qt.UserRole, package)
                    # Set category icon
                    category = package["category"]
                    if category == "utilities":
                        list_item.setIcon(QIcon(resource_path("assets/gui/icons/category/utility.png")))
                    elif category == "games":
                        list_item.setIcon(QIcon(resource_path("assets/gui/icons/category/game.png")))
                    elif category == "emulators":
                        list_item.setIcon(QIcon(resource_path("assets/gui/icons/category/emulator.png")))
                    elif category == "media":
                        list_item.setIcon(QIcon(resource_path("assets/gui/icons/category/media.png")))
                    elif category == "demos":
                        list_item.setIcon(QIcon(resource_path("assets/gui/icons/category/demo.png")))
                    try:
                        if not splash.isHidden():
                            splash.showMessage(f"Loaded {i} apps..", color=splash_color)
                    except NameError:
                        pass
                    i += 1
                except IndexError:
                    pass
            self.sort_list_alphabetically()
            self.ui.listAppsWidget.setCurrentRow(0)
            self.ui.AppsAmountLabel.setText(str(self.ui.listAppsWidget.count()) + " Apps")

        except Exception as e:
            QMessageBox.critical(self, 'OSCDL: Critical Network Error',
                                 'Could not connect to the Open Shop Channel server.\n'
                                 'Cannot continue. :(\n'
                                 'Please check your internet connection, or report this incident.\n\n'
                                 f'{e}')
            sys.exit(1)

    # Actions
    # Enable log
    def turn_log_on(self):
        logging.basicConfig(filename='oscdl-gui.log', level=logging.DEBUG,
                            format="%(asctime)s | %(levelname)s:%(name)s:%(message)s")
        logging.info('User chose to enable log file. Hello there!')
        logging.info("OSCDL v" + DISPLAY_VERSION + ": Running on " + updater.get_type())
        self.status_message('DEBUG: Enabled log file. To disable, exit the program.')
        self.ui.actionEnable_Log_File.setDisabled(True)
        self.ui.actionClear_Log.setEnabled(True)
        self.ui.actionClear_Log.triggered.connect(self.clear_log)

    # Clear log file
    def clear_log(self):
        open("oscdl-gui.log", 'w').close()
        self.status_message('DEBUG: Removed / cleared log file.')

    # Sort apps in app list in alphabetical, ascending order.
    def sort_list_alphabetically(self):
        self.ui.listAppsWidget.sortItems(Qt.AscendingOrder)

    # Download Homebrew Browser
    def download_latest_hbb_action(self):
        self.download_button(hbb=True)

    # Check for updates dialog
    def check_for_updates_action(self):
        self.status_message("Checking for updates.. This will take a few moments..")
        if updater.check_update() is True:
            latest = updater.latest_version()
            self.status_message("New version available! (" + updater.latest_version() + ") OSCDL is out of date.")
            QMessageBox.warning(self, 'OSCDL is out of date',
                                'Please go to the GitHub page and obtain the latest release\n'
                                'Newest Version: ' + latest)
        else:
            self.status_message("OSCDL is up to date!")
            QMessageBox.information(self, 'OSCDL is up to date',
                                    'You are running the latest version of OSCDL!\n')

    # In case OSC gods are angry
    def close_the_shop(self):
        # Close the shop
        self.ui.listAppsWidget.setDisabled(True)
        self.ui.ViewMetadataBtn.setDisabled(True)
        self.ui.WiiLoadButton.setDisabled(True)
        self.ui.progressBar.setDisabled(True)
        self.ui.ExtractAppCheckbox.setDisabled(True)
        self.ui.menubar.setDisabled(True)
        self.ui.ReposComboBox.setDisabled(True)
        self.ui.CategoriesComboBox.setDisabled(True)
        self.ui.SupportedControllersListWidget.setDisabled(True)
        self.ui.SearchBar.setDisabled(True)
        logging.critical('OSC GODS:CLOSED THE SHOP')
        self.status_message("The shop is now closed")

    # Load app icon
    def load_icon(self, app_name, repo):
        # Gets raw image data from server
        data = metadata.icon(app_name=app_name, repo=repo)

        # Loads image
        image = QtGui.QImage()
        image.loadFromData(data)

        # Adds image to label
        lbl = self.ui.HomebrewIconLabel
        lbl.setPixmap(QtGui.QPixmap(image))
        lbl.show()

    def load_announcement_banner(self):
        try:
            if not splash.isHidden():
                splash.showMessage(f"Finishing (3/3) - Checking for announcements..", color=splash_color)
        except NameError:
            pass
        try:
            announcement = updater.get_announcement()
            announcement_label = announcement[0]
            announcement_url_label = announcement[1]
            announcement_banner_color = announcement[2]
            announcement_banner_text_color = announcement[3]
            announcement_website_enabled = announcement[4]
            if announcement is not None:
                # Un-hide banner
                self.ui.announcement.setHidden(False)

                # Set banner styling
                self.ui.announcement.setStyleSheet(f'QFrame {{'
                                                   f'background-color: {announcement_banner_color};'
                                                   f'color: {announcement_banner_text_color};'
                                                   f'}}')

                # Populate banner
                self.ui.announcementLabel.setText(announcement_label)
                self.ui.announcementURLLabel.setText(announcement_url_label)

                if announcement_website_enabled is False:
                    self.ui.announcementURLLabel.setHidden(True)

        except Exception:
            pass

    def search_bar(self):
        text = self.ui.SearchBar.text()
        n = 0
        results = []

        # ! not part of search - joke
        if text == "wii bric":
            self.ui.listAppsWidget.clear()
            item = QListWidgetItem()
            item.setText("Wii Pong\n"
                         "9.000MiB | 9.0.0.0 | Danbo | Wii Pong")
            item.setIcon(QIcon(resource_path("assets/gui/icons/bricks.png")))
            self.ui.listAppsWidget.addItem(item)
            self.close_the_shop()
            return

        # Filter items with search term
        for i in self.ui.listAppsWidget.findItems(text, Qt.MatchContains):
            if self.current_category == "all" and (self.current_developer in i.data(Qt.UserRole)["coder"]):
                results.append(i.text())
                n += 1
            elif i.data(Qt.UserRole)["category"] == self.current_category and (self.current_developer in i.data(Qt.UserRole)["coder"]):
                results.append(i.text())
                n += 1
            else:
                pass

        # Get All Items
        for i in self.ui.listAppsWidget.findItems("", Qt.MatchContains):
            # Hide and unhide!
            if i.text() in results:
                i.setHidden(False)
            else:
                i.setHidden(True)
        if text == "":
            if n == 1:
                self.ui.AppsAmountLabel.setText(f"{n} App")
            else:
                self.ui.AppsAmountLabel.setText(f"{n} Apps")
        else:
            if n == 1:
                self.ui.AppsAmountLabel.setText(f"{n} Result")
            else:
                self.ui.AppsAmountLabel.setText(f"{n} Results")

    # When a different category is selected
    def changed_category(self):

        if self.ui.CategoriesComboBox.currentText() == "All Apps":
            self.current_category = "all"
        else:
            self.current_category = self.ui.CategoriesComboBox.currentText().lower()

        # hide anything from a different category
        for i in range(self.ui.listAppsWidget.count()):
            item = self.ui.listAppsWidget.item(i)
            if self.current_category == "all":
                item.setHidden(False)
            elif item.data(Qt.UserRole)["category"] != self.current_category:
                item.setHidden(True)
            else:
                item.setHidden(False)

        # count apps
        self.search_bar()

    # Load developer profile
    def developer_profile(self):
        self.current_developer = self.ui.developer.text()

        self.ui.SearchBar.setText("")

        # Set category
        self.ui.CategoriesComboBox.setCurrentIndex(0)

        # Hide unneeded elements
        self.ui.CategoriesComboBox.setHidden(True)
        self.ui.ReposComboBox.setHidden(True)
        self.ui.RepositoryLabel.setHidden(True)
        self.ui.ReturnToMainBtn.setHidden(False)
        self.ui.ViewDevWebsite.setHidden(False)

        # Set information
        self.ui.RepositoryNameLabel.setText(f"Developer Profile: {self.current_developer}")
        self.ui.RepositoryDescLabel.setText(f"Showing all apps made by the developer \"{self.current_developer}\".")

        # Set website URL
        self.ui.ViewDevWebsite.setText(f'<a href="https://oscwii.org/library?coder={self.current_developer}">'
                                       f'<span style=" text-decoration: underline; color:#0000ff;">Profile on '
                                       f'Website</span></a>')

        # hide anything from a different coder
        for i in range(self.ui.listAppsWidget.count()):
            item = self.ui.listAppsWidget.item(i)
            if item.data(Qt.UserRole)["coder"] != self.current_developer:
                item.setHidden(True)

        # count apps
        self.search_bar()

    # Return from developer view to normal view
    def return_to_all_apps_btn(self):
        # Unhide unneeded elements
        self.ui.ReturnToMainBtn.setHidden(True)
        self.ui.ViewDevWebsite.setHidden(True)
        self.ui.CategoriesComboBox.setHidden(False)
        self.ui.ReposComboBox.setHidden(False)
        self.ui.RepositoryLabel.setHidden(False)

        # set repo title and description
        self.ui.RepositoryNameLabel.setText(self.repo_data[0])
        self.ui.RepositoryDescLabel.setText(self.repo_data[2])

        self.current_developer = ""

        # show all items
        for i in range(self.ui.listAppsWidget.count()):
            item = self.ui.listAppsWidget.item(i)
            item.setHidden(False)

        # count apps
        self.search_bar()

    # Select theme dialog
    def select_theme_action(self):
        path = resource_path("assets/themes")
        theme_files = [f for f in listdir(path) if isfile(join(path, f))]

        theme, ok = QInputDialog.getItem(self, "Experimental: Select Theme",
                                         "Choose theme to use from the list", theme_files, 0, False)
        if not ok:
            return

        with open(resource_path(f"assets/themes/{theme}"), "r") as fh:
            self.setStyleSheet(fh.read())

    # Set default stylesheet
    def populate_stylesheets(self):
        # Developer Profile Button
        self.ui.developer_profile_btn.setStyleSheet(f"""
        QPushButton {{
            border: none;
            background: none;
        }}

        QPushButton:hover {{
            color: #0078D7;
        }}
        """)


if __name__ == "__main__":
    global app
    app = QApplication()

    global splash
    global splash_color

    # Splash
    image = QtGui.QImage(resource_path("assets/gui/splash.png"))
    splash_color = QColor("White")
    splash = QSplashScreen(QtGui.QPixmap(image))
    splash.show()

    window = MainWindow()
    window.show()
    splash.hide()
    app.exec_()
