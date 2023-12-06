import curses
import time

def show_credits(stdscr):
    # Set up curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(200)  # Increased timeout for slower scrolling

    # Define the credits with more information and separators
    credits = [
        "Developers:",
        "Md. Shaykhul Islam",
        "Algolizen",
        "",  # Empty line as separator
        "Authors:",
        "SHAYKHUL",
        ""
    ]

    # Get terminal size
    max_y, max_x = stdscr.getmaxyx()

    # Calculate starting position at the bottom center
    start_x = max_x // 2 - max(len(credit) for credit in credits) // 2
    start_y = max_y

    # Initialize colors if supported
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Main loop to display credits with slower scrolling
    while start_y >= -(len(credits) + 1):
        stdscr.clear()

        # Display credits with different colors
        for i, credit in enumerate(credits):
            y = start_y + i
            if 0 <= y < max_y:
                if not credit:  # Empty line as a separator
                    stdscr.addstr(y, start_x, "")
                elif i % 2 == 0:
                    stdscr.addstr(y, start_x, credit, curses.color_pair(1))
                else:
                    stdscr.addstr(y, start_x, credit, curses.color_pair(2))

        stdscr.refresh()
        time.sleep(0.1)  # Adjust the speed as needed for slower scrolling
        start_y -= 1  # Move credits up one row

        # Check for user input to exit
        key = stdscr.getch()
        if key != -1:
            break

if __name__ == "__main__":
    curses.wrapper(show_credits)
