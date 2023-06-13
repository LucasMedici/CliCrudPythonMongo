from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
  'secure_connect_bundle': './secure-connect-nome-do-meu-database.zip'
}
auth_provider = PlainTextAuthProvider('YzaQJPjLOyEptzOOZilHzDew', 'wDl.MpgL,5PGcyCh3AaH+HE_sbUCydje.ma2i678GSD7Yh3bt5Ljo2eerhc,r_R+_6GmJQkAoNZX6p8XpGu6J18MH6uYe6wpOgKDk5yb0+j1,2TDQuaTfEhZpOQPxrZB')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")