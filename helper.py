import pandas
import json

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def emulate_ml_model(json_input):
    _json_input = json.dumps(json_input)
    input_json_df = pandas.read_json(_json_input, orient='records')

    predict0 = predict1 = -1
    json_length = len(input_json_df['data'])

    output_data = []

    for index in range(json_length):
        userid = input_json_df['data'][index]['Userid']

        if userid == 1:
            prediction = 1
        elif userid == 2:
            prediction = 0
        else:
            raise ValueError("Invalid Userid!")

        data = {
            "Userid": userid,
            "Predict": prediction
        }
        output_data.append(data)

    return output_data
