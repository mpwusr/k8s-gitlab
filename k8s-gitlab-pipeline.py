# List pipelines for a project:

pipelines = project.pipelines.list()
# Get a pipeline for a project:

pipeline = project.pipelines.get(pipeline_id)
# Create a pipeline for a particular reference:

pipeline = project.pipelines.create({'ref': 'master'})
# Retry the failed builds for a pipeline:

pipeline.retry()
# Cancel builds in a pipeline:

pipeline.cancel()
