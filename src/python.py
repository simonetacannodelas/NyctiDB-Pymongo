import pymongo
from data.model_library import model_list
from data.parameter_limits import parlimit_list
from data.problem_library import problem_list
from data.par_library import parameter_list
from data.model_library_theory import theory_list


client = pymongo.MongoClient("mongodb+srv://simoca:<password>@minerva.hvmsm.mongodb.net/Minerva?retryWrites=true&w=majority")
minerva = client.test

#Create a new database on the cluster
minerva = client.minerva

#Create a new collection on the database
models = minerva.models
parameters=minerva.parameters
parameters_limits = minerva.parameters_limits
issues = minerva.issues
models_theory = minerva.models_theory

#for the model library
for item in model_list:
    models.insert_one(item)

#for the parameters library
for item in parameter_list:
    parameters.insert_one(item)

#for the parameter limits library
for item in parlimit_list:
    parameters_limits.insert_one(item)

#for the issue library
for item in problem_list:
    issues.insert_one(item)

#for the theory library
for item in theory_list:
    models_theory.insert_one(item)
