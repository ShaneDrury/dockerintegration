from collections import namedtuple

Container = namedtuple('Container', 'name, addresses')

Address = namedtuple('Address', 'ip, port')

InternalPort = namedtuple('InternalPort', 'port, transport')
