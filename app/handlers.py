
#!/usr/bin/env
#-- coding: utf-8 --
# coding: utf-8


import random
import webapp2
from datetime import datetime
from webapp2_extras import jinja2, auth, sessions


class BaseHandler(webapp2.RequestHandler):
    """ Handlers Support Class, extends the standard webapp2 request handler
        to provite access to the jinja2 framework and common properties
        helpfull to all templates.
    """

    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)

    def render_template(self, filename, **template_args):
        """ override templates variables adding new params """
        template_args.update({
            # pjax requests preventing the whole page from loading
            'is_pjax': "X-PJAX" in self.request.headers
        })
        self.response.write(self.jinja2.render_template(filename, **template_args))

    def jinja2_factory(self, app):
        j = jinja2.Jinja2(app)
        j.environment.filters.update({
            # Set filters.
        })
        j.environment.globals.update({
            # Set global variables.
            'uri_for': webapp2.uri_for
        })
        return j

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(factory=self.jinja2_factory, app=self.app)

    @webapp2.cached_property
    def auth(self):
        """ allow the usage of webapp2 auth as a self.auth property on each handler """
        return auth.get_auth()


class V0Handler(BaseHandler):
    """docstring for V0Handler"""
    def get(self):
        name = 'Alex'

        template_values = {
            'time':datetime.now(),
            'name': name
        }
        self.render_template('index.html', **template_values)

class V0cv(BaseHandler):
    """docstring for V0Handler"""
    def get(self):
        name = 'Alex'

        template_values = {
            'time':datetime.now(),
            'name': name
        }
        self.render_template('curriculo.html', **template_values)
        

    
