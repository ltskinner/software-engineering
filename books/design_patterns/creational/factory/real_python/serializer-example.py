
"""https://realpython.com/factory-method-python/"""

import json
import yaml
import xml.etree.ElementTree as et

class JsonSerializer:
    def __init__(self):
        self._current_object = None # Notice init new vars with None
    
    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()

"""Wait this is kinda hype, the control switches 
go in a "Factory" class
"""
"""
# Original
class SerializerFactory:
    def get_serializer(self, format):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            raise ValueError(format)
"""

# Mega suped up version
class SerializerFactory:
    """This is so massive b/c existing code wont need to be modified"""
    def __init__(self):
        self._creators = {}
    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)


""" Then get this:"""
class YamlSerializer(JsonSerializer):
    """yaml and json similar interface, so can hot swap like this
    not sure why no super class needed...
    """
    def to_str(self):
        return yaml.dump(self._current_object)
