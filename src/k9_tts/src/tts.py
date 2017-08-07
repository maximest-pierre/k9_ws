#!/usr/bin/env python

# Import festival speech engine
import festival

import os

# Import ROS Stuff
import rospy
from std_msgs.msg import String
from k9_tts.msg import TTS
from k9_tts.srv import Say

class k9_tts:
    def __init__(self):
        rospy.init_node("k9_tts")
        service = rospy.Service('k9_say',Say , self.k9_tts_service)

    def k9_tts_service(self, req):
        os.system("echo {0} | festival --tts".format(req.speech.text))
        return True

if __name__ == "__main__":
    try:
        k9_tts()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
