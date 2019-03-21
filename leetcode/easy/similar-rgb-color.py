class Solution:
    def similarRGB(self, color: 'str') -> 'str':
        def compose(component):
            q, r = divmod(int(component, 16), 17)
            if r > 8:
                q += 1
            return "{:02x}".format(q * 17)

        return '#' + compose(color[1:3]) + compose(color[3:5]) + compose(color[5:7])
