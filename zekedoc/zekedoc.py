import mistletoe
import sys
from zekedoc.renderer import ZekeRenderer

header = '''
<!DOCTYPE html>
<head>
<meta charset='UTF-8'>
<title>Zeke Medley</title>
<link rel="stylesheet" href="styles/type.css"></link>
<link rel="stylesheet" href="styles/position.css"></link>
<link href="styles/prism.css" rel="stylesheet" />
<!-- Favicon is GitHub profile image. -->
<link rel="icon" href="https://avatars1.githubusercontent.com/u/30676292?s=180&v=4">
</head>
<body>
<div class="wrapper">
    <nav>
      <a href="index.md"><img src="media/logo.gif" alt="ZM Logo"></a>
      <ul>
          <li><a href="https://www.linkedin.com/in/zeke-medley-b1261a173/">Linkedin</a></li>
          <li><a href="https://github.com/ZekeMedley">GitHub</a></li>
          <li><a href="interesting-things.md">Interesting</a></li>
      </ul>
    </nav>
<section id="main">
'''

footer = '''
</section>
</div>
<script src="styles/prism.js"></script>
</body>
</html>
'''

def render_file(f):
    return header + mistletoe.markdown(f, ZekeRenderer) + footer
