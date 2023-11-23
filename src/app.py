from flask import Flask, render_template
import serviceinfo
import config

app=Flask(__name__)

services_list= config.services_to_monitor
service_handler=serviceinfo.ServiceData(services=services_list)


@app.route('/')
def service_returner():
    services_status_dlist=[]
    for service in services_list:
        services_status_dlist.append(service_handler.get_status(service))
    return render_template('index.html',services_status=services_status_dlist)

if __name__ == '__main__':
    app.run(debug=True)