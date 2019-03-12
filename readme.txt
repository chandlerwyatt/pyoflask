Initial Setup & Config:

1. Install git:
		Linux: sudo apt-get install git
		macOS: brew install git
2. Clone this repo:
		git clone <uri_of_git_file>
3. cd into the cloned directory
4. Install virtualenv:
		pip3 install virtualenv
5. Create your venv:
		virtualenv env
6. Activate your venv:
		source env/bin/activate
7. Install flask:
		pip install flask
8. export FLASK_APP env var:
		export FLASK_APP=server.py
9. Make sure pyo is installed and works in your venv by importing in repl and starting a Server()
10. Install Celery:
		pip install celery
11. Install RabbitMQ server:
		Linux: sudo apt-get install rabbitmq-server
		macOS: brew install rabbitmq
12. Start the RabbitMQ server:
		Linux: sudo systemctl start rabbitmq-server
		macOS: brew services start rabbitmq
13. Make sure it's running:
		sudo rabbitmqctl status
	a. If you get an error that the command does not exist, run the following, all on one line: 
		if [ ! -d /usr/local/sbin ]; then sudo mkdir /usr/local/sbin; fi && sudo chmod 777 /usr/local/sbin; brew link rabbitmq; sudo chmod 775 /usr/local/sbin
	b. After that, try running the rabbitmqctl status command again
14. Take note of the node name in the output of step 13
15. Add RabbitMQ user:
		sudo rabbitmqctl add_user flask flask
16. Add RabbitMQ vHost:
		sudo rabbitmqctl add_vhost flask_vhost
17. Set RabbitMQ permissions:
		sudo rabbitmqctl set_permissions -p flask_vhost flask ".*" ".*" ".*"
18. Install screen:
		Linux: sudo apt-get install screen
		macOS: sudo chmod 777 /usr/local/sbin; brew install screen; sudo chmod 775 /usr/local/sbin
19. Create, then modify config.json in the following ways:
	a. Add entry for 'celery_broker' with value:
		"amqp://flask:flask@localhost:5672/flask_vhost"
	b. Add entry for 'wav_file' with the value: "<name_of_existing_wav_file>.wav"
20. Create a screen for flask server:
		screen -S flask
21. Start flask server:
		flask run --host=0.0.0.0
22. Detach from the screen:
		keystroke: <CTRL>+A, D
23. Create screen for celery worker:
		screen -S celery
24. Start celery worker:
		celery -A server.celery worker
25. Detach from celery screen:
		keystroke: <CTRL>+A, D
26. Get your computer's IP address:
		ifconfig
27. On the RPi, go edit temp_read_post.py and set the 'ip' var to that IP address (as string)
28. Run temp_read_post.py on the Pi
29. Manipulate the temp sensor to modify parameter values and make cray ish like woah


Doc improvements needed:
- How to ascertain sensor 'id' value and get sensor working under w1/devices
- More in-depth guidance for pyo installation
- Better macOS instructions