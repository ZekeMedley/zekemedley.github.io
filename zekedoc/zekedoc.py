import mistletoe
import sys
from zekedoc.renderer import ZekeRenderer

header = '''
<!DOCTYPE html>
<head>
<meta charset='UTF-8'>
<title>Zeke</title>
<link rel="stylesheet" href="styles/type.css"></link>
<link rel="stylesheet" href="styles/position.css"></link>
<!-- Favicon is GitHub profile image. -->
<link rel="icon" href="https://avatars1.githubusercontent.com/u/30676292?s=180&v=4">
</head>
<body>
<div class="col">
'''

footer = '''
<br>
<br>
</body>
</html>
'''

def render_file(f):
    return header + mistletoe.markdown(f, ZekeRenderer) + footer

