import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "selenium", "time"],"include_files": ["chromedriver.exe", 'r.jpg'], "excludes": [] }

base = 'Console'

def main():

	setup(  name = "RickRoll",
    version = "1.0",
    description = "Rick is back",
    options = {"build_exe": build_exe_options},
    executables = [Executable("lltest.py", base=base)])

	setup()

main()