from __future__ import print_function

import cherrypy
import os
import sys
import simplejson as json

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
                json_news = []
                ##json_album = json_parser.GetAlbum("table", "album","pagenum")

                print(album)

                if( album == "wolves_div" ):
                    json_news = wolves_div
                    print("wolves")

                if( album == "northern_div" ):
                    json_news = northern_div
                    print("northern")

                if( album == "tromso_div" ):
                    json_news = tromso_div
                    print("tromso")

                if( album == "londonzoo_div" ):
                    json_news = londonzoo_div
                    print("zoo")

                if( album == "pentax_div" ):
                    json_news = pentax_div
                    print("pentax")

                if( album == "macro_div" ):
                    json_news = macro_div
                    print("macro")


                print(json.dumps(payload))
                return json_news

wolves_div = [
    {"url":"./img/gallery/wolf_polar.JPG", "alt":"Wolf", "thumb":"blank"},
    {"url":"./img/gallery/wolf_polar.JPG", "alt":"Wolf", "thumb":"blank"},
    {"url":"./img/gallery/wolf_polar.JPG", "alt":"Wolf", "thumb":"blank"},
    {"url":"./img/gallery/wolf_polar.JPG", "alt":"Wolf", "thumb":"blank"},
    {"url":"./img/gallery/wolf_polar.JPG", "alt":"Wolf", "thumb":"blank"},
    {"url":"./img/gallery/wolf_polar.JPG", "alt":"Wolf", "thumb":"blank"}

    ]

northern_div = [
    {"url":"./img/gallery/northern_lights.JPG", "alt":"Northern Lights", "thumb":"blank"},
    {"url":"./img/gallery/northern_lights.JPG", "alt":"Northern Lights", "thumb":"blank"},
    {"url":"./img/gallery/northern_lights.JPG", "alt":"Northern Lights", "thumb":"blank"},
    {"url":"./img/gallery/northern_lights.JPG", "alt":"Northern Lights", "thumb":"blank"},
    {"url":"./img/gallery/northern_lights.JPG", "alt":"Northern Lights", "thumb":"blank"},
    {"url":"./img/gallery/northern_lights.JPG", "alt":"Northern Lights", "thumb":"blank"}
]

tromso_div = [
    {"url":"./img/gallery/duck_tromso.JPG", "alt":"Duck Tromso", "thumb":"blank"},
    {"url":"./img/gallery/duck_tromso.JPG", "alt":"Duck Tromso", "thumb":"blank"},
    {"url":"./img/gallery/duck_tromso.JPG", "alt":"Duck Tromso", "thumb":"blank"},
    {"url":"./img/gallery/duck_tromso.JPG", "alt":"Duck Tromso", "thumb":"blank"},
    {"url":"./img/gallery/duck_tromso.JPG", "alt":"Duck Tromso", "thumb":"blank"},
    {"url":"./img/gallery/duck_tromso.JPG", "alt":"Duck Tromso", "thumb":"blank"}
]

londonzoo_div = [
    {"url":"./img/gallery/bird_oslo.JPG", "alt":"Bird Oslo", "thumb":"blank"},
    {"url":"./img/gallery/bird_oslo.JPG", "alt":"Bird Oslo", "thumb":"blank"},
    {"url":"./img/gallery/bird_oslo.JPG", "alt":"Bird Oslo", "thumb":"blank"},
    {"url":"./img/gallery/bird_oslo.JPG", "alt":"Bird Oslo", "thumb":"blank"},
    {"url":"./img/gallery/bird_oslo.JPG", "alt":"Bird Oslo", "thumb":"blank"},
    {"url":"./img/gallery/bird_oslo.JPG", "alt":"Bird Oslo", "thumb":"blank"}
]

pentax_div = [
    {"url":"img/gallery/fighting_polar.JPG","alt":"Fighting Reindeer", "thumb":"blank"},
    {"url":"img/gallery/fighting_polar.JPG","alt":"Fighting Reindeer", "thumb":"blank"},
    {"url":"img/gallery/fighting_polar.JPG","alt":"Fighting Reindeer", "thumb":"blank"},
    {"url":"img/gallery/fighting_polar.JPG","alt":"Fighting Reindeer", "thumb":"blank"},
    {"url":"img/gallery/fighting_polar.JPG","alt":"Fighting Reindeer", "thumb":"blank"},
    {"url":"img/gallery/fighting_polar.JPG","alt":"Fighting Reindeer", "thumb":"blank"}
]


if __name__ == '__main__':
	pypath = os.path.dirname( sys.argv[0])
	rootdir = os.path.abspath ( os.path.join (pypath, '..'))

        app = App()
        app.data = Data()


	app = cherrypy.tree.mount( app, '/', config=os.path.join( pypath, 'app.config' ) )
	app.merge({ '/' : {'tools.staticdir.root' : rootdir } } )
	cherrypy.config.update({'server.socket_host': 'localhost',
                        'server.socket_port': 80,
                       })
	cherrypy.engine.start()
	cherrypy.engine.block()

