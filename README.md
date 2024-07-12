# Kubernetes Deployment and Automated Testing

## Setup

1. Install Minikube or Kind on your local machine
2. Clone this repository
3. Run `minikube start` or `kind create cluster`
4. Deploy the services using `kubectl apply -f deploy.yaml`

## Running Automated Tests

1. Install Pytest using `pip install pytest`
2. Run `pytest test_frontend_backend_integration.py`

## Verification

1. Access the frontend URL at `http://localhost:8080`
2. Verify that the greeting message from the backend is displayed
