class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        indexed_paths = {}

        for path in paths:
            directory, *files = path.split()

            for file in files:
                filename, content = file.split("(")

                if content not in indexed_paths:
                    indexed_paths[content] = []

                indexed_paths[content].append("{}/{}".format(directory, filename))

        return [
            value for value in indexed_paths.values()
            if len(value) > 1
        ]
