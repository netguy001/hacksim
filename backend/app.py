from flask import Flask
from flask_cors import CORS
from routes.simulation import simulation_bp
from routes.logs import logs_bp

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for frontend communication
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(simulation_bp)
    app.register_blueprint(logs_bp)
    
    @app.route('/')
    def index():
        return {"message": "HackSim Backend API", "status": "running"}
    
    return app

app = create_app()
