import subprocess

# 执行第一个命令并将其放在后台执行
process1 = subprocess.Popen('第一个命令', shell=True)

# 执行第二个命令并将其放在后台执行
process2 = subprocess.Popen('第二个命令', shell=True)

# 执行第三个命令并等待其完成
subprocess.call('第三个命令', shell=True)

# 等待第一个和第二个命令结束
process1.wait()
process2.wait()
