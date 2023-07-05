import matplotlib.pyplot as plt


def onclick(event):
    if not plt.get_current_fig_manager().toolbar.mode:
        x = int(event.xdata)
        y = int(event.ydata)
        with open('output.txt', 'a') as file:
            file.write(f'({x}, {y})\n')


def main():
    with open('input.txt', 'r') as file:
        nums = [int(num) for num in file.readlines()]

    plt.plot(nums)
    plt.title('cardiogram')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.gcf().canvas.mpl_connect('button_press_event', onclick)

    plt.show()


if __name__ == '__main__':
    main()
