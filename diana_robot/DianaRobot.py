from .DianaApi import *

class DianaRobot:
    def __init__(self, ip='192.168.1.10'):
        # Modify the port numbers according to your actual configuration
        self.ip = ip
        self.srv_net_st = [ip, 5001, 5002, 5003, 5004, 5005]
        initSrv(self.srv_net_st)
        releaseBrake(ip)

    def movej(self, joints, v=0.5, a=0.5):
        """Joint space motion"""
        return moveJToTarget(joints, v, a, ipAddress=self.ip)

    def movel(self, pose, v=0.2, a=0.2):
        """Cartesian space motion"""
        return moveLToPose(pose, v, a, ipAddress=self.ip)

    def freedriving(self, mode=freedriving_mode_e.E_NORMAL_FREEDRIVING):
        """Enable/disable freedriving mode"""
        return freeDriving(mode, ipAddress=self.ip)

    def enter_force_mode(self, frame_type, frame_matrix, force_direction, force_value, max_approach_velocity, max_allow_tcp_offset):
        """Enter force control mode"""
        return enterForceMode(frame_type, frame_matrix, force_direction, force_value, max_approach_velocity, max_allow_tcp_offset, ipAddress=self.ip)

    def leave_force_mode(self, mode=mode_e.T_MODE_POSITION):
        """Exit force control mode"""
        return leaveForceMode(mode, ipAddress=self.ip)

    def getjoints(self):
        """Get current joint angles"""
        joints = [0.0] * 7
        getJointPos(joints, ipAddress=self.ip)
        return joints

    def getpose(self):
        """Get current TCP pose"""
        pose = [0.0] * 6
        getTcpPos(pose, ipAddress=self.ip)
        return pose

    def stop(self):
        """Stop the robot"""
        return stop(ipAddress=self.ip)

    def close(self):
        """Release resources"""
        holdBrake(ipAddress=self.ip)
        destroySrv(ipAddress=self.ip)

# Example usage
if __name__ == '__main__':
    robot = DianaRobot(ip='192.168.1.10')
    print("Current joints:", robot.getjoints())
    print("Current TCP pose:", robot.getpose())
    robot.movej([0, -0.5, 0.5, 0, 0, 0, 0])
    robot.movel([0.3, 0.1, 0.2, 0, 3.14, 0])
    robot.stop()