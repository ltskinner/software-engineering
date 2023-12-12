
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


if __name__ == "__main__":

    conn = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')
    g = traversal().withRemote(conn)

    # Remove any existing data to allow this to be rerun
    g.V().drop().iterate()

    # Adds a person vertex with a name of Dave and saves it to a variable
    dave = g.add_v('person').property('first_name', 'Dave')
    # Adds a person vertex with a name of Josh and saves it to a variable
    josh = g.add_v('person').property('first_name', 'Josh')
    # Adds a person vertex with a name of Ted and saves it to a variable
    ted = g.add_v('person').property('first_name', 'Ted')
    # Adds a person vertex with a name of Hank and saves it to a variable
    hank = g.add_v('person').property('first_name', 'Hank')

    # Adds a friends edge between Dave and Ted
    g.add_e('friends').from_(dave).to(ted).next()
    # Adds a friends edge between Dave and Josh
    g.add_e('friends').from_(dave).to(josh).next()
    # Adds a friends edge between Dave and Hank
    g.add_e('friends').from_(dave).to(hank).next()
    # Adds a friends edge between Josh and Hank
    g.add_e('friends').from_(josh).to(hank).next()
    # Adds a friends edge between Ted and Josh
    g.add_e('friends').from_(ted).to(josh).next()

    # Remove any existing data to allow this to be rerun
    g.V().drop().iterate()
