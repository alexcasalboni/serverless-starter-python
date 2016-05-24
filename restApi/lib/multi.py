""" Multi Lib """

def multi_create(event):
    """ Multi - Create """
    return {
        "message": "Your Serverless function 'multi/create' ran successfully",
    }

def multi_show(event):
    """ Multi - Show """
    pid = event['pathId']
    msg = "Your Serverless function 'multi/show' ran successfully ith the following ID '%s'" % pid
    return {
        "message": msg,
    }