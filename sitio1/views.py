from django.http import Http404, HttpResponse
import datetime

html="""
<!DOCTYPE html>
<html lang "es">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<meta name="robots" content="NONE, NOARCHIVE">
<title>HOLA MUNDO</title>
<style type="text/css">
html * {padding:0; margin:0;}
body * {padding:10px 20px;}
body ** {padding:0;}
body {font:small sans-serif;}
body>div {border-bottom:1px solid #ddd;}
h1 {font-weight:normal;}
#summary {background: #e0ebff;}
</style>
</head>
<body>
<div id="summary">
<h1>¡HOLA MUNDO!</h1>
</div>
</body>
</html>
"""


def hola(request):
	return HttpResponse(html)

def raiz(request):
	return HttpResponse("esta es la raiz")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>La fecha ahora es: %s.</body></html>" % now
    return HttpResponse(html)

def horas_adelante(request, offset):
	try:
		offset= int(offset)
	except ValueError:
		raise Http404()

	dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
	html2="<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (offset,dt)
	return HttpResponse(html2)