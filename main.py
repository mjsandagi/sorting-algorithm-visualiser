import pygame
import random
import math
pygame.init()

# Class to manage drawing and visualisation settings
class DrawInformation:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ALICEBLUE = (240, 248, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BACKGROUND_COLOUR = BLACK
    FONT_COLOUR = GREEN
    GREYS = [
        GREY,
        (160, 160, 160),
        (192, 192, 192)
    ]
    FONT = pygame.font.SysFont("Cascadia Code", 18)
    LARGE_FONT = pygame.font.SysFont("Cascadia Code", 40)
    SIDE_PAD = 100
    TOP_PAD = 150
    def __init__(self, width, height, lst) -> None:
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualiser")
        self.set_list(lst)
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


# Function to draw the interface
def draw(draw_info, algorithm_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOUR)
    title = draw_info.LARGE_FONT.render(f"{algorithm_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.FONT_COLOUR)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))
    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.FONT_COLOUR)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 50))
    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | M - Merge Sort | Q - Quick Sort | O - Bogo Sort", 1, draw_info.FONT_COLOUR)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 75))
    draw_list(draw_info)
    pygame.display.update()


# Function to draw the list as vertical bars
def draw_list(draw_info, colour_positions={}, clear_background=False):
    lst = draw_info.lst
    if clear_background:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOUR, clear_rect)
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        colour = draw_info.GREYS[i % 3]
        if i in colour_positions:
            colour = colour_positions[i]
        pygame.draw.rect(draw_info.window, colour, (x, y, draw_info.block_width, draw_info.height))
    if clear_background:
        pygame.display.update()


# Function to generate a random list of integers
def generate_starting_list(n, min_val, max_val):
    lst = [random.randint(min_val, max_val) for _ in range(n)]
    return lst


# Bubble sort implementation
def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True
    return lst


# Insertion sort implementation
def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending
            if not ascending_sort and not descending_sort:
                break
            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i: draw_info.RED, i - 1: draw_info.GREEN}, True)
            yield True
    return lst

# Merge sort implementation
def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    def merge(start, mid, end):
        left = lst[start:mid + 1]
        right = lst[mid + 1:end + 1]

        i = j = 0
        for k in range(start, end + 1):
            if i < len(left) and (j >= len(right) or (left[i] <= right[j] if ascending else left[i] >= right[j])):
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            draw_list(draw_info, {k: draw_info.GREEN}, True)
            yield True
    def divide(start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        yield from divide(start, mid)
        yield from divide(mid + 1, end)
        yield from merge(start, mid, end)
    yield from divide(0, len(lst) - 1)
    return lst

# Quick sort implementation
def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    def partition(start, end):
        pivot = lst[end]
        i = start - 1
        for j in range(start, end):
            if (lst[j] <= pivot if ascending else lst[j] >= pivot):
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                draw_list(draw_info, {i: draw_info.RED, j: draw_info.GREEN}, True)
                yield True
        lst[i + 1], lst[end] = lst[end], lst[i + 1]
        draw_list(draw_info, {i + 1: draw_info.RED, end: draw_info.GREEN}, True)
        yield True
        return i + 1
    def quick_sort_helper(start, end):
        if start >= end:
            return
        pivot_index = yield from partition(start, end)
        yield from quick_sort_helper(start, pivot_index - 1)
        yield from quick_sort_helper(pivot_index + 1, end)
    yield from quick_sort_helper(0, len(lst) - 1)
    return lst


# Bogo sort implementation
def bogo_sort(draw_info, ascending=True):
    lst = draw_info.lst
    def is_sorted():
        for i in range(len(lst) - 1):
            if (lst[i] > lst[i + 1] if ascending else lst[i] < lst[i + 1]):
                return False
        return True
    while not is_sorted():
        random.shuffle(lst)
        draw_list(draw_info, {}, True)
        yield True
    return lst

# Main function to handle the event loop and user interaction
def main():
    run = True
    clock = pygame.time.Clock()

    n = 150
    min_val = 0
    max_val = 300
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1600, 600, lst)

    sorting = False
    ascending = True
    sorting_algorithm = bubble_sort
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(200)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algorithm_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False

            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algorithm_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algorithm_name = "Bubble Sort"
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort
                sorting_algorithm_name = "Quick Sort"
            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = merge_sort
                sorting_algorithm_name = "Merge Sort"
            elif event.key == pygame.K_o and not sorting:
                sorting_algorithm = bogo_sort
                sorting_algorithm_name = "Bogo Sort"
    pygame.quit()


# Run the main function
if __name__ == "__main__":
    main()
