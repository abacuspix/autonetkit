def mixed():
    """Returns anm with input and physical as house graph"""
    from networkx.readwrite import json_graph
    import networkx as nx
    import autonetkit
    # returns a house graph
    data = {'directed': False,
    'graph': [],
    'links': [
    {'_ports': {'r1': 3, 'r3': 1},
    'raw_interfaces': {},
    'source': 0,
    'target': 3},
    {'_ports': {'r2': 3, 's1': 2},
    'raw_interfaces': {},
    'source': 1,
    'target': 4},
    {'_ports': {'sw1': 1, 'r1': 1},
    'raw_interfaces': {},
    'source': 2,
    'target': 3},
    {'_ports': {'sw1': 2, 'r2': 1},
    'raw_interfaces': {},
    'source': 2,
    'target': 4},
    {'_ports': {'r1': 2, 'r2': 2},
    'raw_interfaces': {},
    'source': 3,
    'target': 4}],
    'multigraph': False,
    'nodes': [{'_ports': {0: {'category': 'physical', 'description': None},
    1: {'category': 'physical', 'description': 'r3 to r1', 'id': 'eth0'},
    2: {'category': 'physical', 'description': 'r3 to s1', 'id': 'eth1'}},
    'asn': 1,
    'device_type': 'router',
    'id': 'r3',
    'label': 'r3',
    'x': 675,
    'y': 300},
    {'_ports': {0: {'category': 'physical', 'description': None},
    1: {'category': 'physical', 'description': 's1 to r3', 'id': 'eth0'},
    2: {'category': 'physical', 'description': 's1 to r2', 'id': 'eth1'}},
    'asn': 1,
    'device_type': 'server',
    'id': 's1',
    'label': 's1',
    'x': 675,
    'y': 500},
    {'_ports': {0: {'category': 'physical', 'description': None},
    1: {'category': 'physical', 'description': 'sw1 to r1', 'id': 'eth0'},
    2: {'category': 'physical', 'description': 'sw1 to r2', 'id': 'eth1'}},
    'asn': 1,
    'device_type': 'switch',
    'id': 'sw1',
    'label': 'sw1',
    'x': 350,
    'y': 400},
    {'_ports': {0: {'category': 'physical', 'description': None},
    1: {'category': 'physical', 'description': 'r1 to sw1', 'id': 'eth0'},
    2: {'category': 'physical', 'description': 'r1 to r2', 'id': 'eth1'},
    3: {'category': 'physical', 'description': 'r1 to r3', 'id': 'eth2'}},
    'asn': 1,
    'device_type': 'router',
    'id': 'r1',
    'label': 'r1',
    'x': 500,
    'y': 300},
    {'_ports': {0: {'category': 'physical', 'description': None},
    1: {'category': 'physical', 'description': 'r2 to sw1', 'id': 'eth0'},
    2: {'category': 'physical', 'description': 'r2 to r1', 'id': 'eth1'},
    3: {'category': 'physical', 'description': 'r2 to s1', 'id': 'eth2'}},
    'asn': 1,
    'device_type': 'router',
    'id': 'r2',
    'label': 'r2',
    'x': 500,
    'y': 500}]}
    graph = json_graph.node_link_graph(data)
    anm = autonetkit.anm.NetworkModel()
    g_in = anm.add_overlay("input")
    g_in._replace_graph(nx.Graph(graph))
    #TODO: check if should build overlays here rather than clone in?
    g_phy = anm["phy"]
    g_phy._replace_graph(graph)
    return anm