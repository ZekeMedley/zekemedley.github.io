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
<div class="wrapper">
    <nav>
      <a href="index.html"><img src="media/logo6.svg" alt="ZM Logo"></a>
      <ul>
          <li><a href="https://www.linkedin.com/in/zeke-medley-b1261a173/">Linkedin</a></li>
          <li><a href="https://github.com/ZekeMedley">GitHub</a></li>
          <li><a href="interesting-things.html">Interesting</a></li>
      </ul>
    </nav>
<section id="main">
'''

footer = '''
</section>
</div>
</body>
</html>
'''

def render_file(f):
    return header + mistletoe.markdown(f, ZekeRenderer) + footer
