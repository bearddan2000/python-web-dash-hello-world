import dash
import dash_html_components as html

app = dash.Dash()   #initialising dash app

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1',
		children = 'Hello World',
		style = {
			'textAlign':'cente0r',
			'marginTop':40,
			'marginBottom':40
		}
	)
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
