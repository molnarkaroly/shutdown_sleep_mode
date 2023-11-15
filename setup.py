import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "customtkinter", "time"],
    "excludes": [],
    "include_files": ["digital-7.ttf"]  # Add the .ttf file here
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="sh_gui",
    version="1.1",
    description="Shutdown",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="SHTOPPER.ico")],
)

