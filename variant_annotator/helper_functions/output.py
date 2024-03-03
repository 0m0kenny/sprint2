from helper_functions import user_input, get_xml

def output(response):
    '''specifies how the vep response will be returned to user'''
    # Collect input from user
    contenttype = user_input.content_type()
    # Print messages
    print('-\n-----------------------------------RESULTS---------------------------------------------------\n')
    print('\n---------status code-------------\n','\n', response.status_code)
    print('\n-----------url----------\n', '\n', response.url)
    # Print other response attributes based on content type chosen by user
    if contenttype == 'application/json':
        print('\n----------headers-------------\n','\n', response.headers)
        print('\n-----------json----------\n', '\n', response.json())

    elif contenttype == 'text/xml':
        # Change the content type in header to text/xml
        response.headers['content-type'] = 'text/xml' 
        print('\n----------headers-------------\n','\n', response.headers)
        # Convert response to text/xml and print
        print('\n-----------text/xml----------\n', '\n', get_xml.text_xml(response.json()))
    
    else:
        # If user choses text
        print('\n----------headers-------------\n','\n', response.headers)
        print('\n---------text---------------\n','\n', response.text)
