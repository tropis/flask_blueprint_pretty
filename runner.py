# runner.py
"""
-- local run: 
source venv/bin/activate
python3 runner.py
  or 
flask --app blueapp --debug run

-- DO run:
gunicorn --worker-tmp-dir /dev/shm runner:gunicorn_app

"""

from blueapp import create_app

if __name__ == '__main__':

    fun = create_app()
    fun.run()

else:
    gunicorn_app = create_app()

