from footprints.models import Footprint

def FootprintMiddleware(get_response=None):
	# One-time configuration and initialization.
	def middleware(request):
		# Code to be executed for each request before the view (and later middleware) are called.
		try:
			client_address = request.META['HTTP_X_FORWARDED_FOR']
		except:
			client_address = request.META['REMOTE_ADDR']

		Footprint.objects.create(ip=str(client_address), method=request.method, scheme=request.scheme, path=request.path, username=request.user)

		response = get_response(request)

		# Code to be executed for each request/response after the view is called.

		return response

	return middleware
