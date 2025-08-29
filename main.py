from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        input_data = request.get_json()

        if not input_data or 'data' not in input_data or not isinstance(input_data['data'], list):
            return jsonify({
                "is_success": False,
                "user_id": "chakravardhan",
                "error": "Invalid JSON format or missing 'data' key."
            }), 400

        data_array = input_data['data']

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_chars = []
        total_sum = 0
        alphabet_string = ""

        for item in data_array:
            if item.isalpha():
                alphabets.append(item.upper())
                alphabet_string += item
            elif item.isnumeric():
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
            else:
                special_chars.append(item)

        reversed_alphabets = alphabet_string[::-1]
        concat_string_list = []
        for i, char in enumerate(reversed_alphabets):
            if i % 2 == 0:
                concat_string_list.append(char.upper())
            else:
                concat_string_list.append(char.lower())
        final_concat_string = "".join(concat_string_list)
        
        response = {
            "is_success": True,
            "user_id": "chakravardhan",
            "email": "chakravardhan.naidu2022@vitstudent.ac.in",
            "roll_number": "22BCT0089",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),
            "concat_string": final_concat_string
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "user_id": "chakravardhan",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
