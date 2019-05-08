class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        current_point = [0, 0]
        axe = 1
        direction = 1

        stops = {
            0: {

            },
            1: {

            }
        }
        for obstacle in obstacles:
            if obstacle[0] not in stops[0]:
                stops[0][obstacle[0]] = []
            stops[0][obstacle[0]].append(obstacle[1])

            if obstacle[1] not in stops[1]:
                stops[1][obstacle[1]] = []
            stops[1][obstacle[1]].append(obstacle[0])

        for command in commands:
            if command == -2:
                if axe == 1 and direction == 1:
                    axe = 0
                    direction = -1
                elif axe == 0 and direction == -1:
                    axe = 1
                    direction = -1
                elif axe == 1 and direction == -1:
                    axe = 0
                    direction = 1
                elif axe == 0 and direction == 1:
                    axe = 1
                    direction = 1
            elif command == -1:
                if axe == 1 and direction == 1:
                    axe = 0
                    direction = 1
                elif axe == 0 and direction == 1:
                    axe = 1
                    direction = -1
                elif axe == 1 and direction == -1:
                    axe = 0
                    direction = -1
                elif axe == 0 and direction == -1:
                    axe = 1
                    direction = 1
            else:
                anti_axe = 1 if axe == 0 else 0
                next_position = current_point[axe] + command * direction

                if current_point[anti_axe] in stops[anti_axe]:
                    for stop in stops[anti_axe][current_point[anti_axe]]:
                        if stop > current_point[axe]:
                            if stop - 1 < 0 and next_position < 0:
                                next_position = max(stop + 1, next_position)
                            else:
                                next_position = min(stop - 1, next_position)

                current_point[axe] = next_position

        return current_point[0] ** 2 + current_point[1] ** 2
