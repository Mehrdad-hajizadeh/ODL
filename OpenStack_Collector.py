import requests  # library should be installed
from requests.auth import HTTPBasicAuth
import json
from os import environ as env
from openstack import connection
from neutronclient.v2_0 import client

from keystoneauth1 import identity
# Neutron Authentication
from os import environ as env
import keystoneclient.v2_0.client as ksclient
from neutronclient.v2_0 import client as neutronclient
#from keystoneclient.v3 import client
from neutronclient.v2_0 import client
from keystoneauth1.identity import v3
from keystoneauth1 import session

auth = v3.Password(auth_url="http://10.10.0.21:5000/v3", username="admin",
                  user_domain_name="tuc",
                  password="tuckn2020",
                  project_name="admin",
                  project_domain_name="TUC"

                 )
sess = session.Session(auth=auth)
neutron = client.Client(session=sess)
netw = neutron.list_ports()
print(netw)

#print(keystone.get_token(session=sess))
#neutron=neutronclient.client(endpoint_url='http://10.10.0.21:8774/v2.1/servers',token=token)


#'''

