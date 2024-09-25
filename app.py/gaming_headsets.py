import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a class to represent a gaming headset
class GamingHeadset:
    def __init__(self, name, pros, cons):
        self.name = name
        self.pros = pros
        self.cons = cons
        self.ratings = []  # Store ratings from users

    def add_rating(self, rating):
        if 1 <= rating <= 10:
            self.ratings.append(rating)
        else:
            print("Rating must be between 1 and 10.")

    def average_rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0  # No ratings

# Load or initialize headset data
def load_headsets():
    return [
        GamingHeadset("SteelSeries Arctis Nova Pro", 
                       ["Hi-res audio quality", "Comfortable for long sessions", "Amazing surround sound experience"], 
                       ["Higher price point", "Wired"]),
        
        GamingHeadset("Corsair HS65 Surround", 
                       ["Affordable price", "Dolby Audio 7.1 surround sound", "Lightweight"], 
                       ["Not as durable", "Lacks wireless functionality"]),
        
        GamingHeadset("SteelSeries Arctis Nova Pro Wireless", 
                       ["Exceptional audio quality", "Multi-device connectivity", "Active noise cancellation"], 
                       ["Expensive", "Bulky"]),
        
        GamingHeadset("HyperX Cloud III", 
                       ["Superior microphone quality", "Robust build", "Comfortable fit"], 
                       ["Wired only", "Lacks advanced features"]),
        
        GamingHeadset("Turtle Beach Stealth Pro", 
                       ["Superhuman Hearing tech", "Versatile across platforms", "High-quality audio"], 
                       ["Expensive", "Limited customization"]),
        
        GamingHeadset("Corsair HS55 Wireless", 
                       ["On-the-fly EQ presets", "50ft wireless range", "Lightweight"], 
                       ["Lacks advanced noise-cancelling", "Average battery life"])
    ]

# Load ratings from JSON file
def load_ratings():
    try:
        with open('data/ratings.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save ratings to JSON file
def save_ratings(ratings):
    with open('data/ratings.json', 'w') as f:
        json.dump(ratings, f)

# Initialize ratings data
ratings_data = load_ratings()
headsets = load_headsets()

# Route to display headsets and collect ratings
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        headset_name = request.form['headset_name']
        rating = request.form['rating']
        
        if headset_name in ratings_data:
            ratings_data[headset_name].append(float(rating))
        else:
            ratings_data[headset_name] = [float(rating)]
        
        save_ratings(ratings_data)  # Save updated ratings
        return redirect(url_for('index'))
    
    # Calculate average ratings for display
    for headset in headsets:
        headset.ratings = ratings_data.get(headset.name, [])
    
    return render_template('index.html', headsets=headsets)

if __name__ == '__main__':
    app.run(debug=True)
