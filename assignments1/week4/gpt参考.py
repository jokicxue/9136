# 键盘布局
keyboard = [
    "abcdefghijklm",
    "nopqrstuvwxyz"
]


def get_position(char):
    """ 获取字符在键盘上的位置 """
    for i, row in enumerate(keyboard):
        if char in row:
            return (i, row.index(char))
    return None


def move_to(start, end):
    """ 从起始位置移动到目标位置的指令 """
    moves = []
    start_row, start_col = start
    end_row, end_col = end

    # 水平移动
    if start_col < end_col:
        moves.append('r' * (end_col - start_col))
    elif start_col > end_col:
        moves.append('l' * (start_col - end_col))

    # 垂直移动
    if start_row < end_row:
        moves.append('d' * (end_row - start_row))
    elif start_row > end_row:
        moves.append('u' * (start_row - end_row))

    return ''.join(moves)


def plan_actions(string):
    """ 规划 Robbie 的动作 """
    actions = []
    current_position = (0, 0)  # 从 'a' 开始

    for char in string:
        target_position = get_position(char)
        if target_position:
            actions.append(move_to(current_position, target_position))
            actions.append('p')
            current_position = target_position

    return ''.join(actions)


# 主程序
if __name__ == "__main__":
    user_input = input("请输入字符串：")
    actions = plan_actions(user_input)
    print(f"Robbie 的动作计划：{actions}")
