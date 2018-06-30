import os
import webapp2
from handlers import V0Handler,V0cv

debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

webapp2_config = {
	'webapp2_extras.sessions': {
		'secret_key': '4/ix2rOzIkM0Ed0CuoNxCORwTUsYEYKoSu1miFPLGL1WI'
	}
}

wsgi = webapp2.WSGIApplication([
		webapp2.Route('/', handler=V0Handler, name='V0home', methods=['GET']),
		webapp2.Route('/cv', handler=V0cv, name='V0home', methods=['GET'])
	], debug=debug, config=webapp2_config)	