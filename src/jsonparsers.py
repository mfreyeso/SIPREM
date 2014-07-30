#This is the interface json for SIPREM! Good Luck!
import json

class MyDecoder(json.JSONDecoder):
    
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            print 'MODULE:', module
            class_ = getattr(module, class_name)
            print 'CLASS:', class_
            args = dict( (key.encode('ascii'), value) for key, value in d.items())
            print 'INSTANCE ARGS:', args
            inst = class_(**args)
        else:
            inst = d
        return inst

class MyEncoder(json.JSONEncoder):
    
    def default(self, obj):
        #print 'default(', repr(obj), ')'
        # Convert objects to a dictionary of their representation
        """d = { '__class__':obj.__class__.__name__, 
              '__module__':obj.__module__,
              }"""
        d={}
        d.update(obj.__dict__)
        return d