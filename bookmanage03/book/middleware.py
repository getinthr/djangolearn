from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class TestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("11111Request received")

        # username = request.COOKIES.get('username')
        # if not username:
        #     print("No username cookie")
        # else:
        #     print("Username cookie found")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("11111View received")

class TestMiddleware2(MiddlewareMixin):

    def process_request(self, request):
        print("2222Request received")

        # username = request.COOKIES.get('username')
        # if not username:
        #     print("No username cookie")
        # else:
        #     print("Username cookie found")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("22222View received")

