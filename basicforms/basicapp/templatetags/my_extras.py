from django import template

register = template.Library()

def cut(value, args):
    value = value.replace(args, '')
    return value

register.filter('cut', cut)
