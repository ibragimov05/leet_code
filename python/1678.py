class Solution:
    def interpret(self, command: str) -> str:
        res = ""

        for i in range(len(command)):
            cnt += 1
            if command[i] == "G":
                res += command[i]
            elif command[i] == "(" and command[i + 1] == ")":
                res += "o"
            elif command[i] == "(" and command[i + 1] == "a":
                res += "al"

        return res


"""
Option 2:
with replace
command.replace("()", "o").replace("(al)", "o")
"""
