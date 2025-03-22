import os
from flask import Flask, jsonify, render_template, request
import pymysql
from dotenv import load_dotenv

# Nạp các biến môi trường từ file .env
load_dotenv()

app = Flask(__name__)

# Hàm kết nối tới cơ sở dữ liệu MySQL
def get_db_connection():
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),  # Lấy giá trị từ biến môi trường
        user=os.getenv('DB_USER'),  # Lấy giá trị từ biến môi trường
        password=os.getenv('DB_PASSWORD'),  # Lấy giá trị từ biến môi trường
        db=os.getenv('DB_NAME'),  # Lấy giá trị từ biến môi trường
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Kiểm tra tình trạng server
@app.route('/health')
def health():
    return "Up & Running"

# Tạo bảng trong cơ sở dữ liệu nếu chưa tồn tại
@app.route('/create_table')
def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Câu lệnh SQL để tạo bảng nếu chưa tồn tại
    create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """
    
    # Thực thi câu lệnh SQL để tạo bảng
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()
    return "Table created successfully"

# Chèn một bản ghi vào bảng
@app.route('/insert_record', methods=['POST'])
def insert_record():
    name = request.json['name']  # Lấy dữ liệu từ JSON request
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Câu lệnh SQL để chèn bản ghi
    insert_query = "INSERT INTO example_table (name) VALUES (%s)"
    cursor.execute(insert_query, (name,))
    connection.commit()
    connection.close()
    return "Record inserted successfully"

# Truy vấn tất cả dữ liệu từ bảng
@app.route('/data')
def data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM example_table')  # Lấy tất cả dữ liệu từ bảng
    result = cursor.fetchall()  # Lấy kết quả
    connection.close()
    return jsonify(result)

# Trang chính (UI route)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Chạy ứng dụng Flask
