import http.client
import json

def login(site, uname, pwd):
    connection = http.client.HTTPSConnection(site)
    body="""
    {{
        "username": "{}",
        "password": "{}"
    }}
     """.format(uname, pwd)

    headers = { 'Connection': 'keep-alive',
                'Content-Type': 'application/json; charset=UTF-8',
                'Content-Length': str(len(body)) 
              }
    connection.request( method = "POST", 
                    body = body.encode('utf-8'), 
                    url = "/api/auth/login/", 
                    headers = headers)

    response = connection.getresponse()
    response_body = response.read()    
    result = json.loads(response_body.decode('utf-8'))
    return connection, result['uid'], result['sid']


def create_inbox(connection, uid, sid, recipients, text):
    recipients_objects = { "{{ \"id\": {} }}".format(r) for r in recipients }

    body="""
    {{
        "text": "{}", 
        "recipients": [
            {}
        ]
    }}
     """.format( text,
                 ", ".join(recipients_objects)
                 )
    headers = { 'Connection': 'keep-alive',
                'Content-Type': 'application/json; charset=UTF-8',
                'X-Futuware-UID': uid,
                'X-Futuware-SID': sid 
                }

    connection.request( method = "POST", 
                    body = body,
                    url = "/api/inbox/", 
                    headers = headers)

    response = connection.getresponse()
    response_body = response.read()
    if(response.status != 200):
        print(response.status, response_body)
        return None
    result = json.loads(response_body.decode('utf-8'))
    return result['id'] if 'id' in result else None

if __name__ == '__main__':
    import sys
    import os
    configfile="~/.config/qj/qjconf.py"
    sys.path.append(os.path.dirname(os.path.expanduser(configfile)))
    import qjconf
    connection, uid, sid = login(qjconf.site, qjconf.user, qjconf.password)
    inbox_id = create_inbox(connection, uid, sid, { qjconf.test_user }, qjconf.test_text)
    print(inbox_id)