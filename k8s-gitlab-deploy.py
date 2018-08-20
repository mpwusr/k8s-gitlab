# List deployments for a project:

deployments = project.deployments.list()
# Get a single deployment:

deployment = project.deployments.get(deployment_id)

# List the deploy keys:

keys = gl.deploykeys.list()
