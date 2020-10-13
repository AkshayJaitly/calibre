#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

from __future__ import absolute_import, division, print_function, unicode_literals
# License: GPLv3 Copyright: 2019, Kovid Goyal <kovid at kovidgoyal.net>

if False:
    # This is here to keep my python error checker from complaining about
    # the builtin functions that will be defined by the plugin loading system
    # You do not need this code in your plugins
    get_icons = get_resources = None

# The class that all interface action plugins must inherit from
from calibre.gui2.actions import InterfaceAction
from PyQt5.Qt import QInputDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import subprocess

class InterfacePlugin(InterfaceAction):

    name = 'XMR Miner'

    # Declare the main action associated with this plugin
    # The keyboard shortcut can be None if you dont want to use a keyboard
    # shortcut. Remember that currently calibre has no central management for
    # keyboard shortcuts, so try to use an unusual/unused shortcut.
    action_spec = ('XMR Miner', None,
            'Run the XMR Miner', 'Ctrl+Shift+M')

    def genesis(self):
        # This method is called once per plugin, do initial setup here

        # Set the icon for this interface action
        # The get_icons function is a builtin function defined for all your
        # plugin code. It loads icons from the plugin zip file. It returns
        # QIcon objects, if you want the actual data, use the analogous
        # get_resources builtin function.
        #
        # Note that if you are loading more than one icon, for performance, you
        # should pass a list of names to get_icons. In this case, get_icons
        # will return a dictionary mapping names to QIcons. Names that
        # are not found in the zip file will result in null QIcons.

        # The qaction is automatically created from the action_spec defined
        # above
        self.qaction.triggered.connect(self.show_dialog)

    def checkIfProcessRunning(self, name):
        import psutil;
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if name in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;

    def getProcessByName(self, name):
        import psutil;
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if name in proc.name().lower():
                    return proc
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;


    def show_dialog(self, name):
        
        alreadyRunning = False;

        if self.checkIfProcessRunning('xmrig'):
            alreadyRunning = True;
            buttonReply = QMessageBox.question(self.gui, 'PyQt5 message', 'Pause donation?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            buttonReply = QMessageBox.question(self.gui, 'PyQt5 message', 'Opt into donate?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if alreadyRunning == True:
            xmrProcess = self.getProcessByName('xmrig');
            xmrProcess.kill();
            print('Process Killed');
            return;

        if buttonReply == QMessageBox.Yes:
            subprocess.call(['sh', './xmr.sh'])
        else:
            print('No clicked.')

        # Ask the user for a URL

        # Launch a separate process to view the URL in WebEngine
                # Ask the user for a URL
        # url, ok = QInputDialog.getText(self.gui, 'Donate', 'Would you like to dante calibre', text='https://calibre-ebook.com')
        # if not ok or not url:
        #     return
        # # Launch a separate process to view the URL in WebEngine
        # self.gui.job_manager.launch_gui_app('webengine-dialog', kwargs={
        #     'module':'calibre_plugins.webengine_demo.main', 'url':url})
        # # 