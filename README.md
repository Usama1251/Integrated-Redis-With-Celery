# Integrated Redis With Celery
 In this project, we will integrate redis with celery and integrated postgresSql.

To start a celery server open another cmd/powershell
Celery -A project worker -l INFO                ####for starting the celery server on process

or place this code to start a celery server  on threads
celery -A project worker -l INFO --pool=threads