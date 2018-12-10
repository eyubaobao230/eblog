from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from endblog.models import SuperUser


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # process_request中可以不写在return，或者return None
        # if request.path in ['/login/', '/register/']:
        if '/login/' in request.path or '/sblog/' in request.path:
            return None

        user_id = request.session.get('user_id')
        if user_id:
            user = SuperUser.objects.get(pk=user_id)
            request.user = user
            return None
        else:
            return HttpResponseRedirect('/blog/login/')

    def process_response(self, request, response):
        return response