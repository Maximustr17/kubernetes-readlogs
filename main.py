from kubernetes.client.rest import ApiException
from kubernetes import client, config

config.load_kube_config()

name_space = 'default'
try:
    api_instance = client.CoreV1Api()

    api_response_pods = api_instance.list_namespaced_pod(name_space)
    for pod in api_response_pods.items:
        api_response_pods_logs = api_instance.read_namespaced_pod_log(pod.metadata.name, name_space)
        print(f'Logs for POD {pod.metadata.name} \n {api_response_pods_logs}')

except ApiException as e:
    print('Found exception in reading the logs')