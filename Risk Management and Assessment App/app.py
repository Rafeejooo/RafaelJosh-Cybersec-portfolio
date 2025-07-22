
from flask import Flask, jsonify, request
from models import db, Asset, Vulnerability, Threat, Risk
from misp_integration import fetch_misp_events
from flask import render_template
from dashboard import generate_risk_matrix


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost/risk_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/dashboard')
def dashboard():
    generate_risk_matrix()  
    return render_template('dashboard.html', plot_html=open('templates/dashboard.html').read())

@app.route('/')
def home():
    return render_template('dashboard.html', plot_html=open('templates/dashboard.html').read())

@app.route('/fetch-threats', methods=['GET'])
def fetch_threats():
    misp_events = fetch_misp_events()
    for event in misp_events:
        threat = Threat(
            misp_event_id=event['Event']['id'],
            description=event['Event']['info'],
            type='malware'  
        )
        db.session.add(threat)
    db.session.commit()
    return jsonify({"message": f"Added {len(misp_events)} threats"})

@app.route('/calculate-risks', methods=['POST'])
def calculate_risks():
    assets = Asset.query.all()
    for asset in assets:
        vulnerabilities = Vulnerability.query.filter_by(asset_id=asset.id).all()
        threat_count = Threat.query.count()
        likelihood = min(threat_count / 100, 1.0)  
        impact = (asset.criticality / 5) * (sum(v.severity for v in vulnerabilities) / 5)
        risk_score = likelihood * impact
        
        risk = Risk(
            asset_id=asset.id,
            likelihood=likelihood,
            impact=impact,
            risk_score=risk_score
        )
        db.session.add(risk)
    db.session.commit()
    return jsonify({"message": "Risks calculated"})


if __name__ == '__main__':
    app.run(debug=True)