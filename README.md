# boekkooi/openshift-nginx-php
This is a sample repository to get nginx + php fpm running on openshift.

More information about openshift: https://openshift.redhat.com/

## What's inside

**The `.openshift/action_hooks` scripts:**

* build:
    - Build the versions of nginx, php and nodejs that are needed
* build_*
    - The functions used for checking the versions and installing
* deploy
    - This will render copy the nginx and php conf files
    - Copy the .bash_profile if there is none
* common
    - A common include script for the action hooks (just setting some path's)
* start
    - Starts Nginx and php-fpm
* stop
    - Stops Nginx and php-fpm

**The `.openshift/tmpl` templates:**

Here are the templates used by the build and deploy scripts.
Just customize away.

**The `web/` nginx web folder:**

The web folder currently used. You can change this in `.openshift/tmpl/nginx.conf.tmpl`.

## Usage

To get PHP 5.5 working at OpenShift, you have to do the following:

1. Create a new Openshift "Do-It-Yourself" application
2. Clone this repository
3. Add a new remote "openshift" (You can find the URL to your git repository
   on the Openshift application page)
4. Run `git push --force "openshift" master:master`
5. SSH into your gear
7. Wait for build to finish (This may take at least an hour)
8. Open http://appname-namespace.rhcloud.com/ to verify

## Other

When using the action hooks within you own project by copy-paste method don't forget todo `git update-index --chmod=+x -- $(git ls-files .openshift/action_hooks/*)`.

Currently [nodejs](http://nodejs.org/) will only be build when the version is not the same a the one installed by default, it will just create a proxy for npm so it can be used with less problems.

## Known issues

#### PHP 5.4 won't build
To get PHP 5.4 to build open `.openshift/action_hooks/build_php` and remove `--enable-opcache`(line: 64).

#### Only index.php works in root dir
Currently the `.openshift/tmpl/nginx.conf.tmpl` configuration template for nginx only redirects to the `web/index.php` file.
You can change this by editing the template file. Also see http://wiki.nginx.org/Symfony for some extra information.

#### Openshift disconnects on build
This seems to be a problem within openshift (see https://www.openshift.com/forums/openshift/openshift-build-timeout).

To resume the build, first make an arbitary change to your local repo (e.g. add some text to README.md), commit that change and then do another `git push --force "openshift" master:master`. 
## Thanks

Thanks to the following people:

* [@sgoettschkes](https://github.com/Sgoettschkes)
* [@drejohnson](https://github.com/drejohnson)
* [@openshift](https://github.com/openshift/)
 
## Reading material

Some articles that mention how you can use this repo and other related articles:

* [[DIY] Nginx + PHP 5.4](https://www.openshift.com/forums/openshift/diy-nginx-php-54) origional forum post.
* [Nginx, PHP5.5 and Phalcon on OpenShift](http://www.sitepoint.com/nginx-php5-5-phalcon-openshift/) by [Bruno Skvorc](https://twitter.com/bitfalls) using a fork by [duythien](https://github.com/duythien).
* [How to Run Nginx PHP-FPM under OpenShift](https://www.openshift.com/blogs/how-to-run-nginx-php-fpm-under-openshift) a cartridge created by [Getup Cloud](http://getupcloud.com/index_en.html)
 
If you wrote a article about openshit and nginx+php please let me know so I can add it to the list.

## Todo's
This is stuff which needs to be done right now. Feel free to do a pull request!

* Test update functionality more thoroughly
* Test with Jenkins (http://jenkins-ci.org/) builds
* Get a [cup of coffee](https://www.gittip.com/Warnar%20Boekkooi/)

--------------------
Python 2.7 + Nginx + uWSGI on OpenShift

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
