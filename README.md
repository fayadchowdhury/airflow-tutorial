# airflow-tutorial

## What is Airflow?

Airbnb's workflow management tool/platform that was started at Aribnb in 2014, brought under the Apache incubator project in 2016 and then a top-leve Apache Foundation software project in 2019.

It manages complex workflows and is written in Python.

## What is workflow?

A sequence of tasks defined as a Directed Acyclic Graph (DAG).

A task is defined as a unit of work and is represented as a node in the workflow DAG. Tasks may have dependencies on other tasks, and the dependencies determine the order of execution of the tasks.

An operator is the method used by a task to achieve its goals. An operator can be a BashOperator, PythonOperator etc. It is even possible to write one's own operator.

Tasks have 11 statuses:

1. no_status - Scheduler creates an empty task instance
2. scheduled - Scheduler determined that the task instance needs to be run and is assigned to an executor
3. queued - Scheduler has sent task to executor to run on the queue; if the worker node is free, it will be assigned the task
4. running - A worker has picked up a task and is now running it
5. success - The task completed successfully
6. upstream_failed - The task's upstream task (the one it depends on) failed
7. up_for_reschedule - Reschedule the task to run after certain intervals
8. skipped - The task has been skipped
9. up_for_retry - If max retries has not been reached, retry the task
10. failed - The task failed to complete
11. shutdown - The task run has been shut down

## Basic Architecture

Apache Airflow's architecture consists of several key components:

1. **Scheduler**: The scheduler is responsible for adding the necessary tasks to the queue based on the scheduling intervals specified in the DAGs. It determines when a task should be executed.

2. **Executor**: The executor is the mechanism by which task instances get run. It can be configured to use different modes such as LocalExecutor, CeleryExecutor, or KubernetesExecutor, depending on the scale and requirements of the deployment.

3. **Worker**: Workers are the processes that execute the tasks. They pick up tasks from the queue and run them.

4. **Web Server**: The web server provides a user interface to inspect, trigger, and debug the DAGs and tasks. It is built using Flask and provides a rich UI for monitoring and managing workflows.

5. **Metadata Database**: The metadata database stores information about DAGs, task instances, variables, connections, and other configurations. It is typically a relational database like PostgreSQL or MySQL.

6. **DAGs**: Directed Acyclic Graphs (DAGs) are a collection of tasks with defined dependencies and execution order. They are written in Python and define the workflow.

7. **Plugins**: Airflow supports plugins to extend its functionality. Plugins can be used to add custom operators, sensors, hooks, and more.

These components work together to manage and execute workflows efficiently. A data engineer manages the configuration of the workflow and the environment (type of executor, metadata database in use etc.) from a config file or when the Airflow instance is spun up. The web server, scheduler, executor and workers are connected to the metadata database to push and pull data as required.
