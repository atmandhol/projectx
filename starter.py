# Import Service modules
from scheduler.scheduler import app as scheduler
from worker.worker import app as worker
from taskmanager.taskmanager import app as taskmanager
from ui.router import app as uirouter
