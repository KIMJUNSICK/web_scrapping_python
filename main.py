from indeed import get_indeed_jobs
from stack_over_flow import get_stack_over_flow_jobs

indeed = get_indeed_jobs()
stack0verFlow = get_stack_over_flow_jobs()

jobs = indeed + stack0verFlow
