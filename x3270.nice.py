#!/usr/bin/env python3

# Xresource color scheme to x3270pro converter
# by Soldier of FORTRAN
# License: GPL3

import json
import re
import math
import sys
from pathlib import Path

#from http://web.mit.edu/source-8.1/third/x3270/X3270.xad
menus_foreground = [
    "x3270*dialog*confirmButton.foreground",
	"x3270*dialog*foreground",
	"x3270.aboutPopup*icon.foreground",
    "x3270.keypadForeground",
	"x3270*menuBarContainer.foreground",
	"x3270*fileMenuButton*foreground",
	"x3270*optionsMenuButton*foreground",
	"x3270*connectMenuButton*foreground",
	"x3270*reconnectButton*foreground",
	"x3270*macrosMenuButton*foreground",
	"x3270*keypadButton*foreground",
	"x3270*fileMenu*foreground",
	"x3270*exitMenu*foreground",
	"x3270*optionsMenu*foreground",
	"x3270*hostMenu*foreground",
	"x3270*reconnect*foreground",
	"x3270*macrosMenu*foreground",
	"x3270*togglesMenu*foreground",
	"x3270*fontsMenu*foreground",
	"x3270*modelsMenu*foreground",
	"x3270*colorsMenu*foreground",
	"x3270*charsetMenu*foreground",
	"x3270*dialog*value*foreground",
	"x3270*dialog*foreground",
	"x3270*dialog*confirmButton.foreground",
	"x3270*dialog*confirm2Button.foreground",
	"3270*dialog*cancelButton.foreground",
	"x3270.ftProgressPopup*filename.foreground"
	]

critical_foreground = ["x3270.errorPopup*label.foreground","x3270*dialog*cancelButton.foreground"]

menus_background = [
    "x3270.keypadBackground",
	"x3270*menuBarContainer.background",
	"x3270*fileMenuButton*background",
	"x3270*optionsMenuButton*background",
	"x3270*connectMenuButton*background",
	"x3270*reconnectButton*background",
	"x3270*macrosMenuButton*background",
	"x3270*keypadButton*background",
	"x3270*fileMenu*background",
	"x3270*exitMenu*background",
	"x3270*optionsMenu*background",
	"x3270*hostMenu*background",
	"x3270*reconnect*background",
	"x3270*macrosMenu*background",
	"x3270*togglesMenu*background",
	"x3270*fontsMenu*background",
	"x3270*modelsMenu*background",
	"x3270*colorsMenu*background",
	"x3270*charsetMenu*background",
	"x3270*dialog*value*background",
	"x3270*dialog*background",
	"x3270*dialog*confirmButton.background",
	"x3270*dialog*confirm2Button.background",
	"3270*dialog*cancelButton.background",
	"x3270.ftProgressPopup*filename.background",
]
menus_border = [
	"x3270*reconnectButton*borderColor",
	"x3270*macrosMenuButton*borderColor",
	"x3270*fileMenu.borderColor",
	"x3270*exitMenu.borderColor",
	"x3270*optionsMenu.borderColor",
	"x3270*hostMenu.borderColor",
	"x3270*macrosMenu.borderColor",
	"x3270*togglesMenu.borderColor",
	"x3270*fontsMenu.borderColor",
	"x3270*modelsMenu.borderColor",
	"x3270*colorsMenu.borderColor",
	"x3270*charsetMenu.borderColor",
	"x3270*confirmButton.borderColor",
	"x3270*confirmButton.borderColor",
	"x3270*confirm2Button.borderColor",
	"x3270*cancelButton.borderColor",
	"x3270.ftProgressPopup*filename.borderColor"
]

def main():

    if len(sys.argv) < 2:
        print("Usage: {} <.Xresources file from https://ciembor.github.io/4bit/ or terminal.sexy>".format(sys.argv[0]))
        sys.exit(-1)

    # Print header
    border = "! " + ("-" * 50)
    theme_name = Path(sys.argv[1]).with_suffix('').name
    theme_name_clean = theme_name.replace(" ","")
    theme_file = Path(sys.argv[1]).name
    print(border)
    print("! .x3270pro file generated using x3270.nice by Soldier of FORTRAN")
    print("! Original Xresource file: '{}'".format(theme_file))
    print("! Copy and paste this output to ~/.x3270pro")

    # xterm/Xresource colors
    color_names = ["*background", # *.background:
                    "*color0",    # Black
                    "*color1",    # Red
                    "*color2",    # Green
                    "*color3",    # Yellow
                    "*color4",    # Blue
                    "*color5",    # Purple
                    "*color6",    # Turquoise
                    "*color7",    # White
                    "*color8",    # Intense Black
                    "*color9",    # Intense Red
                    "*color10",   # Intense Green
                    "*color11",   # Intense Yellow
                    "*color12",   # Intense Blue
                    "*color13",   # Intense Purple
                    "*color14",   # Intense Turquoise
                    "*color15",   # Intense White
                    "*foreground"]

    # From x3270 manual:
    #  0    X color to use for IBM "neutral/black" (also used as ANSI color 0)
    #  1	X color to use for IBM "blue" (also used for ANSI color 4)
    #  2	X color to use for IBM "red" (also used for ANSI color 1)
    #  3	X color to use for IBM "pink" (also used for ANSI color 5)
    #  4	X color to use for IBM "green" (also used for ANSI color 2)
    #  5	X color to use for IBM "turquoise"
    #  6	X color to use for IBM "yellow" (also used for ANSI color 3)
    #  7	X color to use for IBM "neutral/white"
    #  8	X color to use for IBM "black"
    #  9	X color to use for IBM "deep blue"
    #  10	X color to use for IBM "orange"
    #  11	X color to use for IBM "purple"
    #  12	X color to use for IBM "pale green"
    #  13	X color to use for IBM "pale turquoise" (also used for ANSI color 6)
    #  14	X color to use for IBM "grey"
    #  15	X color to use for IBM "white" (also used for ANSI color 7)
    #  16 X color to use if one of 0..15 cannot be allocated (white or black)
    #  17 X color to use as the default screen background
    #  18 X color to use as the select background
    #  19 IBM color index (0..15) to use for unprotected, unhighlighted fields
    #  20 IBM color index (0..15) to use for unprotected, highlighted fields
    #  21 IBM color index (0..15) to use for protected, unhighlighted fields
    #  22 IBM color index (0..15) to use for protected, highlighted fields
    # For c3270 the default curses color mappings for host colors 0 through 15 are (but they're reversed. defaults to bold then not bold)
    # 0  black   -> color0
    # 1  blue    -> color12
    # 2  red     -> color9
    # 3  magenta -> color13
    # 4  green   -> color10
    # 5  cyan    -> color14
    # 6  yellow  -> color11
    # 7  white   -> foreground
    # 8  black   -> color0
    # 9  blue    -> color4
    # 10 yellow  -> color3
    # 11 blue    -> color5
    # 12 green   -> color2
    # 13 cyan    -> color6
    # 14 black   -> color7
    # 15 white   -> color15
    # 17 bg      -> background
    x3270colors = {
                    "*background": ["17"],
                    "*color0" :  ["0"], # black
                    "*color12" : ["1"], # deepSkyBlue
                    "*color9" :  ["2"], # red
                    "*color13" : ["3"], # pink
                    "*color10" : ["4"], # Green
                    "*color14" : ["5"], # Turquoise
                    "*color11" : ["6"], # Yellow
                    "*foreground" : ["7"], # white
                    #"*color0" :  ["8"], # black
                    "*color4" :  ["9"], # blue
                    "*color3" :  ["10"], # orange
                    "*color5" :  ["11"], # purple
                    "*color2" :  ["12"], # pale green
                    "*color6" :  ["13"], # paleTurquoise2
                    "*color8" : ["14"], # grey
                    "*color7" : ["15"] # white
                    #"*color15" : ["7"] # white
                    #"*color1" : ["2"] # white
                     }


    xcolors = [None] * 18
    mapc = [None] * 23
    mapc[18] = 8
    mapc[19] = 4
    mapc[20] = 2
    mapc[21] = 1
    mapc[22] = 15
    mapc[16] = "white"
    defines = {}

    print(border)
    print("! {:<23} ".format("Original Xresource file:"))
    print(border)

    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            l = line.replace('!','').strip()
            if l.isspace():
                continue
            try:
                name = line.strip().split()[0]
                if "*" in name:
                    #for weird urxvt rules like URxvt*color1
                    name = name[name.find("*"):]

                if "*" not in name and "." in name:
                    #for weird urxvt rules like URxvt.color1
                    name = "*"+name[name.find(".") + 1:]

                if line[0] == '!': # skip empty comments
                    print("!", l)
                name = name.replace('.','').replace(':','')
                if name in color_names:
                    print("!", line.replace('!','').strip())
                    try:
                        color = line.split()[1].replace('[background_opacity]','')
                        if color in defines:
                            color = defines[color]
                        x3270colors[name].append(color)
                    except KeyError:
                        continue
                if line.strip().split()[0].replace('.','').replace(':','').lower() == "#define":
                    print("!", line.strip())
                    defines[line.strip().split()[1]] = line.strip().split()[2]
            except:
                continue


    mapc[18] = x3270colors['*color8'][1]
    if len(x3270colors['*background']) == 1:
        x3270colors['*background'].append("#000000")
    if len(x3270colors['*foreground']) == 1:
        x3270colors['*foreground'].append("#ffffff")

    for i in x3270colors:
        xcolors[int(x3270colors[i][0])] =  x3270colors[i][1]
    xcolors[8] = x3270colors["*color0"][1]


    print(border)
    print("! Adding theme to Options -> Color Scheme")
    print(border)
    print("{}: {}".format("x3270.schemeList", "Default 3279: default\\n\\"))
    print(" "*17,"Bright: bright\\n\\")
    print(" "*17,"Reverse: reverse\\n\\")
    print(" "*17,"Green Screen: greenScreen\\n\\")
    print(" "*17,"{m}: {n}".format(m=theme_name, n=theme_name_clean))

    print(border)
    print("! Generating {} .x3270pro theme".format(theme_name))
    print(border)
    print("! Menu Colors: Foreground")
    print(border)
    for i in menus_foreground:
        print("{:<42}: {}".format(i,x3270colors["*foreground"][1]))

    print(border)
    print("! Menu Colors: Critical")
    print(border)
    for i in critical_foreground:
        print("{:<42}: {}".format(i,x3270colors["*color9"][1]))

    print(border)
    print("! Menu Colors: Backgrounds")
    print(border)
    for i in menus_background:
        print("{:<42}: {}".format(i,x3270colors["*background"][1]))

    print(border)
    print("! Menu Colors: Borders")
    print(border)
    for i in menus_border:
        print("{:<42}: {}".format(i,x3270colors["*foreground"][1]))

    print("{:<42}: {}".format("x3270*fileMenuButton*borderColor", x3270colors["*background"][1]))
    print("{:<42}: {}".format("x3270*optionsMenuButton*borderColor", x3270colors["*background"][1]))
    print("{:<42}: {}".format("x3270*connectMenuButton*borderColor", x3270colors["*background"][1]))

    print("{:<42}: {}".format("x3270*menuBarContainer.borderColor", x3270colors["*background"][1]))

    print("{:<42}: {}".format("x3270*menuBarContainer.borderWidth", 0))
    print("{:<42}: {}".format("x3270*value.borderColor", x3270colors["*foreground"][1]))
    print("{:<42}: {}".format("x3270*value.foreground", x3270colors["*foreground"][1]))

    print(border)
    print("! Default Color Scheme")
    print(border)
    print("x3270.colorScheme: {}".format(theme_name_clean))

    print(border)
    print("! Color Scheme definition")
    print(border)
    print("x3270.colorScheme.{name}:".format(name=theme_name_clean),end = ' ')
    count = 1
    for i in range(23):
        if (count % 4) == 1:
            print("\\\n  ",end = ' ')
        count += 1
        if i == 16:
            print(mapc[i].lower(),end = ' ')
            continue
        try:
            print(xcolors[i],end = ' ')
        except IndexError:
            print(mapc[i],end = ' ')
    print("\n"+border)
    print("! x3270.nice done")
    print(border)

main()