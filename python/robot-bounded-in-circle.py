class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir, curr_pos = 0, (0, 0)
        
        for instruction in instructions:
            if instruction == "R":
                curr_dir = (curr_dir + 1) % 4
            elif instruction == "L":
                curr_dir = (curr_dir + 3) % 4
            else:
                curr_pos = (curr_pos[0]+dirs[curr_dir][0], curr_pos[1]+dirs[curr_dir][1])
        return curr_pos == (0, 0) or curr_dir != 0