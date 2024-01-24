Project 0x1A. Application Server Tasks

This repository contains solutions and configurations for the Application Server project, aimed at deploying and serving different versions of the AirBnB clone. The tasks involve setting up development and production environments, configuring Gunicorn, Nginx, and handling dynamic content. Each task focuses on a specific aspect of the application deployment process.

Task 0: Set up development with Python
This task involves serving the AirBnB clone v2 - Web framework on web-01. The development environment is set up to test and debug the code before deploying it to production. The Flask application is configured to serve its content from the route /airbnb-onepage/ on port 5000.

Task 1: Set up production with Gunicorn
In this task, the production application server is configured using Gunicorn on web-01, port 5000. Gunicorn and required libraries are installed, and the Flask application object (app) is used as the WSGI entry point. The same content from the previous task is served on the same route.

Task 2: Serve a page with Nginx
This task builds upon the previous tasks, configuring Nginx to serve the page from the route /airbnb-onepage/. Nginx proxies requests to the Gunicorn process listening on port 5000. The Nginx config file is included as 2-app_server-nginx_config.

Task 3: Add a route with query parameters
Expanding the web application, this task adds a new service for Gunicorn to handle. Nginx is configured to proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The Nginx config file is included as 3-app_server-nginx_config.

Task 4: Serve your AirBnB clone
This task involves serving the AirBnB clone - Web dynamic on web-01. Gunicorn serves content from web_dynamic/2-hbnb.py on port 5003, and Nginx is configured to route requests to the Gunicorn instance. The Nginx config file is included as 5-app_server-nginx_config.

Task 5: Deploy it!
For this advanced task, a systemd script (gunicorn.service) is provided to start a Gunicorn process serving the content from web_dynamic/2-hbnb.py. The Gunicorn process has 3 worker processes, logs errors in /tmp/airbnb-error.log, and logs access in /tmp/airbnb-access.log.

Task 6: No service interruption
In this advanced task, a Bash script (4-reload_gunicorn_no_downtime) is provided to reload Gunicorn gracefully. The script initiates a progressive rollout of the update without causing downtime.
