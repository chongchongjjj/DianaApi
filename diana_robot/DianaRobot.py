from .DianaApi import *

class DianaRobot:
    def __init__(self, ip='192.168.1.10'):
        # 端口号请根据实际情况修改
        self.ip = ip
        self.srv_net_st = [ip, 5001, 5002, 5003, 5004, 5005]
        initSrv(self.srv_net_st)
        releaseBrake(ip)

    def movej(self, joints, v=0.5, a=0.5):
        """关节空间运动"""
        return moveJToTarget(joints, v, a, ipAddress=self.ip)

    def movel(self, pose, v=0.2, a=0.2):
        """笛卡尔空间运动"""
        return moveLToPose(pose, v, a, ipAddress=self.ip)

    def getjoints(self):
        """获取当前关节角度"""
        joints = [0.0] * 7
        getJointPos(joints, ipAddress=self.ip)
        return joints

    def getpose(self):
        """获取当前末端位姿"""
        pose = [0.0] * 6
        getTcpPos(pose, ipAddress=self.ip)
        return pose

    def stop(self):
        """停止机器人"""
        return stop(ipAddress=self.ip)

    def close(self):
        """释放资源"""
        holdBrake(ipAddress=self.ip)
        destroySrv(ipAddress=self.ip)

# 使用示例
if __name__ == '__main__':
    robot = DianaRobot(ip='192.168.1.10')
    print("当前关节:", robot.getjoints())
    print("当前末端:", robot.getpose())
    robot.movej([0, -0.5, 0.5, 0, 0, 0, 0])
    robot.movel([0.3, 0.1, 0.2, 0, 3.14, 0])
    robot.stop()
    robot.close()