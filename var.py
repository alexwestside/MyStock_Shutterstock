

from __future__ import print_function
import fileinput
import readline
import re
import datetime

MONTH = {'01':'January', '02':'February', '03':'March', '4':'April', '5':'May', '6':'June',
         '07':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}
WEEKDAY = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',4:'Fraiday', 5:'Saturday', 6:'Sunday'}

type_dict = {'Subscription': '25_a_day', 'Enhanced': 'enhanced', 'On Demand': 'on_demand', 'Videos': 'video_all', 'Single & other': 'single_image_and_other'}
type_list = ['Subscription', 'Enhanced', 'On Demand', 'Videos', 'Single & other']