# 自定义标签 reversal 标签里的数据进行反转处理

from django import template

register = template.Library()


class ReversalNode(template.Node):

    def __init__(self, value):
        self.value = value
        def render(self, context):
            return self.value[::-1]

# 声明并定义标签
@register.tag(name='reversal')
# parse是解析器对象，token是被解析的对象
def do_reversal(parse, token):
    try:
        # tag_name  代表标签名，即reversal
        # value 是由标签传递的数据
        tag_name, value = token.split_contents()
    except:
        raise template.TemplateSyntaxError('syntax')

    return ReversalNode(value)