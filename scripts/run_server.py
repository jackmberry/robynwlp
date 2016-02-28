from __future__ import print_function

import cherrypy
import os
import sys
import simplejson as json
import get_images
from bson import ObjectId

class App( object ):
	exposed = True

	def GET( self ):
		cfg = cherrypy.request.config
		return open( os.path.join ( cfg['tools.staticdir.root'], cfg[ 'tools.staticdir.dir' ], 'index.html' ))

class Data( object ):
        exposed = True

        @cherrypy.tools.json_in()
        @cherrypy.tools.json_out()

        def POST( self ):
                payload = cherrypy.request.json
                album = payload[ 'album' ]
                pagenum = payload[ 'pagenum' ]
               	print( album)
                print(pagenum)
		print(json.dumps(payload))

		json_album = get_images.getCollectionPage(album,pagenum)
		
                print(json.dumps(payload))
                print(json.dumps(json_album))
		return json.dumps(json_album)


if __name__ == '__main__':
	pypath = os.path.dirname( sys.argv[0])
	rootdir = os.path.abspath ( os.path.join (pypath, '../..'))

        app = App()
        app.data = Data()


	app = cherrypy.tree.mount( app, '/', config=os.path.join( pypath, 'app.config' ) )
	app.merge({ '/' : {'tools.staticdir.root' : rootdir } } )
	cherrypy.config.update({'server.socket_host': '178.62.98.183',
                        'server.socket_port': 80,
                       })
	cherrypy.engine.start()
	cherrypy.engine.block()

