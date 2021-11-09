from uuid import uuid4
import os

def paragraph(content):
    content = content.replace('\r', '')
    paragraphs = content.split('\n')
    return paragraphs
    
def path_and_rename(instance, filename):
    """
    Rename the image from news and return the path.
    """
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)