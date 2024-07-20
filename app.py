from flask import Flask, request, jsonify

app = Flask(name)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200554065"})

# Route to handle Dialogflow webhook requests
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Extract intent name from the request
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    # Example of handling different intents and generating responses
    if intent == 'ExerciseInstructions':
        response_text = "Here is the information regarding the exercises you want to perform."
    elif intent == 'ExerciseRecommendation':
        response_text = "Here are some recommendations depending on the exercise."
    elif intent == 'FormCorrection':
        response_text = "You can learn how to perform exercise correctly."
    elif intent == 'SafetyGuideline':
        response_text = "Here are the safety measures that you can use while performing the exercises."
    else:
        response_text = "I'm not sure how to respond to that."

    # Return the response in the required format
    return jsonify({
        "fulfillmentText": response_text
    })

if name == 'main':
    app.run(debug=True)