# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'united.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


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
        MainWindow.setStyleSheet(u"")
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionAbout_OSC_DL = QAction(MainWindow)
        self.actionAbout_OSC_DL.setObjectName(u"actionAbout_OSC_DL")
        self.actionAbout_OSC_DL.setEnabled(False)
        self.actionEnable_Log_File = QAction(MainWindow)
        self.actionEnable_Log_File.setObjectName(u"actionEnable_Log_File")
        self.actionEnable_Log_File.setCheckable(True)
        self.actionClear_Log = QAction(MainWindow)
        self.actionClear_Log.setObjectName(u"actionClear_Log")
        self.actionClear_Log.setEnabled(False)
        self.actionDownload_HBB_Client_Latest = QAction(MainWindow)
        self.actionDownload_HBB_Client_Latest.setObjectName(u"actionDownload_HBB_Client_Latest")
        self.actionCheck_for_Updates = QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName(u"actionCheck_for_Updates")
        self.actionClose_the_shop = QAction(MainWindow)
        self.actionClose_the_shop.setObjectName(u"actionClose_the_shop")
        self.actionDisplay_Banner = QAction(MainWindow)
        self.actionDisplay_Banner.setObjectName(u"actionDisplay_Banner")
        self.actionLoad_Collection = QAction(MainWindow)
        self.actionLoad_Collection.setObjectName(u"actionLoad_Collection")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.actionSelect_Theme = QAction(MainWindow)
        self.actionSelect_Theme.setObjectName(u"actionSelect_Theme")
        self.actionIcons_provided_by = QAction(MainWindow)
        self.actionIcons_provided_by.setObjectName(u"actionIcons_provided_by")
        self.actionIcons_provided_by.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.AppsLibraryBox = QGroupBox(self.centralwidget)
        self.AppsLibraryBox.setObjectName(u"AppsLibraryBox")
        self.verticalLayout = QVBoxLayout(self.AppsLibraryBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 4, -1, -1)
        self.LibraryContentFrame = QFrame(self.AppsLibraryBox)
        self.LibraryContentFrame.setObjectName(u"LibraryContentFrame")
        self.verticalLayout_2 = QVBoxLayout(self.LibraryContentFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LibraryTopFrame = QFrame(self.LibraryContentFrame)
        self.LibraryTopFrame.setObjectName(u"LibraryTopFrame")
        self.LibraryTopFrame.setMaximumSize(QSize(16777215, 45))
        self.LibraryTopFrame.setFrameShape(QFrame.NoFrame)
        self.LibraryTopFrame.setFrameShadow(QFrame.Plain)
        self.LibraryTopFrame.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.LibraryTopFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.LibraryTopFrameTop = QFrame(self.LibraryTopFrame)
        self.LibraryTopFrameTop.setObjectName(u"LibraryTopFrameTop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LibraryTopFrameTop.sizePolicy().hasHeightForWidth())
        self.LibraryTopFrameTop.setSizePolicy(sizePolicy1)
        self.LibraryTopFrameTop.setMaximumSize(QSize(16777215, 25))
        self.LibraryTopFrameTop.setFrameShape(QFrame.NoFrame)
        self.LibraryTopFrameTop.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.LibraryTopFrameTop)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.RepositoryNameLabel = QLabel(self.LibraryTopFrameTop)
        self.RepositoryNameLabel.setObjectName(u"RepositoryNameLabel")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RepositoryNameLabel.setFont(font)
        self.RepositoryNameLabel.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.RepositoryNameLabel)

        self.RepositoryLabel = QLabel(self.LibraryTopFrameTop)
        self.RepositoryLabel.setObjectName(u"RepositoryLabel")
        self.RepositoryLabel.setMinimumSize(QSize(60, 0))
        self.RepositoryLabel.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.RepositoryLabel)

        self.ReposComboBox = QComboBox(self.LibraryTopFrameTop)
        self.ReposComboBox.setObjectName(u"ReposComboBox")
        self.ReposComboBox.setEnabled(True)
        self.ReposComboBox.setMinimumSize(QSize(161, 21))
        self.ReposComboBox.setMaximumSize(QSize(161, 16777215))

        self.horizontalLayout_3.addWidget(self.ReposComboBox)

        self.CategoriesComboBox = QComboBox(self.LibraryTopFrameTop)
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.setObjectName(u"CategoriesComboBox")
        self.CategoriesComboBox.setMinimumSize(QSize(70, 21))
        self.CategoriesComboBox.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_3.addWidget(self.CategoriesComboBox)

        self.ReturnToMainBtn = QPushButton(self.LibraryTopFrameTop)
        self.ReturnToMainBtn.setObjectName(u"ReturnToMainBtn")
        self.ReturnToMainBtn.setMaximumSize(QSize(161, 16777215))
        self.ReturnToMainBtn.setVisible(False)

        self.horizontalLayout_3.addWidget(self.ReturnToMainBtn)


        self.verticalLayout_4.addWidget(self.LibraryTopFrameTop)

        self.LibraryTopFrameBottom = QFrame(self.LibraryTopFrame)
        self.LibraryTopFrameBottom.setObjectName(u"LibraryTopFrameBottom")
        self.LibraryTopFrameBottom.setFrameShape(QFrame.NoFrame)
        self.LibraryTopFrameBottom.setFrameShadow(QFrame.Plain)
        self.LibraryTopFrameBottom.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.LibraryTopFrameBottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.RepositoryDescLabel = QLabel(self.LibraryTopFrameBottom)
        self.RepositoryDescLabel.setObjectName(u"RepositoryDescLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.RepositoryDescLabel.sizePolicy().hasHeightForWidth())
        self.RepositoryDescLabel.setSizePolicy(sizePolicy2)
        self.RepositoryDescLabel.setMaximumSize(QSize(16777215, 16777215))
        self.RepositoryDescLabel.setLineWidth(0)

        self.horizontalLayout.addWidget(self.RepositoryDescLabel)

        self.AppsAmountLabel = QLabel(self.LibraryTopFrameBottom)
        self.AppsAmountLabel.setObjectName(u"AppsAmountLabel")
        self.AppsAmountLabel.setMaximumSize(QSize(60, 16777215))
        self.AppsAmountLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.AppsAmountLabel)


        self.verticalLayout_4.addWidget(self.LibraryTopFrameBottom)


        self.verticalLayout_2.addWidget(self.LibraryTopFrame)

        self.SearchFrame = QFrame(self.LibraryContentFrame)
        self.SearchFrame.setObjectName(u"SearchFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SearchFrame.sizePolicy().hasHeightForWidth())
        self.SearchFrame.setSizePolicy(sizePolicy3)
        self.SearchFrame.setMaximumSize(QSize(16777215, 20))
        self.SearchFrame.setFrameShape(QFrame.StyledPanel)
        self.SearchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.SearchFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SearchBar = QLineEdit(self.SearchFrame)
        self.SearchBar.setObjectName(u"SearchBar")
        sizePolicy1.setHeightForWidth(self.SearchBar.sizePolicy().hasHeightForWidth())
        self.SearchBar.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.SearchBar)


        self.verticalLayout_2.addWidget(self.SearchFrame)

        self.listAppsWidget = QListWidget(self.LibraryContentFrame)
        self.listAppsWidget.setObjectName(u"listAppsWidget")
        sizePolicy1.setHeightForWidth(self.listAppsWidget.sizePolicy().hasHeightForWidth())
        self.listAppsWidget.setSizePolicy(sizePolicy1)
        self.listAppsWidget.setBaseSize(QSize(581, 281))

        self.verticalLayout_2.addWidget(self.listAppsWidget)


        self.verticalLayout.addWidget(self.LibraryContentFrame)

        self.announcement = QFrame(self.AppsLibraryBox)
        self.announcement.setObjectName(u"announcement")
        self.announcement.setMaximumSize(QSize(16777215, 21))
        self.announcement.setVisible(False)
        self.announcement.setStyleSheet(u"QFrame {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.announcement.setFrameShape(QFrame.StyledPanel)
        self.announcement.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.announcement)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 0, 3, 0)
        self.announcementLabel = QLabel(self.announcement)
        self.announcementLabel.setObjectName(u"announcementLabel")
        self.announcementLabel.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.announcementLabel)

        self.announcementURLLabel = QLabel(self.announcement)
        self.announcementURLLabel.setObjectName(u"announcementURLLabel")
        self.announcementURLLabel.setStyleSheet(u"QLabel {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.announcementURLLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.announcementURLLabel.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.announcementURLLabel)


        self.verticalLayout.addWidget(self.announcement)


        self.horizontalLayout_2.addWidget(self.AppsLibraryBox)

        self.SelectionInfoBox = QGroupBox(self.centralwidget)
        self.SelectionInfoBox.setObjectName(u"SelectionInfoBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.SelectionInfoBox.sizePolicy().hasHeightForWidth())
        self.SelectionInfoBox.setSizePolicy(sizePolicy4)
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
        self.label_version = QLabel(self.formLayoutWidget)
        self.label_version.setObjectName(u"label_version")

        self.MetaLayout.setWidget(1, QFormLayout.LabelRole, self.label_version)

        self.version = QLineEdit(self.formLayoutWidget)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(149, 20))
        self.version.setEchoMode(QLineEdit.Normal)
        self.version.setReadOnly(True)

        self.MetaLayout.setWidget(1, QFormLayout.FieldRole, self.version)

        self.label_developer = QLabel(self.formLayoutWidget)
        self.label_developer.setObjectName(u"label_developer")

        self.MetaLayout.setWidget(2, QFormLayout.LabelRole, self.label_developer)

        self.label_releasedate = QLabel(self.formLayoutWidget)
        self.label_releasedate.setObjectName(u"label_releasedate")

        self.MetaLayout.setWidget(3, QFormLayout.LabelRole, self.label_releasedate)

        self.releasedate = QLineEdit(self.formLayoutWidget)
        self.releasedate.setObjectName(u"releasedate")
        self.releasedate.setMinimumSize(QSize(149, 20))
        self.releasedate.setEchoMode(QLineEdit.Normal)
        self.releasedate.setReadOnly(True)

        self.MetaLayout.setWidget(3, QFormLayout.FieldRole, self.releasedate)

        self.label_filesize = QLabel(self.formLayoutWidget)
        self.label_filesize.setObjectName(u"label_filesize")

        self.MetaLayout.setWidget(4, QFormLayout.LabelRole, self.label_filesize)

        self.filesize = QLineEdit(self.formLayoutWidget)
        self.filesize.setObjectName(u"filesize")
        self.filesize.setMinimumSize(QSize(149, 20))
        self.filesize.setEchoMode(QLineEdit.Normal)
        self.filesize.setReadOnly(True)

        self.MetaLayout.setWidget(4, QFormLayout.FieldRole, self.filesize)

        self.appname = QLineEdit(self.formLayoutWidget)
        self.appname.setObjectName(u"appname")
        self.appname.setMinimumSize(QSize(149, 20))
        self.appname.setEchoMode(QLineEdit.Normal)
        self.appname.setReadOnly(True)

        self.MetaLayout.setWidget(0, QFormLayout.FieldRole, self.appname)

        self.label_appname = QLabel(self.formLayoutWidget)
        self.label_appname.setObjectName(u"label_appname")

        self.MetaLayout.setWidget(0, QFormLayout.LabelRole, self.label_appname)

        self.frame = QFrame(self.formLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(149, 20))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.developer = QLineEdit(self.frame)
        self.developer.setObjectName(u"developer")
        self.developer.setGeometry(QRect(0, 0, 151, 20))
        self.developer.setEchoMode(QLineEdit.Normal)
        self.developer.setReadOnly(True)
        self.developer_profile_btn = QPushButton(self.frame)
        self.developer_profile_btn.setObjectName(u"developer_profile_btn")
        self.developer_profile_btn.setGeometry(QRect(130, -1, 21, 22))
        self.developer_profile_btn.setFont(font)
        self.developer_profile_btn.setStyleSheet(u"")

        self.MetaLayout.setWidget(2, QFormLayout.FieldRole, self.frame)

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
        self.HomebrewIconLabel.setGeometry(QRect(150, 200, 128, 48))
        self.HomebrewIconLabel.setAlignment(Qt.AlignCenter)
        self.HomebrewCategoryLabel = QLabel(self.GeneralTab)
        self.HomebrewCategoryLabel.setObjectName(u"HomebrewCategoryLabel")
        self.HomebrewCategoryLabel.setGeometry(QRect(147, 10, 81, 48))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.HomebrewCategoryLabel.setFont(font1)
        self.HomebrewCategoryLabel.setAlignment(Qt.AlignCenter)
        self.HomebrewIconView = QWebEngineView(self.GeneralTab)
        self.HomebrewIconView.setObjectName(u"HomebrewIconView")
        self.HomebrewIconView.setGeometry(QRect(10, 10, 128, 48))
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
        self.DirectLinkLabel.setGeometry(QRect(10, 190, 91, 20))
        self.DirectLinkLineEdit = QLineEdit(self.RawTab)
        self.DirectLinkLineEdit.setObjectName(u"DirectLinkLineEdit")
        self.DirectLinkLineEdit.setGeometry(QRect(10, 210, 151, 20))
        self.DirectLinkLineEdit.setReadOnly(True)
        self.CopyDirectLinkBtn = QPushButton(self.RawTab)
        self.CopyDirectLinkBtn.setObjectName(u"CopyDirectLinkBtn")
        self.CopyDirectLinkBtn.setGeometry(QRect(170, 210, 61, 21))
        self.SupportedControllersLabel = QLabel(self.RawTab)
        self.SupportedControllersLabel.setObjectName(u"SupportedControllersLabel")
        self.SupportedControllersLabel.setGeometry(QRect(10, 10, 221, 16))
        self.SupportedControllersListWidget = QListWidget(self.RawTab)
        self.SupportedControllersListWidget.setObjectName(u"SupportedControllersListWidget")
        self.SupportedControllersListWidget.setGeometry(QRect(10, 30, 221, 141))
        self.SupportedControllersListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.SupportedControllersListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.SupportedControllersListWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.SupportedControllersListWidget.setMovement(QListView.Static)
        self.SupportedControllersListWidget.setGridSize(QSize(65, 65))
        self.SupportedControllersListWidget.setViewMode(QListView.IconMode)
        self.SupportedControllersListWidget.setWordWrap(True)
        self.ExtractAppCheckbox = QCheckBox(self.RawTab)
        self.ExtractAppCheckbox.setObjectName(u"ExtractAppCheckbox")
        self.ExtractAppCheckbox.setGeometry(QRect(10, 170, 271, 31))
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
        self.menuAbout.addAction(self.actionIcons_provided_by)
        self.menuDebug.addAction(self.actionEnable_Log_File)
        self.menuDebug.addAction(self.actionClear_Log)
        self.menuDebug.addSeparator()
        self.menuDebug.addAction(self.actionClose_the_shop)
        self.menuDebug.addAction(self.menuExperimental.menuAction())
        self.menuExperimental.addAction(self.menuAnnouncement_Banner.menuAction())
        self.menuExperimental.addAction(self.actionSelect_Theme)
        self.menuAnnouncement_Banner.addAction(self.actionDisplay_Banner)
        self.menuClients.addAction(self.menuHomebrew_Browser.menuAction())
        self.menuClients.addAction(self.menuOpen_Shop_Channel_DL.menuAction())
        self.menuOpen_Shop_Channel_DL.addAction(self.actionCheck_for_Updates)
        self.menuOpen_Shop_Channel_DL.addAction(self.actionRefresh)
        self.menuHomebrew_Browser.addAction(self.actionDownload_HBB_Client_Latest)

        self.retranslateUi(MainWindow)

        self.listAppsWidget.setCurrentRow(-1)
        self.tabMetadata.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Open Shop Channel Downloader - Library", None))
        self.actionAbout_OSC_DL.setText(QCoreApplication.translate("MainWindow", u"About OSC-DL", None))
        self.actionEnable_Log_File.setText(QCoreApplication.translate("MainWindow", u"Enable GUI Log File", None))
#if QT_CONFIG(shortcut)
        self.actionEnable_Log_File.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear_Log.setText(QCoreApplication.translate("MainWindow", u"Clear GUI Log", None))
        self.actionDownload_HBB_Client_Latest.setText(QCoreApplication.translate("MainWindow", u"Download HBB Client", None))
        self.actionCheck_for_Updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates", None))
        self.actionClose_the_shop.setText(QCoreApplication.translate("MainWindow", u"Close the shop", None))
        self.actionDisplay_Banner.setText(QCoreApplication.translate("MainWindow", u"Reload Banner", None))
        self.actionLoad_Collection.setText(QCoreApplication.translate("MainWindow", u"Load Collection", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh List", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_Theme.setText(QCoreApplication.translate("MainWindow", u"Select Theme", None))
        self.actionIcons_provided_by.setText(QCoreApplication.translate("MainWindow", u"Icons provided by Icons8", None))
#if QT_CONFIG(accessibility)
        self.centralwidget.setAccessibleName(QCoreApplication.translate("MainWindow", u"centralcontainer", None))
#endif // QT_CONFIG(accessibility)
        self.AppsLibraryBox.setTitle(QCoreApplication.translate("MainWindow", u"Apps Library", None))
        self.RepositoryNameLabel.setText(QCoreApplication.translate("MainWindow", u"Repository Name", None))
        self.RepositoryLabel.setText(QCoreApplication.translate("MainWindow", u"Repository:", None))
        self.CategoriesComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Apps", None))
        self.CategoriesComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.CategoriesComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Emulators", None))
        self.CategoriesComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Games", None))
        self.CategoriesComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Media", None))
        self.CategoriesComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Demos", None))

        self.ReturnToMainBtn.setText(QCoreApplication.translate("MainWindow", u"Return to All Apps", None))
        self.RepositoryDescLabel.setText(QCoreApplication.translate("MainWindow", u"Repository Description", None))
        self.AppsAmountLabel.setText(QCoreApplication.translate("MainWindow", u"0 Apps", None))
        self.SearchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Applications..", None))
        self.announcementLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Announcement Header: </span>Announcement Content.</p></body></html>", None))
        self.announcementURLLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://google.com\"><span style=\" text-decoration: underline; color:#ffff00;\">Announcement URL</span></a></p></body></html>", None))
        self.SelectionInfoBox.setTitle(QCoreApplication.translate("MainWindow", u"Application Metadata", None))
#if QT_CONFIG(accessibility)
        self.GeneralTab.setAccessibleName(QCoreApplication.translate("MainWindow", u"tabcontent", None))
#endif // QT_CONFIG(accessibility)
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_developer.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.label_releasedate.setText(QCoreApplication.translate("MainWindow", u"Release Date", None))
        self.label_filesize.setText(QCoreApplication.translate("MainWindow", u"File Size", None))
        self.appname.setText("")
        self.appname.setPlaceholderText("")
        self.label_appname.setText(QCoreApplication.translate("MainWindow", u"App Name", None))
        self.developer_profile_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_displayname.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.HomebrewIconLabel.setText(QCoreApplication.translate("MainWindow", u"No homebrew icon. Aw.", None))
        self.HomebrewCategoryLabel.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.GeneralTab), QCoreApplication.translate("MainWindow", u"General", None))
#if QT_CONFIG(accessibility)
        self.Description.setAccessibleName(QCoreApplication.translate("MainWindow", u"tabcontent", None))
#endif // QT_CONFIG(accessibility)
        self.longDescriptionBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cantarell'; font-size:10pt;\">         </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p></body></html>", None))
        self.LongDescLabel.setText(QCoreApplication.translate("MainWindow", u"Long Description", None))
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.Description), QCoreApplication.translate("MainWindow", u"Description", None))
#if QT_CONFIG(accessibility)
        self.RawTab.setAccessibleName(QCoreApplication.translate("MainWindow", u"tabcontent", None))
#endif // QT_CONFIG(accessibility)
        self.DirectLinkLabel.setText(QCoreApplication.translate("MainWindow", u"Direct Link", None))
        self.CopyDirectLinkBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.SupportedControllersLabel.setText(QCoreApplication.translate("MainWindow", u"Supported Peripherals:", None))
        self.ExtractAppCheckbox.setText(QCoreApplication.translate("MainWindow", u"Extract Downloaded App", None))
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.RawTab), QCoreApplication.translate("MainWindow", u"Peripherals", None))
        self.FileNameLabel.setText(QCoreApplication.translate("MainWindow", u"Output File", None))
        self.ViewMetadataBtn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.WiiLoadButton.setText(QCoreApplication.translate("MainWindow", u"Send to Wii", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuDebug.setTitle(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.menuExperimental.setTitle(QCoreApplication.translate("MainWindow", u"Experimental", None))
        self.menuAnnouncement_Banner.setTitle(QCoreApplication.translate("MainWindow", u"Announcement Banner", None))
        self.menuClients.setTitle(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.menuOpen_Shop_Channel_DL.setTitle(QCoreApplication.translate("MainWindow", u"Open Shop Channel DL", None))
        self.menuHomebrew_Browser.setTitle(QCoreApplication.translate("MainWindow", u"Homebrew Browser", None))
    # retranslateUi

