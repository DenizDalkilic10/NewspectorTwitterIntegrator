import ServerApplication
import time
server_app = ServerApplication.ServerApplication()

var = 1
while var == 1:  # This constructs an infinite loop
    server_app.run()
    time.sleep(60)
