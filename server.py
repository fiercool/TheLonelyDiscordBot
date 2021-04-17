from flask import Flask, render_template
from threading import Thread


app = Flask(
  __name__,
  static_folder='static'  
  )



@app.route('/')
def main():
  #return("hi")
  return render_template('index.html') 

@app.route('/2')
def page_2():
	return render_template('site2.html')



def run():
    app.run(host="0.0.0.0", port=8080)

def start():
    server = Thread(target=run)
    server.start()