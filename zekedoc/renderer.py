from mistletoe.html_renderer import HTMLRenderer

class ZekeRenderer(HTMLRenderer):
    def render_image(self, token):
        template = '<img class="med-img" src="{}" alt="{}"{} />'
        if token.title:
            title = ' title="{}"'.format(self.escape_html(token.title))
        else:
            title = ''
        return template.format(token.src, self.render_to_plain(token), title)
