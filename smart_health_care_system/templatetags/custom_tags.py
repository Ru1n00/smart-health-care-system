from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(name='param_replace')
@stringfilter
def param_replace(value, page_number):
    'sfdf/fjldsfj/?r=2&page=3'
    params = value.split('&')
    found = False
    for index, param in enumerate(params):
        if 'page' in param:
            page_param_index = index
            found = True
            break
    if found:
        print(params[page_param_index], 'page param index')
        if '?' in params[page_param_index]:
            param = params[page_param_index].split('?')
            param[1] = param[1][:5] + str(page_number)
            param = '?'.join(param)
            params[page_param_index] = param
            print(param, 'inside ? if \n\n\n\n')
        else:
            params[page_param_index] = params[page_param_index][:5] + str(page_number)
            print(param, params, 'outside ? if \n\n\n\n')
    else:
        params.append('page='+str(page_number))
    params = '&'.join(params)
    print(value, params, 'sfdbfjds\n\n\n')
    return params
