from dash import *
from testapp import *

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    github_info_header(),
<<<<<<< HEAD
    html.Img(src="assets/wsb.jpeg")
=======
    html.Img(src="assets/burb.jpeg")
>>>>>>> 01526993d6c0055a458d4633a939e88c0e3cf780
])

if __name__ == '__main__':
    app.run_server(debug=True)






