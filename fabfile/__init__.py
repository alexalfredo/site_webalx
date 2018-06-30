from fabric.api import local
from fabric.colors import green, yellow, red
from fabric.decorators import task

@task
def setup():
    """ setup local folder and install requirements, if needed """
    env.project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print red("environment set to %(project_path)s @ localhost" % env)
    print yellow("creating local folders for static files")
    with cd(env.project_path):
        local("mkdir -p static")
        local("mkdir -p static/css")
        local("mkdir -p static/js")
        print green('static/[css|js] directories created')
        
@task
def deploy(email):
    """ deploy current code to appengine using the email address as auth """
    print red("about to deploy to Google App Engine...")
    local("appcfg.py --email=%s update ." % email)
    print green("deploy: done")

@task
def run():
	""" execute localsever using GAE dev_appserver """
	print yellow("going to run local server, watch out")
	local("dev_appserver.py .")
