import pandas as pd
import plotly.express as px
from models import Risk, Asset

def generate_risk_matrix():
    risks = Risk.query.join(Asset).all()
    data = [{
        "Asset": risk.asset.name,
        "Risk Score": risk.risk_score,
        "Likelihood": risk.likelihood,
        "Impact": risk.impact
    } for risk in risks]
    
    df = pd.DataFrame(data)
    fig = px.scatter(
        df, 
        x="Likelihood", 
        y="Impact", 
        size="Risk Score", 
        color="Asset",
        hover_name="Asset",
        title="Cyber Risk Matrix",
        template="plotly_dark"
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(10,10,26,0.8)',
        plot_bgcolor='rgba(10,10,26,0.8)',
        font=dict(color='white')
    )
    
    fig.write_html("templates/dashboard.html")