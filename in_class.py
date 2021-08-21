def gen_successors(node):
    ret = []
    current_state = node[0]
    current_ans = node[1]
    for i in range(len(current_state) - 1):
        for j in range(i + 1, len(current_state)):
            # สร้าง i,j => 01 02 03 12 13 23
            op1 = current_state[i]
            op2 = current_state[j]
            remaining_operands = current_state[:i] + current_state[i + 1:j] + current_state[
                                                                              j + 1:]  # ตัดตัวที่ i กับ j ออกจาก list
            ret.append((remaining_operands + [op1 + op2], current_ans + [str(op1) + '+' + str(op2)]))
    return ret


def is_goal(node):
    current_state = node[0]
    return current_state == [24]


def insert_all(node, fringe):
    children = gen_successors(node)
    for child in children:
        fringe.append(child)


def show_result(g):
    print(g)


def bfs(start_node):
    fringe = [start_node]
    while True:
        if len(fringe) == 0:
            print('Not Found')
            break
        front = fringe.pop(0)
        if is_goal(front):
            show_result(front)
            return True
        insert_all(front, fringe)


start_state = [5, 8, 2, 3]
start_node = (start_state, [])
# bfs(start_node)
gen_successors(start_node)

# https://youtu.be/sg24Rjd1cwk