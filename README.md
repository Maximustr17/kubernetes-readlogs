Prerequisites:

	Install:
	
		Install minikube for windows, X86-64, stable, .exe download
		
		Run PowerShell as administrator comand to add the path to the env variables
			$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
			if ($oldPath.Split(';') -inotcontains 'C:\minikube'){ `
			  [Environment]::SetEnvironmentVariable('Path', $('{0};C:\minikube' -f $oldPath), [EnvironmentVariableTarget]::Machine) `
			}
			
		Start the cluster with command: minikube start
			Expected answer: "Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default"
	
	SetUp nginx:
	
		Run command: kubectl apply -f {LOCATION OF YAMEL FILE}nginx-deployment.yaml // This creates a new cluster with 3 instances of nginx the conf file can bee seen in the file.
		Run command "kubectl get deployments", to check if it got deployed correctly. 
			Expected answer: 
			NAME               READY   UP-TO-DATE   AVAILABLE   AGE
			nginx-deployment   3/3     3            3           39s
			
Script:

	The first step was to look for how to interact with kubernetes from python, I found there is a clint: https://github.com/kubernetes-client/python
	Then I started reading the documentation about the client, I found that the way to get the logs of the PODs is, using the method: read_namespaced_pod_log, but the name of the PODs are made on the fly, so I had to look how to get the name of the pods, I founf getting it from the call: list_namespaced_pod, and then checking the body to get the name of the pods, and from there I was able to use the method read_namespaced_pod_log.	
	After doing doing the script I noticed that the image used wasn't creating logs, so I looked for a simple example of an image of nginx that creates simple logs to read: https://hub.docker.com/r/kscarlett/nginx-log-generator/tags


And that's it, as easy as that!
