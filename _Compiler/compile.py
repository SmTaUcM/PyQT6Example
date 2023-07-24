#--------------------------------------------------------------------------------------------------
# Name:        compile.py
# Purpose:     Used to compile filename.py into filename.exe.
# Version:     v1.00
# Author:      Stuart. Macintosh
#
# Created:     24/07/2023
# Copyright:   (c) Stuart Macintosh 2023
# Licence:     Open Source
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
#                                            Settings
#--------------------------------------------------------------------------------------------------
APP_NAME = "UI File Without Conversion QT6"
APP_PYTHON_FILE = "UI File Without Conversion QT6.py"
ICON_FILE = "example.ico"
UI_FILE = "UI_pyqt_tutorial.ui"

#--------------------------------------------------------------------------------------------------
#                                            Imports
#--------------------------------------------------------------------------------------------------
import PyInstaller.__main__
import os
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
import platform
import sys
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
#                                        Main Program
#--------------------------------------------------------------------------------------------------
# Detect the location of the application folder.
os.chdir("..")
appDir = os.path.abspath(os.curdir)

# Remove any old builds of the application.
print("\nRemoving old build files...")
shutil.rmtree(appDir + "\\_Compiler\\" + APP_NAME, ignore_errors=True)
try:
    os.remove(appDir + "\\_Compiler\\" + APP_NAME + ".zip")
except FileNotFoundError:
    pass

# Copy the required ttt3.ico file into the _Compiler folder.
print("\nCopying " + ICON_FILE + " icon file...")
shutil.copy(appDir + "\\" + ICON_FILE, appDir + "\\_Compiler\\")

# Compile the application.
print("\nCompiling " + APP_NAME + ".exe...\n")
PyInstaller.__main__.run([
     "--clean",
     "--onefile",
     "--windowed",
     "--icon=" + ICON_FILE,
     os.path.join(appDir, APP_PYTHON_FILE),
])
print("\n" + APP_NAME + ".exe created.")

# Clean up the build, copy in any 'Settings' and 'Data' folders. Remove unnecessary files and renaming 'dist' to 'APP_NAME'.
print("\nCopying 'data' and 'settings' folders...")
shutil.rmtree(appDir + "\\_Compiler\\build", ignore_errors=True)
os.remove(appDir + "\\_Compiler\\" + APP_NAME + ".spec")
os.remove(appDir + "\\_Compiler\\" + ICON_FILE)
os.rename(appDir + "\\_Compiler\\dist", appDir + "\\_Compiler\\" + APP_NAME)
shutil.copy(appDir + "\\" + UI_FILE, appDir + "\\_Compiler\\" + APP_NAME + "\\")
##shutil.copytree(appDir + "\\data", appDir + "\\_Compiler\\" + APP_NAME + "\\data")


# Create App.zip for distribution.
print("\nCreating " + APP_NAME + ".zip. Please wait...")
with ZipFile("_Compiler\\" + APP_NAME + ".zip", "w", compression=ZIP_DEFLATED, compresslevel=9) as zipObj:
   # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk(os.getcwd() + "\\_Compiler\\" + APP_NAME):
        for filename in filenames:
           # Create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath, filePath.split("_Compiler\\")[1])
print("\n" + APP_NAME + ".zip created.")


bits = sys.version[ : sys.version.index(" bit")][-3:]
version = platform.platform().split("-")[0] + bits + "-bit"
print("\n\n----------- Compile for %s Complete -----------\n\n" % version)
#----------------------------------------------------------------------------------------------------------------------------------------------------#
