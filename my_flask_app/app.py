from flask import Flask

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route cơ bản
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)