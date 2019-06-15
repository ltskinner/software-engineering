
"""
https://realpython.com/factory-method-python/

Design patterns are core solutions to recurring problems in software
and classifies each pattern into categories according to the nature of
the problem.
Each pattern is given a name, a problem description, a design solution,
and an explanation of the consequences of using it.

The Factory Method is a creational design pattern
Creational design patterns are related to the creation of objects, and
the Factory Method is a design pattern that creates objects with 
a common interface.

This is a recurrent problem that makes Factory Method one of the most
widely used design patterns
"""

"""
FM is used to create concrete implementations of a common interface.
It separates the process of creating an object from the code that
depends on the interface of the object

For example, an application requires and object with a specific
interface to perform its tasks. The concrete implmentation of the
interface is identified by some parameter.
Instead of using a complex if/else tree to determine the concrete 
implementation, the application delegates that decision to a separate
component that creates the concrete object. With this approach, the
code is simplified, making it more reusable and easier to maintain.
"""

"""Example 1: Serializing a Song into a String"""

import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    """Here, serialize supports two different formats JSON AND XML
    Also notice that there are 3 different execution paths from the 
    if/else tree, which seems manageable but can get out of hand
    """
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist':song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)

"""
Problems With Complex Conditional Code
Complex logical code uses if/else trees to change behavior of an
application.
    - The changing of BEHAVIOR is the issue
Using if/else conditional structures make the code harder to read, 
understand and maintain.

The code above is hard to maintain because it is doing too much.

Per the Single Responsibility Principle:
    a module, class, or even a method should have a single well-defined
    responsibility.

The situations causing issues with .serialize() are:
    1) When a new format is introduced: The method will have to change
        to implement the serialization in that format
    2) When the Song object changes: Adding or removing properties to
        the Song class will require the implementation to change in 
        order to accomodate the new structure
    3) When the string representation for a format changes:
        (JSON vs JSON API) The .serialize() method will have to change
        if the desired string representation for a format changes
        because the representation is hard coded in the .serialize()
        method implementation

The ideal situation would be if any of those changes in requirements
could be implmented eithoug changeing the .serialize() method
"""

"""
Looking for a Common Interface
The first step when you see complex conditional code in an application
is to identify the common goal of each of the execution paths.
Code that uses if/else usually has a common goal that is implemented
in different ways in each logical path. The code above converts a Song
object into its string representation using a different format in each
logical path.

Based on the goal, you look for a common interface that can be used to
replace each of the paths. The example above requires an interface
that takes a song object and returns a string.

Once found the common interface, provide separate implementations for
each logical path
"""

"""Refactored Example 1"""

class SongSerializer2:
    def serialize(self, song, format):
        if format == "JSON":
            return self._serialize_to_json(song)
        elif format == "XML":
            return self._serialize_to_xml(song)
        else:
            raise ValueError(format)
    
    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')


"""
This code above is easier to read, but can still be improved with
a basic implementation of Factory Method
"""

"""
Basic Implementation of Factory Method
The central idea in Factory Method is to provide a separate component
with the responsibility to decide which concrete imlementation 
should bbe used based on some specified parameter. That parameter
in our example is the format.

To complete implementation of Factory Method, add a new method
._get_serializer() that takes the format
"""

class SongSerializer3:
    # Also, despite self not being used here, still kept as class
    # Do not want to change all dependancies in other parts of code
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)

# Notice, this returns a function, that gets assigned to
# serializer above
# Also note, none of these methods use self
# sooo can send to functions
def get_serializer(format):
    if format == "JSON":
        return _serialize_to_json
    elif format == "XML":
        return _serialize_to_xml
    else:
        raise ValueError(format)

def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)

def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')


"""
When to Use:
    1) Replacing complex logical code
        Factory Method is good because you can put the body of each
        logical path into separate functions or classes with a common
        interface and the creator can provice concrete implementation

    2) Constructing related objects from external data
        Employee Class
            Manager
            Office Clerk
            Sales Associate
            etc
    
    3) Supporting multiple implementations of the same feature
        An image processing application needs to transform a satellite
        image from one corrdinate system to another, but there are
        multiple algorithms with different levels of accuracy
        to perform the transformation

        The application can allow the user to select an option that
        identifies the concrete algorithm. The Factory Method can 
        provide the concrete implementation of the algorith based on
        the option

    4) Combining similar features under a common interface
        Following the image processing example, an application needs to
        apply a filter to an image. The specific filter to use can be
        identified by some user input, and Factory Method can provide
        the concrete filter implementation

    5) Integrated related external services
        A music player application wants to integrate with multiple
        external services and allow users to select where their music
        comes from. The application can define a common interface for a
        music service and use Factory Method to create correct
        integrations based on user preference.

All these situations are similar. They all define a client that depends 
on a common interface known as the product. They all provide a means to
identify the concrete implementation of the product, so they all
can use the Factory Method in their design.
"""



