#converte cor RGB
def rgb_html(r=0,g=0,b=0):
    """ converte o formato da cor RGB --> Html """
    return '#%02x%02x%02x' % (r,g,b)

def html_rgb(color='#000000'):
    """ Conver o formato da cores em HTML --> RGB"""
    if color.startswith('#'):
        color=color[1:]
    r= int(color[:2], 16)
    g= int(color[2:4], 16)
    b= int(color[4:], 16)

    return r,g,b

#teste
print(rgb_html(255,255,125))
print(html_rgb())
print(html_rgb('#eeeeee'))
