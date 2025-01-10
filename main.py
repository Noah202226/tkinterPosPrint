from mymongo.database import get_database
from mymongo.crud import get_state
from gui.main_window import show_main_window
from gui.login_window import show_login_window

def main():
    db = get_database()
    state = get_state(db)

    print(state)
    
    if state == 'open':
        show_main_window()
    else:
        show_login_window()

if __name__ == "__main__":
    main()
