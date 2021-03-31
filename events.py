from functions import functions


class events():
    
    def listen(ui):
        
        ui.restart_button.clicked.connect(functions.restart)
        ui.shutdown_button.clicked.connect(functions.shutdown)