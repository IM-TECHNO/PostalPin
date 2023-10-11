from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_district', methods=['GET'])
def get_district():
    pincode = request.args.get('pincode')
    district = get_district_name(pincode)
    print(pincode, district)
    
    if district:
        return district
    else:
        return jsonify({'error': 'No district found for the given pincode'})

def get_district_name(pincode):
    url = f"https://api.postalpincode.in/pincode/{pincode}"
    response = requests.get(url)
    data = response.json()
    
    if data[0]['Status'] == 'Success':
        return data[0]['PostOffice'][0]['District']
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
