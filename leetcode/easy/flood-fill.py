class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def flood(image, current_color, new_color, position):
            x, y = position

            image[x][y] = new_color

            if x + 1 < len(image) and image[x + 1][y] == current_color:
                flood(image, current_color, new_color, (x + 1, y))

            if x - 1 > -1 and image[x - 1][y] == current_color:
                flood(image, current_color, new_color, (x - 1, y))

            if y + 1 < len(image[0]) and image[x][y + 1] == current_color:
                flood(image, current_color, new_color, (x, y + 1))

            if y - 1 > -1 and image[x][y - 1] == current_color:
                flood(image, current_color, new_color, (x, y - 1))

        color = image[sr][sc]
        if color == newColor:
            return image

        flood(image, color, newColor, (sr, sc))

        return image
