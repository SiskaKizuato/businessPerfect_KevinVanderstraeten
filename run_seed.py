import django
django.setup()

from app.seed import run

if __name__== '__main__':
    run()
