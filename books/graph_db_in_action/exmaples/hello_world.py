
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


if __name__ == "__main__":

    conn = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')
    g = traversal().withRemote(conn)

    # add some data - be sure to use a terminating step like iterate() so that the traversal
    # "executes". iterate() does not return any data and is used to just generate side-effects
    # (i.e. write data to the database)
    g.add_v('person').property('name', 'marko').as_('m'). \
        add_v('person').property('name', 'vadas').as_('v'). \
        add_e('knows').from_('m').to('v').iterate()

    # retrieve the data from the "marko" vertex
    print("marko: " + str(g.V().has('person', 'name', 'marko').value_map().next()))

    # find the "marko" vertex and then traverse to the people he "knows" and return their data
    print("who marko knows: " + str(g.V().has('person', 'name', 'marko').out('knows').value_map().next()))


    conn.close()

