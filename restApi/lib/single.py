""" Single Lib """

def single_all(event):
    """ Single - All """
    method = event.get('httpMethod', "?")
    msg = "Your Serverless function ran successfully via the '%s' method" % method
    return {
        "message": msg,
    }