def keyboard_layouts():
    return [
        ["abcdefghijklm", "nopqrstuvwxyz"],
        ["789", "456", "123", "0.-"],
        ["chunk", "vibex", "gymps", "fjord", "waltz"],
        ["bemix", "vozhd", "grypt", "clunk", "waqfs"],
    ]

def find_position(char, layout):
    for row_idx, row in enumerate(layout):
        if char in row:
            return row_idx, row.index(char)
    return None

def calculate_moves(start_pos, target_pos, layout):
    start_row, start_col = start_pos
    target_row, target_col = target_pos

    # Calculate horizontal move
    if start_row == target_row:
        move_right = (target_col - start_col) % len(layout[start_row])
        move_left = (start_col - target_col) % len(layout[start_row])
        horizontal_move = min(move_right, move_left)
        if horizontal_move == move_left:
            move_seq = ['lw' if move_left != 0 else '']  # 'w' does not count as a move
        else:
            move_seq = ['rw' if move_right != 0 else '']
    else:
        horizontal_move = 0
        move_seq = []

    # Calculate vertical move
    move_down = (target_row - start_row) % len(layout)
    move_up = (start_row - target_row) % len(layout)
    vertical_move = min(move_down, move_up)
    if vertical_move == move_up:
        move_seq += ['uw' if move_up != 0 else '']
    else:
        move_seq += ['dw' if move_down != 0 else '']

    return horizontal_move + vertical_move, move_seq

def plan_actions(string, layout):
    actions = []
    current_pos = (0, 0)  # Robbie starts at the top left
    total_moves = 0

    for char in string:
        target_pos = find_position(char, layout)
        if target_pos is None:
            return None  # Character not found on this layout
        moves, move_seq = calculate_moves(current_pos, target_pos, layout)
        actions.extend(move_seq)
        actions.append('p')
        total_moves += moves + 1  # +1 for pressing the key
        current_pos = target_pos

    return total_moves, actions

def choose_best_keyboard(string):
    layouts = keyboard_layouts()
    best_layout = None
    best_actions = []
    min_moves = float('inf')

    for idx, layout in enumerate(layouts):
        result = plan_actions(string, layout)
        if result:
            total_moves, actions = result
            if total_moves < min_moves:
                min_moves = total_moves
                best_layout = idx
                best_actions = actions

    return best_layout, best_actions

def main():
    user_input = input("Enter a string: ").strip().lower()

    best_layout, best_actions = choose_best_keyboard(user_input)

    if best_layout is None:
        print("The string cannot be typed on any of the available keyboards.")
    else:
        print(f"Best keyboard configuration: {best_layout}")
        print("Actions Robbie will take:")
        print(' '.join(best_actions))

if __name__ == "__main__":
    main()
