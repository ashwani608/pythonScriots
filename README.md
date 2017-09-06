# pythonScripts

https://www.tikalk.com/setup-git-and-gitweb-under-apache-ubuntu/

Once you have installed git (gitweb included) and apache, here is the simple setup you need to do:
 

 

for git:

 

    Create a git repository (under /var/git):

 

git init /var/git/myproject

 

    if you want to use this repository as your central repository, you will probably want to do it as:

git init --bare –shared /var/git/myproject 


   --bare option will create your repository without working copy and --shared option will set the permissions on everything in the repository to group-writable.

 

 

    git under Apache – put the following configuration in /etc/apache2/sites-available/default

 

<VirtualHost *:80>
  DocumentRoot /var/git

  <Directory "/var/git">
    Allow from All
    Options +ExecCGI
    AllowOverride All
  </Directory>

  SetEnv GIT_PROJECT_ROOT /var/git
  SetEnv GIT_HTTP_EXPORT_ALL
  ScriptAlias /git/ /usr/lib/git-core/git-http-backend/

</VirtualHost>

 

 

for gitweb:

 

    gitweb configuration: /etc/gitweb.conf

    # path to git projects (<project>.git)
    $projectroot = "/var/git";

    # directory to use for temp files
    $git_temp = "/tmp";

    # target of the home link on top of all pages
    #$home_link = $my_uri || "/";

    # html text to include at home page
    $home_text = "indextext.html";

    # file with project list; by default, simply scan the projectroot dir.
    $projects_list = $projectroot;

    # stylesheet to use
    $stylesheet = "/gitweb/gitweb.css";

    # logo to use
    $logo = "/gitweb/git-logo.png";

    # the 'favicon'
    $favicon = "/gitweb/git-favicon.png";


     

    gitweb under Apache - put the following configuration in /etc/apache2/conf.d/gitweb:

        Alias /gitweb /usr/share/gitweb

        <Directory /usr/share/gitweb>
           Options FollowSymLinks +ExecCGI
           AddHandler cgi-script .cgi
        </Directory>

 
Now restart apache:

service apache2 restart


 
and you are ready to go!
