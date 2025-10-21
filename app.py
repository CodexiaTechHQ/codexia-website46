from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # templates/index.html dosyasını çağırır
    return render_template('index.html')

if __name__ == '__main__':
    # Basit bir sunucu ile uygulamayı başlatır (Render'da bu otomatik yapılır)
    app.run(debug=True)