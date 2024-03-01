from dicttoxml import dicttoxml


def text_xml(data, code):
    '''changes default datatype pf the response to text/xml'''
    resp = (dicttoxml(data), code)
    return resp
