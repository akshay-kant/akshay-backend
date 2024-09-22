from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)


def validate_file(file_b64):
    try:
        
        file_data = base64.b64decode(file_b64)
        file_size_kb = len(file_data) / 1024 
        mime_type = "unknown"
        if file_data.startswith(b'\x89PNG'):
            mime_type = "image/png"
        elif file_data.startswith(b'%PDF'):
            mime_type = "application/pdf"
        return True, mime_type, file_size_kb
    except Exception as e:
        return False, None, None


@app.route('/bfhl', methods=['POST'])
def process_post_request():
    data = request.json.get('data')
    file_b64 = request.json.get('file_b64')
    
   
    numbers = [str(x) for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    
    
    lower_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase = sorted(lower_alphabets)[-1] if lower_alphabets else None
    
   
    file_valid, mime_type, file_size_kb = validate_file(file_b64) if file_b64 else (False, None, None)

   
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  
        "email": "john@xyz.com",         
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": mime_type,
        "file_size_kb": file_size_kb
    }
    return jsonify(response)


@app.route('/bfhl', methods=['GET'])
def process_get_request():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
