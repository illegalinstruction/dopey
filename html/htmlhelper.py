""" html page generator, public domain

So I can use wikipedia-style syntax to create my pages.
"""

def is_image(what):
    if not '.' in what: return False
    ext = what.split('.')[-1]
    ext = ext.lower()
    return ext in ['png', 'gif', 'jpg', 'jpeg']

def make_narrow(html, width='60%'):
    s = ''
    s += '<table border="0" width="%s"><tr><td>\n' % width
    s += html
    s += '</td></tr></table>\n'
    return s

def wiki2html(text):
    return Wiki2html(text).html

class Wiki2html:
    def __init__(self, text):
        self.text = text
        self.html = self.run(text)

    def __str__(self):
        return self.html

    def run(self, text):
        text = text.strip()
        text = text.replace('\n\n', '<p>\n\n')
        text = text.replace('"', '&quot;')
        text = expand_tag(text, '[[', ']]', self.doublelink)
        text = expand_tag(text, '[', ']', self.singlelink)
        text = expand_tag(text, "'''", "'''", self.bold)
        text = expand_tag(text, "===", "===", self.title3)
        text = expand_tag(text, "==", "==", self.title2)
        return text

    def link(self, parts):
        parts = [s.strip() for s in parts]
        dst = parts.pop(0)
        name = dst
        if parts:
            name = parts[-1]

        for s in ['image:', 'Image:', 'bild:', 'Bild:']:
            dst = dst.replace(s, '')

        if is_image(dst):
            s = '<img src="%s"' % dst
            d = {}
            d['align'] = 'left'
            d['hspace'] = '10'
            d['vspace'] = '10'
            for option in parts:
                if option == 'left':
                    d['align'] = 'left'
                elif option == 'right':
                    d['align'] = 'right'
                elif option == 'border':
                    d['border'] = '1'
                else:
                    s += ' ' + option
            for name, value in d.items():
                s += ' %s="%s"' % (name, value)
            s += '> \n'
            return s
        else:
            return ' <a href="%s">%s</a> ' % (dst, name)

    def doublelink(self, text):
        return self.link(text.split('|'))

    def singlelink(self, text):
        return self.link(text.split(' '))

    def bold(self, text):
        return '<b>%s</b>' % text

    def title(self, number, text):
        return '\n\n<br clear="all">\n<h%d>%s</h%d>\n\n' % (number, text, number)
    def title2(self, text): return self.title(2, text)
    def title3(self, text): return self.title(3, text)


def expand_tag(text, tag_open, tag_close, handler):
    parts = text.split(tag_open)
    if tag_open == tag_close:
        #assert len(parts) % 2 == 0
        expand = False
        text = ''
        for p in parts:
            if expand:
                text += handler(p)
            else:
                text += p
            expand = not expand
    else:
        text, parts = parts[0], parts[1:]
        for p in parts:
            i, t = p.split(tag_close)
            text += handler(i)
            text += t
    return text
