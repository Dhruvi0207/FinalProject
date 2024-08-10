from flask import Blueprint, request, jsonify, render_template
from .spam_filter import is_spam

main = Blueprint('main', __name__)

# In-memory storage for messages
messages = []
next_id = 1

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    global next_id

    if request.method == 'POST':
        content = request.json.get('content', '')
        spam = is_spam(content)
        message = {
            "id": next_id,
            "content": content,
            "spam": spam
        }
        messages.append(message)
        next_id += 1
        return jsonify(message)

    elif request.method == 'GET':
        return jsonify(messages)

if __name__ == '__main__':
    from . import create_app
    app = create_app()
    app.run(debug=True)
