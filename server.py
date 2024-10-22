from flask import Flask, render_template, request
import json

app = Flask(__name__)
data_file = 'posts.json'

def load_posts():
    with open(data_file, 'r') as file:
        return json.load(file)
    
def save_post(posts):
    with open(data_file, 'w') as file:
        json.dump(posts, file)

@app.route('/', methods=['GET', 'POST'])
def home():
    posts = load_posts()
    if request.method == "POST":
        name = request.form.get('name')
        content = request.form.get('content')
        posts.append({'name': name, 'content': content})
        save_post(posts)
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)