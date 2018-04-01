""" UUID generator module """
import uuid

def generate_uuid():
    """ Generate a random UUID size 16 """
    return str(uuid.uuid4())
