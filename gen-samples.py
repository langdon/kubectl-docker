#!/usr/bin/env python
#probably could do more stuff here, but this is a start

example_kube_config = """# See https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/kubeconfig-file.md for more details 
apiVersion: v1
clusters:
- cluster:
    api-version: v1beta1
    server: http://cow.org:8080
  name: cow-cluster
- cluster:
    certificate-authority: path/to/my/cafile
    server: https://horse.org:4443
  name: horse-cluster
- cluster:
    insecure-skip-tls-verify: true
    server: https://pig.org:443
  name: pig-cluster
contexts:
- context:
    cluster: horse-cluster
    namespace: chisel-ns
    user: green-user
  name: federal-context
- context:
    cluster: pig-cluster
    namespace: saw-ns
    user: black-user
  name: queen-anne-context
current-context: federal-context
kind: Config
preferences:
  colors: true
users:
- name: blue-user
  user:
    token: blue-token
- name: green-user
  user:
    username: admin
    password: secret
    client-certificate: path/to/my/client/cert
    client-key: path/to/my/client/key
"""

with open('./kubernetes-config.sample', 'w+') as kube_config:
    kube_config.write(example_kube_config)
