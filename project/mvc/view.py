import matplotlib.pyplot as plt


class View:
    def __init__(self):
        pass

    def print_menu(self):
        print("Welcome to the main menu")
        print("1 - Print top 10 tags")
        print("2 - Print top 20 Locations (from texts)")
        print("3 - Print top 20 People (from texts)")
        print("4 - Print top 7 Locations (from titles)")
        print("5 - Print top 7 People (from titles)")
        print("6 - Print top 5 People (from texts of specific media)")
        print("7 - Print top 5 Locations (from texts of specific media)")
        print("8 - Print top 5 People (from titles of specific media)")
        print("9 - Print top 5 Locations (from titles of specific media)")
        print("10 - Show Polarity (from titles)")
        print("11 - Show Polarity (from texts)")
        print("12 - Print top 5 people of the day (from texts)")
        print("13 - Print top 5 location of the day (from texts)")
        print("0 - Exit")

    def show_bar_chart(self, data, labels, title, x_label, y_label):
        plt.xticks(range(len(data)), labels)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.bar(range(len(data)), data)
        plt.show()
