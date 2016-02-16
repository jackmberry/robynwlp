from __future__ import print_function

import cherrypy
import os
import sys

class App( object ): 
	exposed = True
	
	def GET( self ): 
		cfg = cherrypy.request.config
		return open( os.path.join ( cfg['tools.staticdir.root'], cfg[ 'tools.staticdir.dir' ], 'index.html' ))

if __name__ == '__main__':
	pypath = os.path.dirname( sys.argv[0])
	rootdir = os.path.abspath ( os.path.join (pypath, '..'))
	app = App()

	app = cherrypy.tree.mount( app, '/', config=os.path.join( pypath, 'app.config' ) )
	app.merge({ '/' : {'tools.staticdir.root' : rootdir } } )
	cherrypy.config.update({'server.socket_host': '178.62.98.183',
                        'server.socket_port': 80,
                       })
	cherrypy.engine.start()
	cherrypy.engine.block()

