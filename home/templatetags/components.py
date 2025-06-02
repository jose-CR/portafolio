from django import template
from django.template import loader, Node, Variable
from django.utils.html import mark_safe
from django.utils.translation import gettext as _

register = template.Library()

# card
@register.tag(name="card")
def do_card(parser, token):
    try:
        tag_name, title = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument for the title"
            % token.contents.split()[0]
        )

    # ¡Esto también estaba mal! Debe pasarse como tupla:
    nodelist = parser.parse(('endcard',))
    parser.delete_first_token()

    return CardNode(title, nodelist)

class CardNode(Node):  # CORRECTO
    def __init__(self, title, nodelist):
        self.title = Variable(title)
        self.nodelist = nodelist

    def render(self, context):
        title = self.title.resolve(context)
        content = self.nodelist.render(context)

        translated_title = _(title)

        tpl = loader.get_template('components/card.html')
        if hasattr(context, 'request'):
            return tpl.render({
                'title': translated_title,
                'content': mark_safe(content),
                **context.flatten(),
            }, request=context['request'])
        else:
            return tpl.render({
                'title': translated_title,
                'content': mark_safe(content),
                **context.flatten(),
            })
#------------------------------------------------------------------

@register.inclusion_tag('components/form.html')
def r_form(form, title, contents, content_button, name=None, href=None, href_text=None):
    if isinstance(contents, str):
        contents = [campo.strip() for campo in contents.split(',')]
    
    campos = {field: form[field] for field in contents}

    return {
        'form': form,
        'title': title,
        'contents': campos,
        'content_button': content_button,
        'name': name,
        'href': href,
        'href_text': href_text
    }

@register.inclusion_tag('components/button.html')
def button(title_button, href=None, parent_class=None, btn_class='', align='center', size='md', color='primary', text_color='white', name_button="name_button"):
    
    #Renderiza un botón reutilizable con varias opciones de estilo.

    #Args:
    #- title_button (str): Texto dentro del botón.
    #- name (str): es para darle un valor a la etiqueta name .
    #- href (str): Si se proporciona, se usa un <a>, si no, <button>.
    #- parent_class (str): Clase personalizada para el contenedor padre.
    #- btn_class (str): Clases extra para el botón.
    #- align (str): Alineación del botón (left, center, right). Default: center.
    #- size (str): Tamaño del botón (sm, md, lg). Default: sm.
    #- color (str): Color del fondo. Puede ser clase ('primary') o código hexadecimal ('#ff0000').
    #- text_color (str): Color del texto. Igual que color.

    return {
        'title_button': title_button,
        'name_button': name_button,
        'href': href,
        'parent_class': parent_class,
        'btn_class': btn_class,
        'align': align,
        'size': size,
        'color': color,
        'text_color': text_color,
    }
