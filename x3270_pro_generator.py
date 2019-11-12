#!/usr/bin/env python3

import json
import re
import math
import sys
# From http://jonasjacek.github.io/colors/
map = '[{"colorId":0,"hexString":"#000000","rgb":{"r":0,"g":0,"b":0},"hsl":{"h":0,"s":0,"l":0},"name":"Black"},{"colorId":1,"hexString":"#800000","rgb":{"r":128,"g":0,"b":0},"hsl":{"h":0,"s":100,"l":25},"name":"Maroon"},{"colorId":2,"hexString":"#008000","rgb":{"r":0,"g":128,"b":0},"hsl":{"h":120,"s":100,"l":25},"name":"Green"},{"colorId":3,"hexString":"#808000","rgb":{"r":128,"g":128,"b":0},"hsl":{"h":60,"s":100,"l":25},"name":"Olive"},{"colorId":4,"hexString":"#000080","rgb":{"r":0,"g":0,"b":128},"hsl":{"h":240,"s":100,"l":25},"name":"Navy"},{"colorId":5,"hexString":"#800080","rgb":{"r":128,"g":0,"b":128},"hsl":{"h":300,"s":100,"l":25},"name":"Purple"},{"colorId":6,"hexString":"#008080","rgb":{"r":0,"g":128,"b":128},"hsl":{"h":180,"s":100,"l":25},"name":"Teal"},{"colorId":7,"hexString":"#c0c0c0","rgb":{"r":192,"g":192,"b":192},"hsl":{"h":0,"s":0,"l":75},"name":"Silver"},{"colorId":8,"hexString":"#808080","rgb":{"r":128,"g":128,"b":128},"hsl":{"h":0,"s":0,"l":50},"name":"Grey"},{"colorId":9,"hexString":"#ff0000","rgb":{"r":255,"g":0,"b":0},"hsl":{"h":0,"s":100,"l":50},"name":"Red"},{"colorId":10,"hexString":"#00ff00","rgb":{"r":0,"g":255,"b":0},"hsl":{"h":120,"s":100,"l":50},"name":"Lime"},{"colorId":11,"hexString":"#ffff00","rgb":{"r":255,"g":255,"b":0},"hsl":{"h":60,"s":100,"l":50},"name":"Yellow"},{"colorId":12,"hexString":"#0000ff","rgb":{"r":0,"g":0,"b":255},"hsl":{"h":240,"s":100,"l":50},"name":"Blue"},{"colorId":13,"hexString":"#ff00ff","rgb":{"r":255,"g":0,"b":255},"hsl":{"h":300,"s":100,"l":50},"name":"Fuchsia"},{"colorId":14,"hexString":"#00ffff","rgb":{"r":0,"g":255,"b":255},"hsl":{"h":180,"s":100,"l":50},"name":"Aqua"},{"colorId":15,"hexString":"#ffffff","rgb":{"r":255,"g":255,"b":255},"hsl":{"h":0,"s":0,"l":100},"name":"White"},{"colorId":16,"hexString":"#000000","rgb":{"r":0,"g":0,"b":0},"hsl":{"h":0,"s":0,"l":0},"name":"Grey0"},{"colorId":17,"hexString":"#00005f","rgb":{"r":0,"g":0,"b":95},"hsl":{"h":240,"s":100,"l":18},"name":"NavyBlue"},{"colorId":18,"hexString":"#000087","rgb":{"r":0,"g":0,"b":135},"hsl":{"h":240,"s":100,"l":26},"name":"DarkBlue"},{"colorId":19,"hexString":"#0000af","rgb":{"r":0,"g":0,"b":175},"hsl":{"h":240,"s":100,"l":34},"name":"Blue3"},{"colorId":20,"hexString":"#0000d7","rgb":{"r":0,"g":0,"b":215},"hsl":{"h":240,"s":100,"l":42},"name":"Blue3"},{"colorId":21,"hexString":"#0000ff","rgb":{"r":0,"g":0,"b":255},"hsl":{"h":240,"s":100,"l":50},"name":"Blue1"},{"colorId":22,"hexString":"#005f00","rgb":{"r":0,"g":95,"b":0},"hsl":{"h":120,"s":100,"l":18},"name":"DarkGreen"},{"colorId":23,"hexString":"#005f5f","rgb":{"r":0,"g":95,"b":95},"hsl":{"h":180,"s":100,"l":18},"name":"DeepSkyBlue4"},{"colorId":24,"hexString":"#005f87","rgb":{"r":0,"g":95,"b":135},"hsl":{"h":197.777777777778,"s":100,"l":26},"name":"DeepSkyBlue4"},{"colorId":25,"hexString":"#005faf","rgb":{"r":0,"g":95,"b":175},"hsl":{"h":207.428571428571,"s":100,"l":34},"name":"DeepSkyBlue4"},{"colorId":26,"hexString":"#005fd7","rgb":{"r":0,"g":95,"b":215},"hsl":{"h":213.488372093023,"s":100,"l":42},"name":"DodgerBlue3"},{"colorId":27,"hexString":"#005fff","rgb":{"r":0,"g":95,"b":255},"hsl":{"h":217.647058823529,"s":100,"l":50},"name":"DodgerBlue2"},{"colorId":28,"hexString":"#008700","rgb":{"r":0,"g":135,"b":0},"hsl":{"h":120,"s":100,"l":26},"name":"Green4"},{"colorId":29,"hexString":"#00875f","rgb":{"r":0,"g":135,"b":95},"hsl":{"h":162.222222222222,"s":100,"l":26},"name":"SpringGreen4"},{"colorId":30,"hexString":"#008787","rgb":{"r":0,"g":135,"b":135},"hsl":{"h":180,"s":100,"l":26},"name":"Turquoise4"},{"colorId":31,"hexString":"#0087af","rgb":{"r":0,"g":135,"b":175},"hsl":{"h":193.714285714286,"s":100,"l":34},"name":"DeepSkyBlue3"},{"colorId":32,"hexString":"#0087d7","rgb":{"r":0,"g":135,"b":215},"hsl":{"h":202.325581395349,"s":100,"l":42},"name":"DeepSkyBlue3"},{"colorId":33,"hexString":"#0087ff","rgb":{"r":0,"g":135,"b":255},"hsl":{"h":208.235294117647,"s":100,"l":50},"name":"DodgerBlue1"},{"colorId":34,"hexString":"#00af00","rgb":{"r":0,"g":175,"b":0},"hsl":{"h":120,"s":100,"l":34},"name":"Green3"},{"colorId":35,"hexString":"#00af5f","rgb":{"r":0,"g":175,"b":95},"hsl":{"h":152.571428571429,"s":100,"l":34},"name":"SpringGreen3"},{"colorId":36,"hexString":"#00af87","rgb":{"r":0,"g":175,"b":135},"hsl":{"h":166.285714285714,"s":100,"l":34},"name":"DarkCyan"},{"colorId":37,"hexString":"#00afaf","rgb":{"r":0,"g":175,"b":175},"hsl":{"h":180,"s":100,"l":34},"name":"LightSeaGreen"},{"colorId":38,"hexString":"#00afd7","rgb":{"r":0,"g":175,"b":215},"hsl":{"h":191.162790697674,"s":100,"l":42},"name":"DeepSkyBlue2"},{"colorId":39,"hexString":"#00afff","rgb":{"r":0,"g":175,"b":255},"hsl":{"h":198.823529411765,"s":100,"l":50},"name":"DeepSkyBlue1"},{"colorId":40,"hexString":"#00d700","rgb":{"r":0,"g":215,"b":0},"hsl":{"h":120,"s":100,"l":42},"name":"Green3"},{"colorId":41,"hexString":"#00d75f","rgb":{"r":0,"g":215,"b":95},"hsl":{"h":146.511627906977,"s":100,"l":42},"name":"SpringGreen3"},{"colorId":42,"hexString":"#00d787","rgb":{"r":0,"g":215,"b":135},"hsl":{"h":157.674418604651,"s":100,"l":42},"name":"SpringGreen2"},{"colorId":43,"hexString":"#00d7af","rgb":{"r":0,"g":215,"b":175},"hsl":{"h":168.837209302326,"s":100,"l":42},"name":"Cyan3"},{"colorId":44,"hexString":"#00d7d7","rgb":{"r":0,"g":215,"b":215},"hsl":{"h":180,"s":100,"l":42},"name":"DarkTurquoise"},{"colorId":45,"hexString":"#00d7ff","rgb":{"r":0,"g":215,"b":255},"hsl":{"h":189.411764705882,"s":100,"l":50},"name":"Turquoise2"},{"colorId":46,"hexString":"#00ff00","rgb":{"r":0,"g":255,"b":0},"hsl":{"h":120,"s":100,"l":50},"name":"Green1"},{"colorId":47,"hexString":"#00ff5f","rgb":{"r":0,"g":255,"b":95},"hsl":{"h":142.352941176471,"s":100,"l":50},"name":"SpringGreen2"},{"colorId":48,"hexString":"#00ff87","rgb":{"r":0,"g":255,"b":135},"hsl":{"h":151.764705882353,"s":100,"l":50},"name":"SpringGreen1"},{"colorId":49,"hexString":"#00ffaf","rgb":{"r":0,"g":255,"b":175},"hsl":{"h":161.176470588235,"s":100,"l":50},"name":"MediumSpringGreen"},{"colorId":50,"hexString":"#00ffd7","rgb":{"r":0,"g":255,"b":215},"hsl":{"h":170.588235294118,"s":100,"l":50},"name":"Cyan2"},{"colorId":51,"hexString":"#00ffff","rgb":{"r":0,"g":255,"b":255},"hsl":{"h":180,"s":100,"l":50},"name":"Cyan1"},{"colorId":52,"hexString":"#5f0000","rgb":{"r":95,"g":0,"b":0},"hsl":{"h":0,"s":100,"l":18},"name":"DarkRed"},{"colorId":53,"hexString":"#5f005f","rgb":{"r":95,"g":0,"b":95},"hsl":{"h":300,"s":100,"l":18},"name":"DeepPink4"},{"colorId":54,"hexString":"#5f0087","rgb":{"r":95,"g":0,"b":135},"hsl":{"h":282.222222222222,"s":100,"l":26},"name":"Purple4"},{"colorId":55,"hexString":"#5f00af","rgb":{"r":95,"g":0,"b":175},"hsl":{"h":272.571428571429,"s":100,"l":34},"name":"Purple4"},{"colorId":56,"hexString":"#5f00d7","rgb":{"r":95,"g":0,"b":215},"hsl":{"h":266.511627906977,"s":100,"l":42},"name":"Purple3"},{"colorId":57,"hexString":"#5f00ff","rgb":{"r":95,"g":0,"b":255},"hsl":{"h":262.352941176471,"s":100,"l":50},"name":"BlueViolet"},{"colorId":58,"hexString":"#5f5f00","rgb":{"r":95,"g":95,"b":0},"hsl":{"h":60,"s":100,"l":18},"name":"Orange4"},{"colorId":59,"hexString":"#5f5f5f","rgb":{"r":95,"g":95,"b":95},"hsl":{"h":0,"s":0,"l":37},"name":"Grey37"},{"colorId":60,"hexString":"#5f5f87","rgb":{"r":95,"g":95,"b":135},"hsl":{"h":240,"s":17,"l":45},"name":"MediumPurple4"},{"colorId":61,"hexString":"#5f5faf","rgb":{"r":95,"g":95,"b":175},"hsl":{"h":240,"s":33,"l":52},"name":"SlateBlue3"},{"colorId":62,"hexString":"#5f5fd7","rgb":{"r":95,"g":95,"b":215},"hsl":{"h":240,"s":60,"l":60},"name":"SlateBlue3"},{"colorId":63,"hexString":"#5f5fff","rgb":{"r":95,"g":95,"b":255},"hsl":{"h":240,"s":100,"l":68},"name":"RoyalBlue1"},{"colorId":64,"hexString":"#5f8700","rgb":{"r":95,"g":135,"b":0},"hsl":{"h":77.7777777777778,"s":100,"l":26},"name":"Chartreuse4"},{"colorId":65,"hexString":"#5f875f","rgb":{"r":95,"g":135,"b":95},"hsl":{"h":120,"s":17,"l":45},"name":"DarkSeaGreen4"},{"colorId":66,"hexString":"#5f8787","rgb":{"r":95,"g":135,"b":135},"hsl":{"h":180,"s":17,"l":45},"name":"PaleTurquoise4"},{"colorId":67,"hexString":"#5f87af","rgb":{"r":95,"g":135,"b":175},"hsl":{"h":210,"s":33,"l":52},"name":"SteelBlue"},{"colorId":68,"hexString":"#5f87d7","rgb":{"r":95,"g":135,"b":215},"hsl":{"h":220,"s":60,"l":60},"name":"SteelBlue3"},{"colorId":69,"hexString":"#5f87ff","rgb":{"r":95,"g":135,"b":255},"hsl":{"h":225,"s":100,"l":68},"name":"CornflowerBlue"},{"colorId":70,"hexString":"#5faf00","rgb":{"r":95,"g":175,"b":0},"hsl":{"h":87.4285714285714,"s":100,"l":34},"name":"Chartreuse3"},{"colorId":71,"hexString":"#5faf5f","rgb":{"r":95,"g":175,"b":95},"hsl":{"h":120,"s":33,"l":52},"name":"DarkSeaGreen4"},{"colorId":72,"hexString":"#5faf87","rgb":{"r":95,"g":175,"b":135},"hsl":{"h":150,"s":33,"l":52},"name":"CadetBlue"},{"colorId":73,"hexString":"#5fafaf","rgb":{"r":95,"g":175,"b":175},"hsl":{"h":180,"s":33,"l":52},"name":"CadetBlue"},{"colorId":74,"hexString":"#5fafd7","rgb":{"r":95,"g":175,"b":215},"hsl":{"h":200,"s":60,"l":60},"name":"SkyBlue3"},{"colorId":75,"hexString":"#5fafff","rgb":{"r":95,"g":175,"b":255},"hsl":{"h":210,"s":100,"l":68},"name":"SteelBlue1"},{"colorId":76,"hexString":"#5fd700","rgb":{"r":95,"g":215,"b":0},"hsl":{"h":93.4883720930233,"s":100,"l":42},"name":"Chartreuse3"},{"colorId":77,"hexString":"#5fd75f","rgb":{"r":95,"g":215,"b":95},"hsl":{"h":120,"s":60,"l":60},"name":"PaleGreen3"},{"colorId":78,"hexString":"#5fd787","rgb":{"r":95,"g":215,"b":135},"hsl":{"h":140,"s":60,"l":60},"name":"SeaGreen3"},{"colorId":79,"hexString":"#5fd7af","rgb":{"r":95,"g":215,"b":175},"hsl":{"h":160,"s":60,"l":60},"name":"Aquamarine3"},{"colorId":80,"hexString":"#5fd7d7","rgb":{"r":95,"g":215,"b":215},"hsl":{"h":180,"s":60,"l":60},"name":"MediumTurquoise"},{"colorId":81,"hexString":"#5fd7ff","rgb":{"r":95,"g":215,"b":255},"hsl":{"h":195,"s":100,"l":68},"name":"SteelBlue1"},{"colorId":82,"hexString":"#5fff00","rgb":{"r":95,"g":255,"b":0},"hsl":{"h":97.6470588235294,"s":100,"l":50},"name":"Chartreuse2"},{"colorId":83,"hexString":"#5fff5f","rgb":{"r":95,"g":255,"b":95},"hsl":{"h":120,"s":100,"l":68},"name":"SeaGreen2"},{"colorId":84,"hexString":"#5fff87","rgb":{"r":95,"g":255,"b":135},"hsl":{"h":135,"s":100,"l":68},"name":"SeaGreen1"},{"colorId":85,"hexString":"#5fffaf","rgb":{"r":95,"g":255,"b":175},"hsl":{"h":150,"s":100,"l":68},"name":"SeaGreen1"},{"colorId":86,"hexString":"#5fffd7","rgb":{"r":95,"g":255,"b":215},"hsl":{"h":165,"s":100,"l":68},"name":"Aquamarine1"},{"colorId":87,"hexString":"#5fffff","rgb":{"r":95,"g":255,"b":255},"hsl":{"h":180,"s":100,"l":68},"name":"DarkSlateGray2"},{"colorId":88,"hexString":"#870000","rgb":{"r":135,"g":0,"b":0},"hsl":{"h":0,"s":100,"l":26},"name":"DarkRed"},{"colorId":89,"hexString":"#87005f","rgb":{"r":135,"g":0,"b":95},"hsl":{"h":317.777777777778,"s":100,"l":26},"name":"DeepPink4"},{"colorId":90,"hexString":"#870087","rgb":{"r":135,"g":0,"b":135},"hsl":{"h":300,"s":100,"l":26},"name":"DarkMagenta"},{"colorId":91,"hexString":"#8700af","rgb":{"r":135,"g":0,"b":175},"hsl":{"h":286.285714285714,"s":100,"l":34},"name":"DarkMagenta"},{"colorId":92,"hexString":"#8700d7","rgb":{"r":135,"g":0,"b":215},"hsl":{"h":277.674418604651,"s":100,"l":42},"name":"DarkViolet"},{"colorId":93,"hexString":"#8700ff","rgb":{"r":135,"g":0,"b":255},"hsl":{"h":271.764705882353,"s":100,"l":50},"name":"Purple"},{"colorId":94,"hexString":"#875f00","rgb":{"r":135,"g":95,"b":0},"hsl":{"h":42.2222222222222,"s":100,"l":26},"name":"Orange4"},{"colorId":95,"hexString":"#875f5f","rgb":{"r":135,"g":95,"b":95},"hsl":{"h":0,"s":17,"l":45},"name":"LightPink4"},{"colorId":96,"hexString":"#875f87","rgb":{"r":135,"g":95,"b":135},"hsl":{"h":300,"s":17,"l":45},"name":"Plum4"},{"colorId":97,"hexString":"#875faf","rgb":{"r":135,"g":95,"b":175},"hsl":{"h":270,"s":33,"l":52},"name":"MediumPurple3"},{"colorId":98,"hexString":"#875fd7","rgb":{"r":135,"g":95,"b":215},"hsl":{"h":260,"s":60,"l":60},"name":"MediumPurple3"},{"colorId":99,"hexString":"#875fff","rgb":{"r":135,"g":95,"b":255},"hsl":{"h":255,"s":100,"l":68},"name":"SlateBlue1"},{"colorId":100,"hexString":"#878700","rgb":{"r":135,"g":135,"b":0},"hsl":{"h":60,"s":100,"l":26},"name":"Yellow4"},{"colorId":101,"hexString":"#87875f","rgb":{"r":135,"g":135,"b":95},"hsl":{"h":60,"s":17,"l":45},"name":"Wheat4"},{"colorId":102,"hexString":"#878787","rgb":{"r":135,"g":135,"b":135},"hsl":{"h":0,"s":0,"l":52},"name":"Grey53"},{"colorId":103,"hexString":"#8787af","rgb":{"r":135,"g":135,"b":175},"hsl":{"h":240,"s":20,"l":60},"name":"LightSlateGrey"},{"colorId":104,"hexString":"#8787d7","rgb":{"r":135,"g":135,"b":215},"hsl":{"h":240,"s":50,"l":68},"name":"MediumPurple"},{"colorId":105,"hexString":"#8787ff","rgb":{"r":135,"g":135,"b":255},"hsl":{"h":240,"s":100,"l":76},"name":"LightSlateBlue"},{"colorId":106,"hexString":"#87af00","rgb":{"r":135,"g":175,"b":0},"hsl":{"h":73.7142857142857,"s":100,"l":34},"name":"Yellow4"},{"colorId":107,"hexString":"#87af5f","rgb":{"r":135,"g":175,"b":95},"hsl":{"h":90,"s":33,"l":52},"name":"DarkOliveGreen3"},{"colorId":108,"hexString":"#87af87","rgb":{"r":135,"g":175,"b":135},"hsl":{"h":120,"s":20,"l":60},"name":"DarkSeaGreen"},{"colorId":109,"hexString":"#87afaf","rgb":{"r":135,"g":175,"b":175},"hsl":{"h":180,"s":20,"l":60},"name":"LightSkyBlue3"},{"colorId":110,"hexString":"#87afd7","rgb":{"r":135,"g":175,"b":215},"hsl":{"h":210,"s":50,"l":68},"name":"LightSkyBlue3"},{"colorId":111,"hexString":"#87afff","rgb":{"r":135,"g":175,"b":255},"hsl":{"h":220,"s":100,"l":76},"name":"SkyBlue2"},{"colorId":112,"hexString":"#87d700","rgb":{"r":135,"g":215,"b":0},"hsl":{"h":82.3255813953488,"s":100,"l":42},"name":"Chartreuse2"},{"colorId":113,"hexString":"#87d75f","rgb":{"r":135,"g":215,"b":95},"hsl":{"h":100,"s":60,"l":60},"name":"DarkOliveGreen3"},{"colorId":114,"hexString":"#87d787","rgb":{"r":135,"g":215,"b":135},"hsl":{"h":120,"s":50,"l":68},"name":"PaleGreen3"},{"colorId":115,"hexString":"#87d7af","rgb":{"r":135,"g":215,"b":175},"hsl":{"h":150,"s":50,"l":68},"name":"DarkSeaGreen3"},{"colorId":116,"hexString":"#87d7d7","rgb":{"r":135,"g":215,"b":215},"hsl":{"h":180,"s":50,"l":68},"name":"DarkSlateGray3"},{"colorId":117,"hexString":"#87d7ff","rgb":{"r":135,"g":215,"b":255},"hsl":{"h":200,"s":100,"l":76},"name":"SkyBlue1"},{"colorId":118,"hexString":"#87ff00","rgb":{"r":135,"g":255,"b":0},"hsl":{"h":88.2352941176471,"s":100,"l":50},"name":"Chartreuse1"},{"colorId":119,"hexString":"#87ff5f","rgb":{"r":135,"g":255,"b":95},"hsl":{"h":105,"s":100,"l":68},"name":"LightGreen"},{"colorId":120,"hexString":"#87ff87","rgb":{"r":135,"g":255,"b":135},"hsl":{"h":120,"s":100,"l":76},"name":"LightGreen"},{"colorId":121,"hexString":"#87ffaf","rgb":{"r":135,"g":255,"b":175},"hsl":{"h":140,"s":100,"l":76},"name":"PaleGreen1"},{"colorId":122,"hexString":"#87ffd7","rgb":{"r":135,"g":255,"b":215},"hsl":{"h":160,"s":100,"l":76},"name":"Aquamarine1"},{"colorId":123,"hexString":"#87ffff","rgb":{"r":135,"g":255,"b":255},"hsl":{"h":180,"s":100,"l":76},"name":"DarkSlateGray1"},{"colorId":124,"hexString":"#af0000","rgb":{"r":175,"g":0,"b":0},"hsl":{"h":0,"s":100,"l":34},"name":"Red3"},{"colorId":125,"hexString":"#af005f","rgb":{"r":175,"g":0,"b":95},"hsl":{"h":327.428571428571,"s":100,"l":34},"name":"DeepPink4"},{"colorId":126,"hexString":"#af0087","rgb":{"r":175,"g":0,"b":135},"hsl":{"h":313.714285714286,"s":100,"l":34},"name":"MediumVioletRed"},{"colorId":127,"hexString":"#af00af","rgb":{"r":175,"g":0,"b":175},"hsl":{"h":300,"s":100,"l":34},"name":"Magenta3"},{"colorId":128,"hexString":"#af00d7","rgb":{"r":175,"g":0,"b":215},"hsl":{"h":288.837209302326,"s":100,"l":42},"name":"DarkViolet"},{"colorId":129,"hexString":"#af00ff","rgb":{"r":175,"g":0,"b":255},"hsl":{"h":281.176470588235,"s":100,"l":50},"name":"Purple"},{"colorId":130,"hexString":"#af5f00","rgb":{"r":175,"g":95,"b":0},"hsl":{"h":32.5714285714286,"s":100,"l":34},"name":"DarkOrange3"},{"colorId":131,"hexString":"#af5f5f","rgb":{"r":175,"g":95,"b":95},"hsl":{"h":0,"s":33,"l":52},"name":"IndianRed"},{"colorId":132,"hexString":"#af5f87","rgb":{"r":175,"g":95,"b":135},"hsl":{"h":330,"s":33,"l":52},"name":"HotPink3"},{"colorId":133,"hexString":"#af5faf","rgb":{"r":175,"g":95,"b":175},"hsl":{"h":300,"s":33,"l":52},"name":"MediumOrchid3"},{"colorId":134,"hexString":"#af5fd7","rgb":{"r":175,"g":95,"b":215},"hsl":{"h":280,"s":60,"l":60},"name":"MediumOrchid"},{"colorId":135,"hexString":"#af5fff","rgb":{"r":175,"g":95,"b":255},"hsl":{"h":270,"s":100,"l":68},"name":"MediumPurple2"},{"colorId":136,"hexString":"#af8700","rgb":{"r":175,"g":135,"b":0},"hsl":{"h":46.2857142857143,"s":100,"l":34},"name":"DarkGoldenrod"},{"colorId":137,"hexString":"#af875f","rgb":{"r":175,"g":135,"b":95},"hsl":{"h":30,"s":33,"l":52},"name":"LightSalmon3"},{"colorId":138,"hexString":"#af8787","rgb":{"r":175,"g":135,"b":135},"hsl":{"h":0,"s":20,"l":60},"name":"RosyBrown"},{"colorId":139,"hexString":"#af87af","rgb":{"r":175,"g":135,"b":175},"hsl":{"h":300,"s":20,"l":60},"name":"Grey63"},{"colorId":140,"hexString":"#af87d7","rgb":{"r":175,"g":135,"b":215},"hsl":{"h":270,"s":50,"l":68},"name":"MediumPurple2"},{"colorId":141,"hexString":"#af87ff","rgb":{"r":175,"g":135,"b":255},"hsl":{"h":260,"s":100,"l":76},"name":"MediumPurple1"},{"colorId":142,"hexString":"#afaf00","rgb":{"r":175,"g":175,"b":0},"hsl":{"h":60,"s":100,"l":34},"name":"Gold3"},{"colorId":143,"hexString":"#afaf5f","rgb":{"r":175,"g":175,"b":95},"hsl":{"h":60,"s":33,"l":52},"name":"DarkKhaki"},{"colorId":144,"hexString":"#afaf87","rgb":{"r":175,"g":175,"b":135},"hsl":{"h":60,"s":20,"l":60},"name":"NavajoWhite3"},{"colorId":145,"hexString":"#afafaf","rgb":{"r":175,"g":175,"b":175},"hsl":{"h":0,"s":0,"l":68},"name":"Grey69"},{"colorId":146,"hexString":"#afafd7","rgb":{"r":175,"g":175,"b":215},"hsl":{"h":240,"s":33,"l":76},"name":"LightSteelBlue3"},{"colorId":147,"hexString":"#afafff","rgb":{"r":175,"g":175,"b":255},"hsl":{"h":240,"s":100,"l":84},"name":"LightSteelBlue"},{"colorId":148,"hexString":"#afd700","rgb":{"r":175,"g":215,"b":0},"hsl":{"h":71.1627906976744,"s":100,"l":42},"name":"Yellow3"},{"colorId":149,"hexString":"#afd75f","rgb":{"r":175,"g":215,"b":95},"hsl":{"h":80,"s":60,"l":60},"name":"DarkOliveGreen3"},{"colorId":150,"hexString":"#afd787","rgb":{"r":175,"g":215,"b":135},"hsl":{"h":90,"s":50,"l":68},"name":"DarkSeaGreen3"},{"colorId":151,"hexString":"#afd7af","rgb":{"r":175,"g":215,"b":175},"hsl":{"h":120,"s":33,"l":76},"name":"DarkSeaGreen2"},{"colorId":152,"hexString":"#afd7d7","rgb":{"r":175,"g":215,"b":215},"hsl":{"h":180,"s":33,"l":76},"name":"LightCyan3"},{"colorId":153,"hexString":"#afd7ff","rgb":{"r":175,"g":215,"b":255},"hsl":{"h":210,"s":100,"l":84},"name":"LightSkyBlue1"},{"colorId":154,"hexString":"#afff00","rgb":{"r":175,"g":255,"b":0},"hsl":{"h":78.8235294117647,"s":100,"l":50},"name":"GreenYellow"},{"colorId":155,"hexString":"#afff5f","rgb":{"r":175,"g":255,"b":95},"hsl":{"h":90,"s":100,"l":68},"name":"DarkOliveGreen2"},{"colorId":156,"hexString":"#afff87","rgb":{"r":175,"g":255,"b":135},"hsl":{"h":100,"s":100,"l":76},"name":"PaleGreen1"},{"colorId":157,"hexString":"#afffaf","rgb":{"r":175,"g":255,"b":175},"hsl":{"h":120,"s":100,"l":84},"name":"DarkSeaGreen2"},{"colorId":158,"hexString":"#afffd7","rgb":{"r":175,"g":255,"b":215},"hsl":{"h":150,"s":100,"l":84},"name":"DarkSeaGreen1"},{"colorId":159,"hexString":"#afffff","rgb":{"r":175,"g":255,"b":255},"hsl":{"h":180,"s":100,"l":84},"name":"PaleTurquoise1"},{"colorId":160,"hexString":"#d70000","rgb":{"r":215,"g":0,"b":0},"hsl":{"h":0,"s":100,"l":42},"name":"Red3"},{"colorId":161,"hexString":"#d7005f","rgb":{"r":215,"g":0,"b":95},"hsl":{"h":333.488372093023,"s":100,"l":42},"name":"DeepPink3"},{"colorId":162,"hexString":"#d70087","rgb":{"r":215,"g":0,"b":135},"hsl":{"h":322.325581395349,"s":100,"l":42},"name":"DeepPink3"},{"colorId":163,"hexString":"#d700af","rgb":{"r":215,"g":0,"b":175},"hsl":{"h":311.162790697674,"s":100,"l":42},"name":"Magenta3"},{"colorId":164,"hexString":"#d700d7","rgb":{"r":215,"g":0,"b":215},"hsl":{"h":300,"s":100,"l":42},"name":"Magenta3"},{"colorId":165,"hexString":"#d700ff","rgb":{"r":215,"g":0,"b":255},"hsl":{"h":290.588235294118,"s":100,"l":50},"name":"Magenta2"},{"colorId":166,"hexString":"#d75f00","rgb":{"r":215,"g":95,"b":0},"hsl":{"h":26.5116279069767,"s":100,"l":42},"name":"DarkOrange3"},{"colorId":167,"hexString":"#d75f5f","rgb":{"r":215,"g":95,"b":95},"hsl":{"h":0,"s":60,"l":60},"name":"IndianRed"},{"colorId":168,"hexString":"#d75f87","rgb":{"r":215,"g":95,"b":135},"hsl":{"h":340,"s":60,"l":60},"name":"HotPink3"},{"colorId":169,"hexString":"#d75faf","rgb":{"r":215,"g":95,"b":175},"hsl":{"h":320,"s":60,"l":60},"name":"HotPink2"},{"colorId":170,"hexString":"#d75fd7","rgb":{"r":215,"g":95,"b":215},"hsl":{"h":300,"s":60,"l":60},"name":"Orchid"},{"colorId":171,"hexString":"#d75fff","rgb":{"r":215,"g":95,"b":255},"hsl":{"h":285,"s":100,"l":68},"name":"MediumOrchid1"},{"colorId":172,"hexString":"#d78700","rgb":{"r":215,"g":135,"b":0},"hsl":{"h":37.6744186046512,"s":100,"l":42},"name":"Orange3"},{"colorId":173,"hexString":"#d7875f","rgb":{"r":215,"g":135,"b":95},"hsl":{"h":20,"s":60,"l":60},"name":"LightSalmon3"},{"colorId":174,"hexString":"#d78787","rgb":{"r":215,"g":135,"b":135},"hsl":{"h":0,"s":50,"l":68},"name":"LightPink3"},{"colorId":175,"hexString":"#d787af","rgb":{"r":215,"g":135,"b":175},"hsl":{"h":330,"s":50,"l":68},"name":"Pink3"},{"colorId":176,"hexString":"#d787d7","rgb":{"r":215,"g":135,"b":215},"hsl":{"h":300,"s":50,"l":68},"name":"Plum3"},{"colorId":177,"hexString":"#d787ff","rgb":{"r":215,"g":135,"b":255},"hsl":{"h":280,"s":100,"l":76},"name":"Violet"},{"colorId":178,"hexString":"#d7af00","rgb":{"r":215,"g":175,"b":0},"hsl":{"h":48.8372093023256,"s":100,"l":42},"name":"Gold3"},{"colorId":179,"hexString":"#d7af5f","rgb":{"r":215,"g":175,"b":95},"hsl":{"h":40,"s":60,"l":60},"name":"LightGoldenrod3"},{"colorId":180,"hexString":"#d7af87","rgb":{"r":215,"g":175,"b":135},"hsl":{"h":30,"s":50,"l":68},"name":"Tan"},{"colorId":181,"hexString":"#d7afaf","rgb":{"r":215,"g":175,"b":175},"hsl":{"h":0,"s":33,"l":76},"name":"MistyRose3"},{"colorId":182,"hexString":"#d7afd7","rgb":{"r":215,"g":175,"b":215},"hsl":{"h":300,"s":33,"l":76},"name":"Thistle3"},{"colorId":183,"hexString":"#d7afff","rgb":{"r":215,"g":175,"b":255},"hsl":{"h":270,"s":100,"l":84},"name":"Plum2"},{"colorId":184,"hexString":"#d7d700","rgb":{"r":215,"g":215,"b":0},"hsl":{"h":60,"s":100,"l":42},"name":"Yellow3"},{"colorId":185,"hexString":"#d7d75f","rgb":{"r":215,"g":215,"b":95},"hsl":{"h":60,"s":60,"l":60},"name":"Khaki3"},{"colorId":186,"hexString":"#d7d787","rgb":{"r":215,"g":215,"b":135},"hsl":{"h":60,"s":50,"l":68},"name":"LightGoldenrod2"},{"colorId":187,"hexString":"#d7d7af","rgb":{"r":215,"g":215,"b":175},"hsl":{"h":60,"s":33,"l":76},"name":"LightYellow3"},{"colorId":188,"hexString":"#d7d7d7","rgb":{"r":215,"g":215,"b":215},"hsl":{"h":0,"s":0,"l":84},"name":"Grey84"},{"colorId":189,"hexString":"#d7d7ff","rgb":{"r":215,"g":215,"b":255},"hsl":{"h":240,"s":100,"l":92},"name":"LightSteelBlue1"},{"colorId":190,"hexString":"#d7ff00","rgb":{"r":215,"g":255,"b":0},"hsl":{"h":69.4117647058823,"s":100,"l":50},"name":"Yellow2"},{"colorId":191,"hexString":"#d7ff5f","rgb":{"r":215,"g":255,"b":95},"hsl":{"h":75,"s":100,"l":68},"name":"DarkOliveGreen1"},{"colorId":192,"hexString":"#d7ff87","rgb":{"r":215,"g":255,"b":135},"hsl":{"h":80,"s":100,"l":76},"name":"DarkOliveGreen1"},{"colorId":193,"hexString":"#d7ffaf","rgb":{"r":215,"g":255,"b":175},"hsl":{"h":90,"s":100,"l":84},"name":"DarkSeaGreen1"},{"colorId":194,"hexString":"#d7ffd7","rgb":{"r":215,"g":255,"b":215},"hsl":{"h":120,"s":100,"l":92},"name":"Honeydew2"},{"colorId":195,"hexString":"#d7ffff","rgb":{"r":215,"g":255,"b":255},"hsl":{"h":180,"s":100,"l":92},"name":"LightCyan1"},{"colorId":196,"hexString":"#ff0000","rgb":{"r":255,"g":0,"b":0},"hsl":{"h":0,"s":100,"l":50},"name":"Red1"},{"colorId":197,"hexString":"#ff005f","rgb":{"r":255,"g":0,"b":95},"hsl":{"h":337.647058823529,"s":100,"l":50},"name":"DeepPink2"},{"colorId":198,"hexString":"#ff0087","rgb":{"r":255,"g":0,"b":135},"hsl":{"h":328.235294117647,"s":100,"l":50},"name":"DeepPink1"},{"colorId":199,"hexString":"#ff00af","rgb":{"r":255,"g":0,"b":175},"hsl":{"h":318.823529411765,"s":100,"l":50},"name":"DeepPink1"},{"colorId":200,"hexString":"#ff00d7","rgb":{"r":255,"g":0,"b":215},"hsl":{"h":309.411764705882,"s":100,"l":50},"name":"Magenta2"},{"colorId":201,"hexString":"#ff00ff","rgb":{"r":255,"g":0,"b":255},"hsl":{"h":300,"s":100,"l":50},"name":"Magenta1"},{"colorId":202,"hexString":"#ff5f00","rgb":{"r":255,"g":95,"b":0},"hsl":{"h":22.3529411764706,"s":100,"l":50},"name":"OrangeRed1"},{"colorId":203,"hexString":"#ff5f5f","rgb":{"r":255,"g":95,"b":95},"hsl":{"h":0,"s":100,"l":68},"name":"IndianRed1"},{"colorId":204,"hexString":"#ff5f87","rgb":{"r":255,"g":95,"b":135},"hsl":{"h":345,"s":100,"l":68},"name":"IndianRed1"},{"colorId":205,"hexString":"#ff5faf","rgb":{"r":255,"g":95,"b":175},"hsl":{"h":330,"s":100,"l":68},"name":"HotPink"},{"colorId":206,"hexString":"#ff5fd7","rgb":{"r":255,"g":95,"b":215},"hsl":{"h":315,"s":100,"l":68},"name":"HotPink"},{"colorId":207,"hexString":"#ff5fff","rgb":{"r":255,"g":95,"b":255},"hsl":{"h":300,"s":100,"l":68},"name":"MediumOrchid1"},{"colorId":208,"hexString":"#ff8700","rgb":{"r":255,"g":135,"b":0},"hsl":{"h":31.7647058823529,"s":100,"l":50},"name":"DarkOrange"},{"colorId":209,"hexString":"#ff875f","rgb":{"r":255,"g":135,"b":95},"hsl":{"h":15,"s":100,"l":68},"name":"Salmon1"},{"colorId":210,"hexString":"#ff8787","rgb":{"r":255,"g":135,"b":135},"hsl":{"h":0,"s":100,"l":76},"name":"LightCoral"},{"colorId":211,"hexString":"#ff87af","rgb":{"r":255,"g":135,"b":175},"hsl":{"h":340,"s":100,"l":76},"name":"PaleVioletRed1"},{"colorId":212,"hexString":"#ff87d7","rgb":{"r":255,"g":135,"b":215},"hsl":{"h":320,"s":100,"l":76},"name":"Orchid2"},{"colorId":213,"hexString":"#ff87ff","rgb":{"r":255,"g":135,"b":255},"hsl":{"h":300,"s":100,"l":76},"name":"Orchid1"},{"colorId":214,"hexString":"#ffaf00","rgb":{"r":255,"g":175,"b":0},"hsl":{"h":41.1764705882353,"s":100,"l":50},"name":"Orange1"},{"colorId":215,"hexString":"#ffaf5f","rgb":{"r":255,"g":175,"b":95},"hsl":{"h":30,"s":100,"l":68},"name":"SandyBrown"},{"colorId":216,"hexString":"#ffaf87","rgb":{"r":255,"g":175,"b":135},"hsl":{"h":20,"s":100,"l":76},"name":"LightSalmon1"},{"colorId":217,"hexString":"#ffafaf","rgb":{"r":255,"g":175,"b":175},"hsl":{"h":0,"s":100,"l":84},"name":"LightPink1"},{"colorId":218,"hexString":"#ffafd7","rgb":{"r":255,"g":175,"b":215},"hsl":{"h":330,"s":100,"l":84},"name":"Pink1"},{"colorId":219,"hexString":"#ffafff","rgb":{"r":255,"g":175,"b":255},"hsl":{"h":300,"s":100,"l":84},"name":"Plum1"},{"colorId":220,"hexString":"#ffd700","rgb":{"r":255,"g":215,"b":0},"hsl":{"h":50.5882352941176,"s":100,"l":50},"name":"Gold1"},{"colorId":221,"hexString":"#ffd75f","rgb":{"r":255,"g":215,"b":95},"hsl":{"h":45,"s":100,"l":68},"name":"LightGoldenrod2"},{"colorId":222,"hexString":"#ffd787","rgb":{"r":255,"g":215,"b":135},"hsl":{"h":40,"s":100,"l":76},"name":"LightGoldenrod2"},{"colorId":223,"hexString":"#ffd7af","rgb":{"r":255,"g":215,"b":175},"hsl":{"h":30,"s":100,"l":84},"name":"NavajoWhite1"},{"colorId":224,"hexString":"#ffd7d7","rgb":{"r":255,"g":215,"b":215},"hsl":{"h":0,"s":100,"l":92},"name":"MistyRose1"},{"colorId":225,"hexString":"#ffd7ff","rgb":{"r":255,"g":215,"b":255},"hsl":{"h":300,"s":100,"l":92},"name":"Thistle1"},{"colorId":226,"hexString":"#ffff00","rgb":{"r":255,"g":255,"b":0},"hsl":{"h":60,"s":100,"l":50},"name":"Yellow1"},{"colorId":227,"hexString":"#ffff5f","rgb":{"r":255,"g":255,"b":95},"hsl":{"h":60,"s":100,"l":68},"name":"LightGoldenrod1"},{"colorId":228,"hexString":"#ffff87","rgb":{"r":255,"g":255,"b":135},"hsl":{"h":60,"s":100,"l":76},"name":"Khaki1"},{"colorId":229,"hexString":"#ffffaf","rgb":{"r":255,"g":255,"b":175},"hsl":{"h":60,"s":100,"l":84},"name":"Wheat1"},{"colorId":230,"hexString":"#ffffd7","rgb":{"r":255,"g":255,"b":215},"hsl":{"h":60,"s":100,"l":92},"name":"Cornsilk1"},{"colorId":231,"hexString":"#ffffff","rgb":{"r":255,"g":255,"b":255},"hsl":{"h":0,"s":0,"l":100},"name":"Grey100"},{"colorId":232,"hexString":"#080808","rgb":{"r":8,"g":8,"b":8},"hsl":{"h":0,"s":0,"l":3},"name":"Grey3"},{"colorId":233,"hexString":"#121212","rgb":{"r":18,"g":18,"b":18},"hsl":{"h":0,"s":0,"l":7},"name":"Grey7"},{"colorId":234,"hexString":"#1c1c1c","rgb":{"r":28,"g":28,"b":28},"hsl":{"h":0,"s":0,"l":10},"name":"Grey11"},{"colorId":235,"hexString":"#262626","rgb":{"r":38,"g":38,"b":38},"hsl":{"h":0,"s":0,"l":14},"name":"Grey15"},{"colorId":236,"hexString":"#303030","rgb":{"r":48,"g":48,"b":48},"hsl":{"h":0,"s":0,"l":18},"name":"Grey19"},{"colorId":237,"hexString":"#3a3a3a","rgb":{"r":58,"g":58,"b":58},"hsl":{"h":0,"s":0,"l":22},"name":"Grey23"},{"colorId":238,"hexString":"#444444","rgb":{"r":68,"g":68,"b":68},"hsl":{"h":0,"s":0,"l":26},"name":"Grey27"},{"colorId":239,"hexString":"#4e4e4e","rgb":{"r":78,"g":78,"b":78},"hsl":{"h":0,"s":0,"l":30},"name":"Grey30"},{"colorId":240,"hexString":"#585858","rgb":{"r":88,"g":88,"b":88},"hsl":{"h":0,"s":0,"l":34},"name":"Grey35"},{"colorId":241,"hexString":"#626262","rgb":{"r":98,"g":98,"b":98},"hsl":{"h":0,"s":0,"l":37},"name":"Grey39"},{"colorId":242,"hexString":"#6c6c6c","rgb":{"r":108,"g":108,"b":108},"hsl":{"h":0,"s":0,"l":40},"name":"Grey42"},{"colorId":243,"hexString":"#767676","rgb":{"r":118,"g":118,"b":118},"hsl":{"h":0,"s":0,"l":46},"name":"Grey46"},{"colorId":244,"hexString":"#808080","rgb":{"r":128,"g":128,"b":128},"hsl":{"h":0,"s":0,"l":50},"name":"Grey50"},{"colorId":245,"hexString":"#8a8a8a","rgb":{"r":138,"g":138,"b":138},"hsl":{"h":0,"s":0,"l":54},"name":"Grey54"},{"colorId":246,"hexString":"#949494","rgb":{"r":148,"g":148,"b":148},"hsl":{"h":0,"s":0,"l":58},"name":"Grey58"},{"colorId":247,"hexString":"#9e9e9e","rgb":{"r":158,"g":158,"b":158},"hsl":{"h":0,"s":0,"l":61},"name":"Grey62"},{"colorId":248,"hexString":"#a8a8a8","rgb":{"r":168,"g":168,"b":168},"hsl":{"h":0,"s":0,"l":65},"name":"Grey66"},{"colorId":249,"hexString":"#b2b2b2","rgb":{"r":178,"g":178,"b":178},"hsl":{"h":0,"s":0,"l":69},"name":"Grey70"},{"colorId":250,"hexString":"#bcbcbc","rgb":{"r":188,"g":188,"b":188},"hsl":{"h":0,"s":0,"l":73},"name":"Grey74"},{"colorId":251,"hexString":"#c6c6c6","rgb":{"r":198,"g":198,"b":198},"hsl":{"h":0,"s":0,"l":77},"name":"Grey78"},{"colorId":252,"hexString":"#d0d0d0","rgb":{"r":208,"g":208,"b":208},"hsl":{"h":0,"s":0,"l":81},"name":"Grey82"},{"colorId":253,"hexString":"#dadada","rgb":{"r":218,"g":218,"b":218},"hsl":{"h":0,"s":0,"l":85},"name":"Grey85"},{"colorId":254,"hexString":"#e4e4e4","rgb":{"r":228,"g":228,"b":228},"hsl":{"h":0,"s":0,"l":89},"name":"Grey89"},{"colorId":255,"hexString":"#eeeeee","rgb":{"r":238,"g":238,"b":238},"hsl":{"h":0,"s":0,"l":93},"name":"Grey93"}]'

colorID = json.loads(map)

# From: https://gist.github.com/nice/51e55edc8bf63fd28aa0
# Thanks to ctrl_phil : http://stackoverflow.com/users/1570041/ctrl-phil
# Answered at: http://stackoverflow.com/a/11770026/2102830

colors = {
    '000000':  '16', '00005f':  '17', '000087':  '18', '0000af':  '19', '0000d7':  '20',
    '0000ff':  '21', '005f00':  '22', '005f5f':  '23', '005f87':  '24', '005faf':  '25',
    '005fd7':  '26', '005fff':  '27', '008700':  '28', '00875f':  '29', '008787':  '30',
    '0087af':  '31', '0087d7':  '32', '0087ff':  '33', '00af00':  '34', '00af5f':  '35',
    '00af87':  '36', '00afaf':  '37', '00afd7':  '38', '00afff':  '39', '00d700':  '40',
    '00d75f':  '41', '00d787':  '42', '00d7af':  '43', '00d7d7':  '44', '00d7ff':  '45',
    '00ff00':  '46', '00ff5f':  '47', '00ff87':  '48', '00ffaf':  '49', '00ffd7':  '50',
    '00ffff':  '51', '5f0000':  '52', '5f005f':  '53', '5f0087':  '54', '5f00af':  '55',
    '5f00d7':  '56', '5f00ff':  '57', '5f5f00':  '58', '5f5f5f':  '59', '5f5f87':  '60',
    '5f5faf':  '61', '5f5fd7':  '62', '5f5fff':  '63', '5f8700':  '64', '5f875f':  '65',
    '5f8787':  '66', '5f87af':  '67', '5f87d7':  '68', '5f87ff':  '69', '5faf00':  '70',
    '5faf5f':  '71', '5faf87':  '72', '5fafaf':  '73', '5fafd7':  '74', '5fafff':  '75',
    '5fd700':  '76', '5fd75f':  '77', '5fd787':  '78', '5fd7af':  '79', '5fd7d7':  '80',
    '5fd7ff':  '81', '5fff00':  '82', '5fff5f':  '83', '5fff87':  '84', '5fffaf':  '85',
    '5fffd7':  '86', '5fffff':  '87', '870000':  '88', '87005f':  '89', '870087':  '90',
    '8700af':  '91', '8700d7':  '92', '8700ff':  '93', '875f00':  '94', '875f5f':  '95',
    '875f87':  '96', '875faf':  '97', '875fd7':  '98', '875fff':  '99', '878700': '100',
    '87875f': '101', '878787': '102', '8787af': '103', '8787d7': '104', '8787ff': '105',
    '87af00': '106', '87af5f': '107', '87af87': '108', '87afaf': '109', '87afd7': '110',
    '87afff': '111', '87d700': '112', '87d75f': '113', '87d787': '114', '87d7af': '115',
    '87d7d7': '116', '87d7ff': '117', '87ff00': '118', '87ff5f': '119', '87ff87': '120',
    '87ffaf': '121', '87ffd7': '122', '87ffff': '123', 'af0000': '124', 'af005f': '125',
    'af0087': '126', 'af00af': '127', 'af00d7': '128', 'af00ff': '129', 'af5f00': '130',
    'af5f5f': '131', 'af5f87': '132', 'af5faf': '133', 'af5fd7': '134', 'af5fff': '135',
    'af8700': '136', 'af875f': '137', 'af8787': '138', 'af87af': '139', 'af87d7': '140',
    'af87ff': '141', 'afaf00': '142', 'afaf5f': '143', 'afaf87': '144', 'afafaf': '145',
    'afafd7': '146', 'afafff': '147', 'afd700': '148', 'afd75f': '149', 'afd787': '150',
    'afd7af': '151', 'afd7d7': '152', 'afd7ff': '153', 'afff00': '154', 'afff5f': '155',
    'afff87': '156', 'afffaf': '157', 'afffd7': '158', 'afffff': '159', 'd70000': '160',
    'd7005f': '161', 'd70087': '162', 'd700af': '163', 'd700d7': '164', 'd700ff': '165',
    'd75f00': '166', 'd75f5f': '167', 'd75f87': '168', 'd75faf': '169', 'd75fd7': '170',
    'd75fff': '171', 'd78700': '172', 'd7875f': '173', 'd78787': '174', 'd787af': '175',
    'd787d7': '176', 'd787ff': '177', 'd7af00': '178', 'd7af5f': '179', 'd7af87': '180',
    'd7afaf': '181', 'd7afd7': '182', 'd7afff': '183', 'd7d700': '184', 'd7d75f': '185',
    'd7d787': '186', 'd7d7af': '187', 'd7d7d7': '188', 'd7d7ff': '189', 'd7ff00': '190',
    'd7ff5f': '191', 'd7ff87': '192', 'd7ffaf': '193', 'd7ffd7': '194', 'd7ffff': '195',
    'ff0000': '196', 'ff005f': '197', 'ff0087': '198', 'ff00af': '199', 'ff00d7': '200',
    'ff00ff': '201', 'ff5f00': '202', 'ff5f5f': '203', 'ff5f87': '204', 'ff5faf': '205',
    'ff5fd7': '206', 'ff5fff': '207', 'ff8700': '208', 'ff875f': '209', 'ff8787': '210',
    'ff87af': '211', 'ff87d7': '212', 'ff87ff': '213', 'ffaf00': '214', 'ffaf5f': '215',
    'ffaf87': '216', 'ffafaf': '217', 'ffafd7': '218', 'ffafff': '219', 'ffd700': '220',
    'ffd75f': '221', 'ffd787': '222', 'ffd7af': '223', 'ffd7d7': '224', 'ffd7ff': '225',
    'ffff00': '226', 'ffff5f': '227', 'ffff87': '228', 'ffffaf': '229', 'ffffd7': '230',
    'ffffff': '231', '080808': '232', '121212': '233', '1c1c1c': '234', '262626': '235',
    '303030': '236', '3a3a3a': '237', '444444': '238', '4e4e4e': '239', '585858': '240',
    '626262': '241', '6c6c6c': '242', '767676': '243', '808080': '244', '8a8a8a': '245',
    '949494': '246', '9e9e9e': '247', 'a8a8a8': '248', 'b2b2b2': '249', 'bcbcbc': '250',
    'c6c6c6': '251', 'd0d0d0': '252', 'dadada': '253', 'e4e4e4': '254', 'eeeeee': '255',
}

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
    "x3270*fileMenuButton*borderColor", 
	"x3270*optionsMenuButton*borderColor",
	"x3270*connectMenuButton*borderColor",
	"x3270*reconnectButton*borderColor",
	"x3270*macrosMenuButton*borderColor",
	"x3270*menuBarContainer.borderColor",
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

def Decompose(hexval):
    return float(int(hexval[0:2], 16)), float(int(hexval[2:4], 16)), float(int(hexval[4:6], 16))

def Normalize(r, g, b):
    magsqr = r*r + g*g + b*b
    if magsqr < 0.0001:
        return 0.0, 0.0, 0.0
    n = 1.0 / math.sqrt(magsqr)
    return r*n, g*n, b*n

def ColorDist(c1, c2):
    c1r, c1g, c1b = Decompose(c1)
    c2r, c2g, c2b = Decompose(c2)

    dr = c1r - c2r
    dg = c1g - c2g
    db = c1b - c2b
    return dr*dr + dg*dg + db*db

def BestMatch(hexval):
    best = None
    bestdist = 0.0
    for key in colors.keys():
        dist = ColorDist(hexval, key)
        if best is None or dist < bestdist:
            best = colors[key]
            bestdist = dist
    return best

def main():
   
    color_names = ["*background","*color0", "*color1", "*color2", "*color3", "*color4", "*color5", "*color6", "*color7", "*color8", "*color9", "*color10", "*color11", "*color12", "*color13", "*color14", "*color15", "*foreground"]
    x3270colors = {
                    "*color0" : ["0"],
                     "*color1" : ["1"],
                     "*color2" : ["2"],
                     "*color3" : ["3"],
                     "*color4" : ["4"],
                    "*color5" : ["5"],
                    "*color6" : ["6"],
                     "*color7" : ["7"],
                      "*color8" : ["8"],
                      "*color9" : ["9"],
                     "*color10" : ["10"],
                     "*color11" : ["11"],
                     "*color12" : ["12"],
                     "*color13" : ["13"],
                     "*color14" : ["14"],
                     "*color15" : ["15"],
                     "*background": ["17"]
                     }



    xcolors = [None] * 18
    mapc = [None] * 23
    mapc[18] = "white"
    mapc[19] = 4
    mapc[20] = 2
    mapc[21] = 1
    mapc[22] = 15
    mapc[16] = "black"

    if len(sys.argv) < 2:
        print("Usage: {} <.Xresources file from https://ciembor.github.io/4bit/ or terminal.sexy>".format(sys.argv[0]))
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            for color in color_names:
                if re.findall('\\b'+color[1:]+'\\b', line):
                    num256 = BestMatch(line.split()[1][1:])
                    for Xcolor in colorID:
                        if Xcolor['colorId'] == int(num256):
                            try:
                                x3270colors[color].append(Xcolor['name'])
                            except KeyError:
                                foreground = Xcolor['name']
                            

    for i in x3270colors:
        xcolors[int(x3270colors[i][0])] =  x3270colors[i][1]

# Example Color Scheme
# x3270.colorScheme: demo
# ! Then we set the colors we need
# ! These colors were picked for the class
# x3270.colorScheme.demo: \
# 	black midnightBlue darkred brown \
# 	darkGreen midnightblue darkgoldenrod black \
# 	black midnightblue SaddleBrown purple \
# 	DarkGreen darkTurquoise grey black \
# 	black white dimGrey 4 \
#  2 1 0

    print("! Menu Colors")
    print("! Foreground")
    for i in menus_foreground:
        print("{}:\t {}".format(i,foreground))
    print("! Critical")
    for i in critical_foreground:
        print("{}:\t {}".format(i,x3270colors["*color1"][1]))
    print("! Backgrounds")
    for i in menus_background:
        print("{}:\t {}".format(i,x3270colors["*background"][1]))
    print("! Borders")
    for i in menus_border:
        print("{}:\t {}".format(i,x3270colors["*background"][1]))
    
    print("x3270*menuBarContainer.borderWidth: 0")
    print("x3270*value.borderColor: \t{}".format(foreground))
    print("x3270*value.foreground: \t{}".format(foreground))

    print("! Generating new .x3270pro theme")
    print("! Copy and paste to ~/.x3270pro")
    print("x3270.colorScheme: new\nx3270.colorScheme.new:",end = ' ')
    
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
    print()

main()