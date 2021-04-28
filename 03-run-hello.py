# tutorial/03-run-hello.py
from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

# Obtain the workspace from the configuration
ws = Workspace.from_config()

# Launch the experiment against the workspace using a human readable name
experiment = Experiment(workspace=ws, name='day1-experiment-hello')

# Obtain the configuration and source for the experiment code, also, define the target for the execution of the experment
config = ScriptRunConfig(source_directory='./src', script='hello.py', compute_target='cpu-cluster')

# Submit the experiment based on the previous configuration
run = experiment.submit(config)

# Obtain and endpoint with the url provided by the run object to supervise the experimet execution
aml_url = run.get_portal_url()
print(aml_url)
