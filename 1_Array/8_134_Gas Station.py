# O(n2)
# 2856 ms, 14.6 MB
def canCompleteCircuit(gas, cost):
    '''
    depart_gas
    记录从不同出发地出发并到达下一个站点后, 汽车的油量
    全为正, 从任何站点出发都可回到原地
    有正有负, 从正数站点出发可能回到原地(需验证)
    全为负, 站点之间完全不可通行
    '''

    len_ = len(gas)

    depart_gas = [0] * len_
    
    for i in range(len_): 
        depart_gas[i] = gas[i] - cost[i]

    for i in range(len_):
        if depart_gas[i] >= 0:
            gas_residue = 0

            # 验证depart_gas大于0的出发点i
            for j in range(len_):
                flag = True     # 默认可回到原点
                gas_residue += depart_gas[(j+i) % len_]
                if gas_residue < 0:
                    flag = False
                    break
            
            if flag is True:
                return i

    return -1

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(canCompleteCircuit(gas, cost))
