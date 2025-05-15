import random
import math
import time

def get_nodes(initial_pos, time_limit):
    print(f"Starting MCTS simulation for position with turn {initial_pos.turn}")
    nodes = {}
    nodes[initial_pos] = (0.0, 0.0, {initial_pos: 0})
    start_time = time.time()
    leaf_count = 0
    while time.time() - start_time < time_limit:
        leaf_count += 1
        leaf_path = get_leaf(nodes, initial_pos)
        leaf = leaf_path[-1]
        
        if leaf not in nodes:
            nodes[leaf] = (0.0, 0.0, {leaf_path[-2] if len(leaf_path) > 1 else initial_pos: 0})
        
        _, ni, _ = nodes[leaf]
        
        if ni > 0 and not leaf.terminal:
            legal_moves = leaf.legal_moves()
            for loc in legal_moves:
                new_pos = leaf.move(loc)
                if new_pos not in nodes:
                    nodes[new_pos] = (0.0, 0.0, {leaf: 0})
            loc = random.choice(legal_moves)
            child_pos = leaf.move(loc)
            reward = 0
            num_runs = 10
            for _ in range(num_runs):
                reward += randomly_play(child_pos)
            w, n, parent_n_dict = nodes[child_pos]
            if leaf not in parent_n_dict:
                parent_n_dict[leaf] = 0
            parent_n_dict[leaf] += 1
            nodes[child_pos] = (w + reward, n + num_runs, parent_n_dict)
        else:
            reward = 0
            num_runs = 10
            for _ in range(num_runs):
                reward += randomly_play(leaf)
        
        parent = initial_pos
        for position in leaf_path:
            w, n, parent_n_dict = nodes[position]
            parent_n_dict[parent] += num_runs
            nodes[position] = (w + reward, n + num_runs, parent_n_dict)
            parent = position
    print(f"MCTS completed: processed {leaf_count} leaves")
    return nodes

def ucb2_agent(time_limit):
    def strat(pos):
        nodes = get_nodes(pos, time_limit)
        player = pos.turn
        best_score = float('-inf') if player == 0 else float('inf')
        next_best_move = None
        
        for loc in pos.legal_moves():
            next_pos = pos.move(loc)
            score = 0.0
            if next_pos in nodes:
                w, n, _ = nodes[next_pos]
                score = w / n if n > 0 else 0.0
            if (player == 1 and score < best_score) or (player == 0 and score > best_score):
                best_score = score
                next_best_move = loc
                print(f"Selected move {next_best_move} with score {best_score}")
        
        return next_best_move
    return strat

def randomly_play(pos):
    cur_pos = pos
    while not cur_pos.terminal:
        moves = cur_pos.legal_moves()
        loc = random.choice(moves)
        cur_pos = cur_pos.move(loc)
    return float(cur_pos.result)

def get_leaf(nodes, root):
    current_node = root
    path = []
    while True:
        w, ni, _ = nodes[current_node]
        path.append(current_node)
        if ni == 0:
            return path
        
        legal_moves = current_node.legal_moves()
        next_player = current_node.turn
        best_score = float('-inf') if next_player == 0 else float('inf')
        next_best_node = None
        best_loc = None
        
        for loc in legal_moves:
            result_position = current_node.move(loc)
            if result_position not in nodes:
                nodes[result_position] = (0.0, 0.0, {current_node: 0})
                path.append(result_position)
                return path
            temp_w, temp_ni, temp_parent_n_count = nodes[result_position]
            if current_node not in temp_parent_n_count:
                temp_parent_n_count[current_node] = 0
            if temp_parent_n_count[current_node] == 0:
                path.append(result_position)
                return path
            
            score = get_score(nodes[current_node][1], temp_parent_n_count[current_node], temp_w / temp_ni if temp_ni > 0 else 0.0, next_player)
            if (next_player == 1 and score < best_score) or (next_player == 0 and score > best_score):
                best_score = score
                next_best_node = result_position
                best_loc = loc
        
        current_node = next_best_node
        if current_node is None:
            return path
    return path

def get_score(N, ni, r, player, c=2.0):
    return r + math.sqrt(c * math.log(N) / ni) if player == 0 else r - math.sqrt(c * math.log(N) / ni)