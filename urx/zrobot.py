"""
Python library to control an UR robot through its TCP/IP interface
DOC LINK
http://support.universal-robots.com/URRobot/RemoteAccess
"""


from urx.urrobot import URRobot

__author__ = "ZSJ"

class ZRobot(URRobot):

  def _format_move(self, command, tpose, acc, vel, radius=0, prefix="", wrt_tcp=False):
    tpose = [round(i, self.max_float_length) for i in tpose]
    tpose.append(acc)
    tpose.append(vel)
    tpose.append(radius)
    if wrt_tcp:
      return "{}(pose_trans(get_target_tcp_pose(),{}[{},{},{},{},{},{}]), a={}, v={}, r={})".format(command, prefix, *tpose)
    else:
      return "{}({}[{},{},{},{},{},{}], a={}, v={}, r={})".format(command, prefix, *tpose)

  def movex(self, command, tpose, acc=0.01, vel=0.01, wait=True, wrt_tcp=False, threshold=None):
    """
    Send a move command to the robot. since UR robotene have several methods this one
    sends whatever is defined in 'command' string
    """

    prog = self._format_move(command, tpose, acc, vel, prefix="p", wrt_tcp=wrt_tcp)
    self.send_program(prog)
    if wait & (~wrt_tcp):
      self._wait_for_move(tpose[:6], threshold=threshold)
      return self.getl()

  def movel(self, tpose, acc=0.01, vel=0.01, wait=True, wrt_tcp = False, threshold=None):
    """
    Send a movel command to the robot. See URScript documentation.
    """
    return self.movex("movel", tpose, acc=acc, vel=vel, wait=wait, wrt_tcp=wrt_tcp, threshold=threshold)

  def move_tcp(self, tpose, acc=0.01, vel=0.01):
    return self.movel(tpose, acc=acc, vel=vel, wait=False, wrt_tcp = True, threshold=None)

  def set_pose(self, tpose, acc=0.01, vel=0.01):
    return self.movel(tpose, acc=acc, vel=vel, wait=False, wrt_tcp = False, threshold=None)


