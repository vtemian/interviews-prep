"""
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid
round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid
and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example 1:
Input: ["5","2","C","D","+"]
Output: 30
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
Example 2:
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.
Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.
"""


class Solution:
    def calPoints(self, ops):
        if len(ops) < 2:
            if ops[0] in "CD+":
                return 0
            return int(ops[0])

        scores = []

        for operation in ops:
            if operation == "C":
                scores.pop()
            elif operation == "D":
                scores.append(2 * scores[-1])
            elif operation == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(operation))

        return sum(scores)


for test_input, expected_result in [
    #(["5","2","C","D","+"], 30),
    #(["5","-2","4","C","D","9","+","+"], 27),
    (["84","C","-87","D","D","15","C","-76","-28","-65","26","-49","+","+","-56","-82","+","+","-66","31"], -1427),
]:
    result = Solution().calPoints(test_input)
    print(result, result == expected_result)
