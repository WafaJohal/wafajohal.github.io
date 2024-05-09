# Install these packages if needed
# pip install pgmpy
# pip install networkx

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
import networkx as nx
import matplotlib.pyplot as plt

# Define the structure of a simple Bayesian network
model = BayesianNetwork([('Rain', 'Sprinkler'), ('Rain', 'WetGrass'), ('Sprinkler', 'WetGrass')])

# Define the Conditional Probability Tables (CPTs)
cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.7], [0.3]])
cpd_sprinkler = TabularCPD(variable='Sprinkler', variable_card=2, 
                           values=[[0.8, 0.2], [0.2, 0.8]], 
                           evidence=['Rain'], evidence_card=[2])
cpd_wet_grass = TabularCPD(variable='WetGrass', variable_card=2, 
                           values=[[1.0, 0.1, 0.1, 0.01], [0.0, 0.9, 0.9, 0.99]], 
                           evidence=['Sprinkler', 'Rain'], evidence_card=[2, 2])

# Add CPTs to the model
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_wet_grass)

# Verify the model is consistent
assert model.check_model()

# Visualize the Bayesian network using NetworkX
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(model)
nx.draw(model, pos)
plt.title("Bayesian Network Structure")
plt.show()
