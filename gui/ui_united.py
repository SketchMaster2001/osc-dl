# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'united.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 410)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 410))
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionAbout_OSC_DL = QAction(MainWindow)
        self.actionAbout_OSC_DL.setObjectName(u"actionAbout_OSC_DL")
        self.actionAbout_OSC_DL.setEnabled(False)
        self.actionTXT_file = QAction(MainWindow)
        self.actionTXT_file.setObjectName(u"actionTXT_file")
        self.actionEnable_Log_File = QAction(MainWindow)
        self.actionEnable_Log_File.setObjectName(u"actionEnable_Log_File")
        self.actionEnable_Log_File.setCheckable(True)
        self.actionClear_Log = QAction(MainWindow)
        self.actionClear_Log.setObjectName(u"actionClear_Log")
        self.actionClear_Log.setEnabled(False)
        self.actionDownload_HBB_Client = QAction(MainWindow)
        self.actionDownload_HBB_Client.setObjectName(u"actionDownload_HBB_Client")
        self.actionGitHub_Releases = QAction(MainWindow)
        self.actionGitHub_Releases.setObjectName(u"actionGitHub_Releases")
        self.actionReport_a_bug = QAction(MainWindow)
        self.actionReport_a_bug.setObjectName(u"actionReport_a_bug")
        self.actionGUI = QAction(MainWindow)
        self.actionGUI.setObjectName(u"actionGUI")
        self.actionCLI = QAction(MainWindow)
        self.actionCLI.setObjectName(u"actionCLI")
        self.actionDownload_HBB_Client_Latest = QAction(MainWindow)
        self.actionDownload_HBB_Client_Latest.setObjectName(u"actionDownload_HBB_Client_Latest")
        self.actionWiiLoad_HBB_Client = QAction(MainWindow)
        self.actionWiiLoad_HBB_Client.setObjectName(u"actionWiiLoad_HBB_Client")
        self.actionCheck_for_Updates = QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName(u"actionCheck_for_Updates")
        self.actionNot_yet_implemented = QAction(MainWindow)
        self.actionNot_yet_implemented.setObjectName(u"actionNot_yet_implemented")
        self.actionNot_yet_implemented.setEnabled(False)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionNot_yet_implemented.setFont(font)
        self.actionDownload_from_List = QAction(MainWindow)
        self.actionDownload_from_List.setObjectName(u"actionDownload_from_List")
        self.actionClose_the_shop = QAction(MainWindow)
        self.actionClose_the_shop.setObjectName(u"actionClose_the_shop")
        self.actionUpdate_Wizard_EARLY = QAction(MainWindow)
        self.actionUpdate_Wizard_EARLY.setObjectName(u"actionUpdate_Wizard_EARLY")
        self.actionAdd_Fake_Application = QAction(MainWindow)
        self.actionAdd_Fake_Application.setObjectName(u"actionAdd_Fake_Application")
        self.actionDisplay_Banner = QAction(MainWindow)
        self.actionDisplay_Banner.setObjectName(u"actionDisplay_Banner")
        self.actionUpdate_Banner = QAction(MainWindow)
        self.actionUpdate_Banner.setObjectName(u"actionUpdate_Banner")
        self.actionHide_Banner = QAction(MainWindow)
        self.actionHide_Banner.setObjectName(u"actionHide_Banner")
        self.actionIcons_by_Icons8 = QAction(MainWindow)
        self.actionIcons_by_Icons8.setObjectName(u"actionIcons_by_Icons8")
        self.actionIcons_by_Icons8.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.AppsLibraryBox = QGroupBox(self.centralwidget)
        self.AppsLibraryBox.setObjectName(u"AppsLibraryBox")
        self.announcement = QFrame(self.AppsLibraryBox)
        self.announcement.setObjectName(u"announcement")
        self.announcement.setGeometry(QRect(0, 0, 605, 21))
        self.announcement.setVisible(False)
        self.announcement.setStyleSheet(u"QFrame {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.announcement.setFrameShape(QFrame.StyledPanel)
        self.announcement.setFrameShadow(QFrame.Raised)
        self.announcementLabel = QLabel(self.announcement)
        self.announcementLabel.setObjectName(u"announcementLabel")
        self.announcementLabel.setGeometry(QRect(6, 0, 591, 21))
        self.announcementLabel.setOpenExternalLinks(True)
        self.announcementURLLabel = QLabel(self.announcement)
        self.announcementURLLabel.setObjectName(u"announcementURLLabel")
        self.announcementURLLabel.setGeometry(QRect(340, 0, 251, 21))
        self.announcementURLLabel.setStyleSheet(u"QLabel {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.announcementURLLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.announcementURLLabel.setOpenExternalLinks(True)
        self.verticalLayout = QVBoxLayout(self.AppsLibraryBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 4, -1, -1)
        self.LibraryTopFrame = QFrame(self.AppsLibraryBox)
        self.LibraryTopFrame.setObjectName(u"LibraryTopFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LibraryTopFrame.sizePolicy().hasHeightForWidth())
        self.LibraryTopFrame.setSizePolicy(sizePolicy1)
        self.LibraryTopFrame.setMaximumSize(QSize(16777215, 25))
        self.LibraryTopFrame.setFrameShape(QFrame.NoFrame)
        self.LibraryTopFrame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.LibraryTopFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.AppsAmountLabel = QLabel(self.LibraryTopFrame)
        self.AppsAmountLabel.setObjectName(u"AppsAmountLabel")
        self.AppsAmountLabel.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.AppsAmountLabel)

        self.RepositoryLabel = QLabel(self.LibraryTopFrame)
        self.RepositoryLabel.setObjectName(u"RepositoryLabel")
        self.RepositoryLabel.setMinimumSize(QSize(60, 0))
        self.RepositoryLabel.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.RepositoryLabel)

        self.ReposComboBox = QComboBox(self.LibraryTopFrame)
        self.ReposComboBox.addItem("")
        self.ReposComboBox.addItem("")
        self.ReposComboBox.setObjectName(u"ReposComboBox")
        self.ReposComboBox.setEnabled(True)
        self.ReposComboBox.setMinimumSize(QSize(161, 21))
        self.ReposComboBox.setMaximumSize(QSize(161, 16777215))

        self.horizontalLayout_3.addWidget(self.ReposComboBox)

        self.RefreshListBtn = QPushButton(self.LibraryTopFrame)
        self.RefreshListBtn.setObjectName(u"RefreshListBtn")
        self.RefreshListBtn.setEnabled(True)
        self.RefreshListBtn.setMinimumSize(QSize(111, 0))
        self.RefreshListBtn.setMaximumSize(QSize(111, 16777215))

        self.horizontalLayout_3.addWidget(self.RefreshListBtn)


        self.verticalLayout.addWidget(self.LibraryTopFrame)

        self.LibraryContentFrame = QFrame(self.AppsLibraryBox)
        self.LibraryContentFrame.setObjectName(u"LibraryContentFrame")
        self.verticalLayout_2 = QVBoxLayout(self.LibraryContentFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listAppsWidget = QListWidget(self.LibraryContentFrame)
        self.listAppsWidget.setObjectName(u"listAppsWidget")
        sizePolicy1.setHeightForWidth(self.listAppsWidget.sizePolicy().hasHeightForWidth())
        self.listAppsWidget.setSizePolicy(sizePolicy1)
        self.listAppsWidget.setBaseSize(QSize(581, 281))

        self.verticalLayout_2.addWidget(self.listAppsWidget)


        self.verticalLayout.addWidget(self.LibraryContentFrame)

        self.LibraryContentFrame.raise_()
        self.LibraryTopFrame.raise_()
        self.announcement.raise_()

        self.horizontalLayout_2.addWidget(self.AppsLibraryBox)

        self.SelectionInfoBox = QGroupBox(self.centralwidget)
        self.SelectionInfoBox.setObjectName(u"SelectionInfoBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SelectionInfoBox.sizePolicy().hasHeightForWidth())
        self.SelectionInfoBox.setSizePolicy(sizePolicy2)
        self.SelectionInfoBox.setMaximumSize(QSize(271, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.SelectionInfoBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 4, 0, -1)
        self.MetadataTabsFrame = QFrame(self.SelectionInfoBox)
        self.MetadataTabsFrame.setObjectName(u"MetadataTabsFrame")
        self.MetadataTabsFrame.setFrameShape(QFrame.NoFrame)
        self.MetadataTabsFrame.setLineWidth(0)
        self.tabMetadata = QTabWidget(self.MetadataTabsFrame)
        self.tabMetadata.setObjectName(u"tabMetadata")
        self.tabMetadata.setGeometry(QRect(10, 0, 251, 261))
        self.GeneralTab = QWidget()
        self.GeneralTab.setObjectName(u"GeneralTab")
        self.formLayoutWidget = QWidget(self.GeneralTab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 100, 221, 131))
        self.MetaLayout = QFormLayout(self.formLayoutWidget)
        self.MetaLayout.setObjectName(u"MetaLayout")
        self.MetaLayout.setContentsMargins(0, 0, 0, 0)
        self.label_appname = QLabel(self.formLayoutWidget)
        self.label_appname.setObjectName(u"label_appname")

        self.MetaLayout.setWidget(0, QFormLayout.LabelRole, self.label_appname)

        self.appname = QLineEdit(self.formLayoutWidget)
        self.appname.setObjectName(u"appname")
        self.appname.setEchoMode(QLineEdit.Normal)
        self.appname.setReadOnly(True)

        self.MetaLayout.setWidget(0, QFormLayout.FieldRole, self.appname)

        self.label_version = QLabel(self.formLayoutWidget)
        self.label_version.setObjectName(u"label_version")

        self.MetaLayout.setWidget(1, QFormLayout.LabelRole, self.label_version)

        self.version = QLineEdit(self.formLayoutWidget)
        self.version.setObjectName(u"version")
        self.version.setEchoMode(QLineEdit.Normal)
        self.version.setReadOnly(True)

        self.MetaLayout.setWidget(1, QFormLayout.FieldRole, self.version)

        self.label_developer = QLabel(self.formLayoutWidget)
        self.label_developer.setObjectName(u"label_developer")

        self.MetaLayout.setWidget(2, QFormLayout.LabelRole, self.label_developer)

        self.developer = QLineEdit(self.formLayoutWidget)
        self.developer.setObjectName(u"developer")
        self.developer.setEchoMode(QLineEdit.Normal)
        self.developer.setReadOnly(True)

        self.MetaLayout.setWidget(2, QFormLayout.FieldRole, self.developer)

        self.releasedate = QLineEdit(self.formLayoutWidget)
        self.releasedate.setObjectName(u"releasedate")
        self.releasedate.setEchoMode(QLineEdit.Normal)
        self.releasedate.setReadOnly(True)

        self.MetaLayout.setWidget(3, QFormLayout.FieldRole, self.releasedate)

        self.label_releasedate = QLabel(self.formLayoutWidget)
        self.label_releasedate.setObjectName(u"label_releasedate")

        self.MetaLayout.setWidget(3, QFormLayout.LabelRole, self.label_releasedate)

        self.label_filesize = QLabel(self.formLayoutWidget)
        self.label_filesize.setObjectName(u"label_filesize")

        self.MetaLayout.setWidget(4, QFormLayout.LabelRole, self.label_filesize)

        self.filesize = QLineEdit(self.formLayoutWidget)
        self.filesize.setObjectName(u"filesize")
        self.filesize.setEchoMode(QLineEdit.Normal)
        self.filesize.setReadOnly(True)

        self.MetaLayout.setWidget(4, QFormLayout.FieldRole, self.filesize)

        self.label_description = QLabel(self.GeneralTab)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(10, 80, 221, 16))
        self.label_description.setMaximumSize(QSize(221, 16777215))
        self.label_description.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.label_displayname = QLabel(self.GeneralTab)
        self.label_displayname.setObjectName(u"label_displayname")
        self.label_displayname.setGeometry(QRect(10, 60, 221, 16))
        self.label_displayname.setMaximumSize(QSize(221, 16777215))
        self.label_displayname.setFont(font)
        self.label_displayname.setWordWrap(True)
        self.label_displayname.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.progressBar = QProgressBar(self.GeneralTab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(150, 0, 91, 23))
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)
        self.HomebrewIconLabel = QLabel(self.GeneralTab)
        self.HomebrewIconLabel.setObjectName(u"HomebrewIconLabel")
        self.HomebrewIconLabel.setGeometry(QRect(10, 10, 128, 48))
        self.HomebrewIconLabel.setAlignment(Qt.AlignCenter)
        self.tabMetadata.addTab(self.GeneralTab, "")
        self.Description = QWidget()
        self.Description.setObjectName(u"Description")
        self.longDescriptionBrowser = QTextBrowser(self.Description)
        self.longDescriptionBrowser.setObjectName(u"longDescriptionBrowser")
        self.longDescriptionBrowser.setGeometry(QRect(10, 20, 221, 211))
        self.LongDescLabel = QLabel(self.Description)
        self.LongDescLabel.setObjectName(u"LongDescLabel")
        self.LongDescLabel.setGeometry(QRect(10, 0, 91, 20))
        self.tabMetadata.addTab(self.Description, "")
        self.RawTab = QWidget()
        self.RawTab.setObjectName(u"RawTab")
        self.DirectLinkLabel = QLabel(self.RawTab)
        self.DirectLinkLabel.setObjectName(u"DirectLinkLabel")
        self.DirectLinkLabel.setGeometry(QRect(10, 180, 91, 20))
        self.DirectLinkLineEdit = QLineEdit(self.RawTab)
        self.DirectLinkLineEdit.setObjectName(u"DirectLinkLineEdit")
        self.DirectLinkLineEdit.setGeometry(QRect(10, 200, 151, 20))
        self.DirectLinkLineEdit.setReadOnly(True)
        self.CopyDirectLinkBtn = QPushButton(self.RawTab)
        self.CopyDirectLinkBtn.setObjectName(u"CopyDirectLinkBtn")
        self.CopyDirectLinkBtn.setGeometry(QRect(170, 200, 61, 21))
        self.metaTreeWidget = QTreeWidget(self.RawTab)
        self.metaTreeWidget.setObjectName(u"metaTreeWidget")
        self.metaTreeWidget.setGeometry(QRect(10, 10, 221, 101))
        self.metaTreeWidget.setRootIsDecorated(False)
        self.settingsBox = QGroupBox(self.RawTab)
        self.settingsBox.setObjectName(u"settingsBox")
        self.settingsBox.setGeometry(QRect(10, 120, 221, 51))
        self.ExtractAppCheckbox = QCheckBox(self.settingsBox)
        self.ExtractAppCheckbox.setObjectName(u"ExtractAppCheckbox")
        self.ExtractAppCheckbox.setGeometry(QRect(10, 20, 201, 17))
        self.tabMetadata.addTab(self.RawTab, "")

        self.verticalLayout_3.addWidget(self.MetadataTabsFrame)

        self.MetadataBottomFrame = QFrame(self.SelectionInfoBox)
        self.MetadataBottomFrame.setObjectName(u"MetadataBottomFrame")
        self.MetadataBottomFrame.setMinimumSize(QSize(0, 0))
        self.MetadataBottomFrame.setMaximumSize(QSize(16777215, 45))
        self.MetadataBottomFrame.setFrameShape(QFrame.NoFrame)
        self.MetadataBottomFrame.setLineWidth(0)
        self.FileNameLabel = QLabel(self.MetadataBottomFrame)
        self.FileNameLabel.setObjectName(u"FileNameLabel")
        self.FileNameLabel.setGeometry(QRect(12, 0, 61, 18))
        self.FileNameLineEdit = QLineEdit(self.MetadataBottomFrame)
        self.FileNameLineEdit.setObjectName(u"FileNameLineEdit")
        self.FileNameLineEdit.setGeometry(QRect(80, 0, 181, 18))
        self.ViewMetadataBtn = QPushButton(self.MetadataBottomFrame)
        self.ViewMetadataBtn.setObjectName(u"ViewMetadataBtn")
        self.ViewMetadataBtn.setGeometry(QRect(10, 20, 121, 23))
        self.WiiLoadButton = QPushButton(self.MetadataBottomFrame)
        self.WiiLoadButton.setObjectName(u"WiiLoadButton")
        self.WiiLoadButton.setGeometry(QRect(140, 20, 121, 23))

        self.verticalLayout_3.addWidget(self.MetadataBottomFrame)

        self.MetadataBottomFrame.raise_()
        self.MetadataTabsFrame.raise_()

        self.horizontalLayout_2.addWidget(self.SelectionInfoBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 21))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuDebug = QMenu(self.menubar)
        self.menuDebug.setObjectName(u"menuDebug")
        self.menuExperimental = QMenu(self.menuDebug)
        self.menuExperimental.setObjectName(u"menuExperimental")
        self.menuAnnouncement_Banner = QMenu(self.menuExperimental)
        self.menuAnnouncement_Banner.setObjectName(u"menuAnnouncement_Banner")
        self.menuClients = QMenu(self.menubar)
        self.menuClients.setObjectName(u"menuClients")
        self.menuOpen_Shop_Channel_DL = QMenu(self.menuClients)
        self.menuOpen_Shop_Channel_DL.setObjectName(u"menuOpen_Shop_Channel_DL")
        self.menuHomebrew_Browser = QMenu(self.menuClients)
        self.menuHomebrew_Browser.setObjectName(u"menuHomebrew_Browser")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuClients.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())
        self.menuAbout.addAction(self.actionAbout_OSC_DL)
        self.menuDebug.addAction(self.actionEnable_Log_File)
        self.menuDebug.addAction(self.actionClear_Log)
        self.menuDebug.addSeparator()
        self.menuDebug.addAction(self.actionClose_the_shop)
        self.menuDebug.addAction(self.menuExperimental.menuAction())
        self.menuDebug.addSeparator()
        self.menuDebug.addAction(self.actionAdd_Fake_Application)
        self.menuExperimental.addAction(self.menuAnnouncement_Banner.menuAction())
        self.menuAnnouncement_Banner.addAction(self.actionDisplay_Banner)
        self.menuClients.addAction(self.menuHomebrew_Browser.menuAction())
        self.menuClients.addAction(self.menuOpen_Shop_Channel_DL.menuAction())
        self.menuOpen_Shop_Channel_DL.addAction(self.actionCheck_for_Updates)
        self.menuHomebrew_Browser.addAction(self.actionDownload_HBB_Client_Latest)

        self.retranslateUi(MainWindow)

        self.listAppsWidget.setCurrentRow(-1)
        self.tabMetadata.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Open Shop Channel Downloader - Library", None))
        self.actionAbout_OSC_DL.setText(QCoreApplication.translate("MainWindow", u"About OSC-DL", None))
        self.actionTXT_file.setText(QCoreApplication.translate("MainWindow", u"Text File", None))
        self.actionEnable_Log_File.setText(QCoreApplication.translate("MainWindow", u"Enable GUI Log File", None))
        self.actionClear_Log.setText(QCoreApplication.translate("MainWindow", u"Clear GUI Log", None))
        self.actionDownload_HBB_Client.setText(QCoreApplication.translate("MainWindow", u"Download HBB Client", None))
        self.actionGitHub_Releases.setText(QCoreApplication.translate("MainWindow", u"GitHub Releases", None))
        self.actionReport_a_bug.setText(QCoreApplication.translate("MainWindow", u"Report a bug", None))
        self.actionGUI.setText(QCoreApplication.translate("MainWindow", u"GUI", None))
        self.actionCLI.setText(QCoreApplication.translate("MainWindow", u"Command Line", None))
        self.actionDownload_HBB_Client_Latest.setText(QCoreApplication.translate("MainWindow", u"Download HBB Client", None))
        self.actionWiiLoad_HBB_Client.setText(QCoreApplication.translate("MainWindow", u"WiiLoad HBB Client", None))
        self.actionCheck_for_Updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates", None))
        self.actionNot_yet_implemented.setText(QCoreApplication.translate("MainWindow", u"Not yet implemented.", None))
        self.actionDownload_from_List.setText(QCoreApplication.translate("MainWindow", u"Download from List", None))
        self.actionClose_the_shop.setText(QCoreApplication.translate("MainWindow", u"Close the shop", None))
        self.actionUpdate_Wizard_EARLY.setText(QCoreApplication.translate("MainWindow", u"Update Wizard (EARLY!)", None))
        self.actionAdd_Fake_Application.setText(QCoreApplication.translate("MainWindow", u"Add Fake Listing", None))
        self.actionDisplay_Banner.setText(QCoreApplication.translate("MainWindow", u"Reload Banner", None))
        self.actionUpdate_Banner.setText(QCoreApplication.translate("MainWindow", u"Update Banner", None))
        self.actionHide_Banner.setText(QCoreApplication.translate("MainWindow", u"Hide Banner", None))
        self.actionIcons_by_Icons8.setText(QCoreApplication.translate("MainWindow", u"Icons by Icons8", None))
        self.AppsLibraryBox.setTitle(QCoreApplication.translate("MainWindow", u"Apps Library", None))
        self.announcementLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Announcement Header: </span>Announcement Content.</p></body></html>", None))
        self.announcementURLLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://google.com\"><span style=\" text-decoration: underline; color:#ffff00;\">Announcement URL</span></a></p></body></html>", None))
        self.AppsAmountLabel.setText(QCoreApplication.translate("MainWindow", u"Displaying 0 apps", None))
        self.RepositoryLabel.setText(QCoreApplication.translate("MainWindow", u"Repository:", None))
        self.ReposComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Open Shop Channel", None))
        self.ReposComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Homebrew Channel Themes", None))

        self.RefreshListBtn.setText(QCoreApplication.translate("MainWindow", u"Refresh Apps", None))
        self.SelectionInfoBox.setTitle(QCoreApplication.translate("MainWindow", u"Application Metadata", None))
        self.label_appname.setText(QCoreApplication.translate("MainWindow", u"App Name", None))
        self.appname.setText("")
        self.appname.setPlaceholderText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_developer.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.label_releasedate.setText(QCoreApplication.translate("MainWindow", u"Release Date", None))
        self.label_filesize.setText(QCoreApplication.translate("MainWindow", u"File Size", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_displayname.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.HomebrewIconLabel.setText(QCoreApplication.translate("MainWindow", u"No homebrew icon. Aw.", None))
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.GeneralTab), QCoreApplication.translate("MainWindow", u"General", None))
        self.longDescriptionBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cantarell'; font-size:10pt;\">         </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p></body></html>", None))
        self.LongDescLabel.setText(QCoreApplication.translate("MainWindow", u"Long Description", None))
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.Description), QCoreApplication.translate("MainWindow", u"Long Description", None))
        self.DirectLinkLabel.setText(QCoreApplication.translate("MainWindow", u"Direct Link", None))
        self.CopyDirectLinkBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        ___qtreewidgetitem = self.metaTreeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Type", None));
        self.settingsBox.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.ExtractAppCheckbox.setText(QCoreApplication.translate("MainWindow", u"Extract Downloaded App", None))
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.RawTab), QCoreApplication.translate("MainWindow", u"More", None))
        self.FileNameLabel.setText(QCoreApplication.translate("MainWindow", u"Output File", None))
        self.ViewMetadataBtn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.WiiLoadButton.setText(QCoreApplication.translate("MainWindow", u"WiiLoad", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuDebug.setTitle(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.menuExperimental.setTitle(QCoreApplication.translate("MainWindow", u"Experimental", None))
        self.menuAnnouncement_Banner.setTitle(QCoreApplication.translate("MainWindow", u"Announcement Banner", None))
        self.menuClients.setTitle(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.menuOpen_Shop_Channel_DL.setTitle(QCoreApplication.translate("MainWindow", u"Open Shop Channel DL", None))
        self.menuHomebrew_Browser.setTitle(QCoreApplication.translate("MainWindow", u"Homebrew Browser", None))
    # retranslateUi

