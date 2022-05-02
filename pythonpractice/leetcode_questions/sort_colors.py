import enum
colors = [2,0,2,1,1,0]

class Color(enum.Enum):
    red = 0
    white = 1
    blue = 2

class SortColors:
    def __init__(self, colors=None) -> None:
        if colors:
            self.colors = colors
        else:
            self.colors = []

    # things to note:
    # one pass to store in a dict
    # dictionary is ordered by default (by oreder of insertion)
    # problem with this solution is that it is not constant space
    def sort_colors(self):
        colors = self.colors
        sorted_colors = {"red": 0, "white": 0, "blue": 0}
        list_sorted_colors = []
        for color in colors: # O(n)
            sorted_colors[f"{Color(color).name}"] += 1
        for color in sorted_colors: # O(3)
            list_sorted_colors.extend([Color[color].value for num in range(0, sorted_colors[f"{color}"])])
        # or
        # for num in range(0, 3):
        #     color = Color(num).name
        #     num_of_times = sorted_colors[color] # this works because dict is ordered
        #     list_sorted_colors.extend([Color[color].value] * num_of_times)
        return list_sorted_colors

    def two_pointer_sort_colors(self):
        pass

    def insertion_sort_colors(self):
        """manually writing insertion sort algorithm for this solution since we cant use the library sort function"""
        pass

solution = SortColors(colors)
print(solution.sort_colors())
