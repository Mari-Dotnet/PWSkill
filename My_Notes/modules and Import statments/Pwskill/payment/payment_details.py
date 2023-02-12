import os,sys
from os.path import dirname,abspath,join
sys.path.insert(0,abspath(join(dirname(__file__),'..')))
from Course import Course_details
def payment():
    print("This payament function")

Course_details.course()


