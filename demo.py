#!/usr/bin/env python
import time
import subprocess

seedList = ['862', '9798', '6769', '7274', '5439', '9675', '2342', '373', '2590', '8304', '5909', '6874', '7955', '9272', '2801', '4309', '5077', '772', '3111', '8369', '926']
run_duration = 100 # seconds
cmd_prepare = "source /opt/ros/noetic/setup.sh && source /home/hello/workspace_qp/fael_ws/devel/setup.sh &&"
cmd0 = f"timeout {run_duration}s roslaunch exploration_manager sim_env.launch"
cmd1 = f"timeout {run_duration}s roslaunch exploration_manager robot_move.launch"
cmd2 = f"timeout {run_duration}s roslaunch exploration_manager explorer.launch"

for seed in seedList[:1]:
    print(f"\n\n##########\n\nStarting run {seed}\n\n")
    process1 = subprocess.Popen(cmd_prepare+cmd0, shell=True,executable="/bin/bash")
    time.sleep(10)
    process2 = subprocess.Popen(cmd_prepare+cmd1, shell=True,executable="/bin/bash")
    time.sleep(5)
    process3 = subprocess.Popen(cmd_prepare+cmd2, shell=True,executable="/bin/bash")
    process1.wait()
    process2.wait()
    process3.wait()
