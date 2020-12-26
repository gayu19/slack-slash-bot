import json
from chalice import Chalice, Cron
from urllib.parse import parse_qs
import os
from chalicelib.helpers import is_root_domain


app = Chalice(app_name='slash_bot')
app.debug = True       


@app.route('/root-domain', methods=['POST'], content_types=['application/json',
                                                         'application/x-www-form-urlencoded'])
def root_domain():
    parsed = parse_qs(app.current_request.raw_body.decode())    
    domain = parsed.get('text')    
    if domain is None:
        message = 'No input given for the command \n Usage: `/root-domain domain.com`'
        return {
            'statusCode': 200,
            'response_type': 'ephemeral',
            'text': message                
        }
    else:        
        info = is_root_domain(domain[0])
        print(info)
        return {
            'statusCode': 200,
            'response_type': 'ephemeral',
            'text': info
        }
    
        





# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
