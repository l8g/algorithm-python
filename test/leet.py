
board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]


class Solution:

    def find_next(self, from_pos, end_pos, cmd):
        if from_pos[0] != end_pos[0]:
            if from_pos[0] < end_pos[0]:
                if from_pos[1] < len(board[from_pos[0] + 1]):
                    cmd += "D" + self.find_next((from_pos[0] + 1, from_pos[1]), end_pos, cmd)
                else:
                    cmd += "L" + self.find_next((from_pos[0], from_pos[1] - 1), end_pos, cmd)
            elif from_pos[0] > end_pos[0]:
                cmd += "U" + self.find_next((from_pos[0] - 1, from_pos[1]), end_pos, cmd)
        elif from_pos[1] != end_pos[1]:
            if from_pos[1] < end_pos[1]:
                cmd += "R" + self.find_next((from_pos[0], from_pos[1] + 1), end_pos, cmd)
            elif from_pos[1] > end_pos[1]:
                cmd += "L" + self.find_next((from_pos[0], from_pos[1] - 1), end_pos, cmd)
        else:
            cmd += "!"
        return cmd

    def find_letter(self, l):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] ==l:
                    return (i, j)

    def alphabetBoardPath(self, target: str) -> str:
        s = self.find_next((0, 0), self.find_letter(target[0]), "")
        for k in range(len(target) - 1):
            s += self.find_next(self.find_letter(target[k]), self.find_letter(target[k + 1]), "")

        return s


s = Solution()
print(s.alphabetBoardPath("zdz"))