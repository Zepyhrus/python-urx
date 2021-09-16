import sys
sys.path.insert(0, ".")


import time
import numpy as np

def basic_test(robot_ip):

  import urx

  with urx.URRobot(robot_ip) as rob:
    rob.set_tcp((0, 0, 0, 0, 0, 0))
    rob.set_payload(0, (0, 0, 0))
    time.sleep(0.2)
    print("Current tool pose is: ",  rob.getl())

    while True:
      print("Current tool pose is: ",  rob.getl())
      rob.movel(rob.getl(), acc=1, vel=5, relative=False, wait=False)
      time.sleep(1)
      
      print("Current tool pose is: ",  rob.getl())
      rob.movel(rob.getl(), acc=1, vel=5, relative=False, wait=False)
      time.sleep(1)


def test_move_tcp(robot_ip):

  from urx.robot import Robot

  with Robot(robot_ip) as rob:
    rob.set_tcp((0, 0, 0.1, 0, 0, 0))
    while True:
      print("Current tool pose is: ",  rob.getl())
      rob.movel_tool((0, 0, 0.1, 0, 0, 0), acc=3, vel=5, wait=False)
      time.sleep(1)
      
      print("Current tool pose is: ",  rob.getl())
      rob.movel_tool((0, 0, -0.1, 0, 0, 0), acc=3, vel=5, wait=False)
      time.sleep(1)

      print("Current tool pose is: ",  rob.getl())
      rob.movel_tool((0, 0, 0, np.pi/6, 0, 0), acc=3, vel=5, wait=False)
      time.sleep(1)
      
      print("Current tool pose is: ",  rob.getl())
      rob.movel_tool((0, 0, 0, -np.pi/6, 0, 0), acc=3, vel=5, wait=False)
      time.sleep(1)

      print("Current tool pose is: ",  rob.getl())
      rob.movel_tool((0, 0, 0, 0, np.pi/6, 0), acc=3, vel=5, wait=False)
      time.sleep(1)
      
      print("Current tool pose is: ",  rob.getl())
      rob.movel_tool((0, 0, 0, 0, -np.pi/6, 0), acc=3, vel=5, wait=False)
      time.sleep(1)

def test_move_tcp_direct(robot_ip):

  from urx.zrobot import ZRobot

  with ZRobot(robot_ip) as rob:
    rob.set_tcp((0, 0, 0.1, 0, 0, 0))
    while True:
      print("Current tool pose is: ",  rob.getl())
      rob.move_tcp((0, 0, 0.1, 0, 0, 0), acc=3, vel=5)
      time.sleep(1)
      
      print("Current tool pose is: ",  rob.getl())
      rob.move_tcp((0, 0, -0.1, 0, 0, 0), acc=3, vel=5)
      time.sleep(1)

      print("Current tool pose is: ",  rob.getl())
      rob.move_tcp((0, 0, 0, np.pi/6, 0, 0), acc=3, vel=5)
      time.sleep(1)
      
      print("Current tool pose is: ",  rob.getl())
      rob.move_tcp((0, 0, 0, -np.pi/6, 0, 0), acc=3, vel=5)
      time.sleep(1)

      print("Current tool pose is: ",  rob.getl())
      rob.move_tcp((0, 0, 0, 0, np.pi/6, 0), acc=3, vel=5)
      time.sleep(1)
      
      print("Current tool pose is: ",  rob.getl())
      rob.move_tcp((0, 0, 0, 0, -np.pi/6, 0), acc=3, vel=5)
      time.sleep(1)
