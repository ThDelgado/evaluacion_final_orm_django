from django  import template
import locale


register = template.Library()


@register.filter
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL, 'es_Cl.UTF-8')
        formatted_value = locale.format_string("%0.0f", value, grouping=True)
        return formatted_value
    
    except (ValueError, TypeError, locale.Error):
        return value 
   