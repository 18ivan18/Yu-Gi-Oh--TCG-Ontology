from owlready2 import *
import inconsistency
import model
import individuals
import inference
import query
import visualize

print(
    '''
>>> ONTOLOGY CREATION
'''
)

# Create new empty ontology specifing its IRI
onto = get_ontology("http://myonto.com/yugiOntology.owl")
print("Created empty ontology: {}".format(onto.base_iri))

print("\nCreating ontology model ...")
model.createModel(onto)
print("... Done!")

print("\nCreating ontology instances ...")
individuals.addInstances(onto)
inference.addInstances(onto)
query.addInstances(onto)
print("... Done!")

# https://owlready2.readthedocs.io/en/latest/disjoint.html?highlight=close_world
# close_world(onto)

'''
INTRODUCE INCONSISTENCIES
'''

# inconsistency.defense(onto)
# inconsistency.level(onto)
# inconsistency.rarity(onto)
# inconsistency.match(onto)

'''
SAVE OWL FILE
'''

onto.save(file="yugiOntology.owl", format="rdfxml")
print("\nOntology saved in file yugiOntology.owl")

print("\n", end="")

'''
PRINT MODEL
'''

visualize.printModel(onto)
print("\n", end="")


print(
    '''
>>> REASONING
'''
)

# Isolating ontology before reasoning
print("Creating new world for isolating ontology before reasoning ...")
worldBR = World()
onto_path.append(os.getcwd())
worldBR.get_ontology("http://myonto.com/yugiOntology.owl").load()
print("... Done!\n")

# Create new empty ontology specifing its IRI
inferred = get_ontology("http://myonto.com/yugiOntologyInferred.owl")
with inferred:
    # Running HermiT Reasoner
    sync_reasoner([onto], infer_property_values=True)
    # sync_reasoner_pellet()

print("Inconsistent classes: {}".format(list(onto.inconsistent_classes())))

'''
SAVE OWL FILES
'''

inferred.save(file="yugiOntologyInferred.owl", format="rdfxml")
print("\nInferred ontology saved in file yugiOntologyInferred.owl\n")

print(
    '''
>>> QUERYING ONTOLOGY
'''
)

query.executeQuery(worldBR)
