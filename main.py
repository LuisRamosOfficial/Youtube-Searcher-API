from modules import get_JsonSearch
from flask import *
import json, time, urllib.parse
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def home_page():
    objected = {"page": "Page is succesfully loaded", "time": time.time()}
    
    return render_template('landing.html')



# Search youtube videos API Endpoint

@app.route('/search')
@cross_origin()
def request_page():
    search_query = str(request.args.get('q'))
    
    url_search = 'https://www.youtube.com/results?' + urllib.parse.urlencode({"search_query": search_query})
    
    return get_JsonSearch(url_search)
if __name__ == '__main__':
    app.run(port=4040)