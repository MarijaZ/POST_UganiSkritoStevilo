#!/usr/bin/env python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class SkritoSteviloHandler(BaseHandler):
    def get(self):
        self.render_template("hello.html")

    def post(self):
        stevilka = self.request.get("vnos_2")
        secret_number = 33
        params = {"prava": stevilka,"skrita_stevilka": secret_number}
        if int(stevilka) == int(secret_number):
             return self.render_template("odgovor.html", params)
        else:
            return self.render_template("nepravilno.html", params)


app = webapp2.WSGIApplication([
    webapp2.Route('/skrita_stevilka', SkritoSteviloHandler),
    webapp2.Route('/odgovor', SkritoSteviloHandler),
    webapp2.Route('/nepravilno', SkritoSteviloHandler)
], debug=True)
# POST_UganiSkritoStevilo
