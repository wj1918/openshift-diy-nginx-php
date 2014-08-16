Python 2.7 + Nginx + uWSGI on OpenShift
=========================================

Simple DIY cartridge to add Python 2.7, Nginx and uWSGI support on OpenShift.

Setting up Openshift
--------------------

    $ rhc app create <appname> diy-0.1
    $ cd <appname>
    $ git remote add upstream -m master git://github.com/skozlovf/openshift-diy-nginx-uwsgi.git
    $ git pull -s recursive -X theirs upstream master
    $ git push


Repo layout
-------------------

    misc/openshift/ - OpenShift related scripts & configs.
    misc/templates/ - Configuration templates.
    wsgi/           - WSGI application directory.


Application
-----------

Default template uses simple WSGI HTTP server and provides simple HTML
with application's environment variables.

To install additional packages just edit `requirements.txt`.

Additional deploy actions may be performed in the
`.openshift/action_hooks/post_deploy` script.


Notes
-----

If you experience problems with downloading (or building) tools on first
push or want to use different versions of them then you may want to update
URLs of the tools in the `.openshift/action_hooks/build` or versions
in the `misc/openshift/config`.

To simulate openshift enviornment.
export OPENSHIFT_REPO_DIR=$HOME/projects/openshift-diy-nginx-uwsgi
export OPENSHIFT_DIY_DIR=$HOME/projects/DUMMY_OPENSHIFT_DIY/
export OPENSHIFT_TMP_DIR=/tmp/
export OPENSHIFT_LOG_DIR=/tmp/log/
export OPENSHIFT_DIY_IP=127.0.0.1
export OPENSHIFT_DIY_PORT=8080

