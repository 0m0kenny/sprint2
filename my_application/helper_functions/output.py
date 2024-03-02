from helper_functions import user_input, get_xml

def output(response):
    '''specifies how the response will be returned to user'''
    contenttype = user_input.content_type() #collects input from user
    print('-\n-----------------------------------RESULTS---------------------------------------------------\n')
    print('\n---------status code-------------\n','\n', response.status_code)
    print('\n-----------url----------\n', '\n', response.url)
    if contenttype == 'application/json':
        print('\n----------headers-------------\n','\n', response.headers)
        print('\n-----------json----------\n', '\n', response.json())  

    elif contenttype == 'text/xml':
        response.headers['content-type'] = 'text/xml' #change content type in header to text/xml
        print('\n----------headers-------------\n','\n', response.headers)
        print('\n-----------text/xml----------\n', '\n', get_xml.text_xml(response.json()))  
    else:
        print('\n----------headers-------------\n','\n', response.headers)
        print('\n---------text---------------\n','\n', response.text)
