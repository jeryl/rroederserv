from pyramid.view import view_config
from pyramid.httpexceptions import HTTPClientError

class EnhanceYourCalm(HTTPClientError):
    code = 420
    title = "Enhance your calm"
    explanation = ('Enhance your calm, bruh.')

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'rroeder'}

@view_config(route_name='rroeder', renderer='templates/rroeder.pt')
def rroeder_view(request):
    raise EnhanceYourCalm()
