Initial Setup & Config:

1. Install git:							sudo apt-get install git
2. Clone this repo:						git clone <uri_of_git_file>
3. cd into the cloned directory
4. Install virtualenv:					pip3 install virtualenv
5. Create your venv:					virtualenv env
6. Activate your venv:					source env/bin/activate
7. Install flask:						pip install flask
8. export FLASK_APP env var:			export FLASK_APP=server.py
9. Make sure pyo is installed and works in your venv by importing in repl and starting a Server()
10. Install Celery:						pip install celery
11. Install RabbitMQ server:			sudo apt-get install rabbitmq-server
12. Start the RabbitMQ server:			sudo systemctl start rabbitmq-server
13. Make sure it's running:				sudo rabbitmqctl status
14. Take note of the node name in the output of step 12
15. Add RabbitMQ user:					sudo rabbitmqctl add_user flask flask
16. Add RabbitMQ vHost:					sudo rabbitmqctl add_vhost flask_vhost
17. Set RabbitMQ permissions:			sudo rabbitmqctl set_permissions -p flask_vhost flask ".*" ".*" ".*"
18. Install screen:						sudo apt-get install screen
19. Create screen for celery worker:	screen -S celery
20. Start celery worker:				celery -A server.celery worker
21. Copy the value of "transport:" from the celery worker screen
22. Detach from celery screen:			keystroke: <CTRL>+A, D
23. Modify server.py in the following ways:
	a. Enter the string from step 21 on line 6 for 'CELERY_BROKER_URL' value
	b. Enter the name (string) of an existing wav file on line 34 as SfPlayer's first arg
24. Create a screen for flask server:	screen -S flask
25. Start flask server:					flask run --host=0.0.0.0
26. Detach from the screen:				keystroke: <CTRL>+A, D
27. Get your computer's IP address:		ifconfig
28. On the RPi, go edit temp_read_post.py and set the 'ip' var to that IP address (as string)
29. Run temp_read_post.py on the Pi
30. Manipulate the temp sensor to modify parameter values and make cray ish like woah


Doc improvements needed:
- How to ascertain sensor 'id' value and get sensor working under w1/devices
- More in-depth guidance for pyo installation