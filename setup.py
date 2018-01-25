import cx_Freeze as cx_f
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Carlos\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Carlos\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'


Images = os.path.join(os.path.dirname(__file__), "Images")

executables = [
    cx_f.Executable("main.py")
    ]

cx_f.setup(
    name="RPG",
    options={
        "build_exe" : {
            "packages" : ["pygame"],
            "include_files" : [
                os.path.join(Images, "SmallForestTile.png"), os.path.join(Images, "dummy.png"),
                os.path.join(Images, "SmallOverworldTile.png")
                ]
            }},
    version="0.0.5",
    executables=executables
    )
        
