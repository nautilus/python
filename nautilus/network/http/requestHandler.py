from aiohttp import web

class RequestHandler(web.View):
    """
        The base class for nautilus http request handlers.

        Example:

            import nautilus
            from nautilus.network.http import RequestHandler, Response

            class MyService(nautilus.Service): pass

            @MyService.route('/')
            class MyRequestHandler(RequestHandler):
                async def get(self):
                    self.finish('hello')
    """

    async def post(self):
        # self.check_xsrf_cookie()
        pass

    async def options(self):
        return web.Response(status=204, body=b'')
