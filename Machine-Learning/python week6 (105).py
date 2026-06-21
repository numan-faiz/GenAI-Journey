# decison tree-data splitting and feature selection part#2
# now lets implement the coding part:

# decision tree splitting demo

import numpy as np
from sklearn.tree import DecisionTreeClassifier,export_text
from sklearn.datasets import make_classification

# create a simple binary dataset

x,y=make_classification(
    n_samples=12,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    random_state=42
)

feature_names=["Feature_1","Feature_2"]
print("\n Dataset(first 8 samples)")

for i in range(8):
    print(f"{feature_names[0]}={x[i,0]:.2f},"
          f"{feature_names[1]}={x[i,1]:.2f},"
          f"class={y[i]}")
    


# train shallow decison tree(depth=2)

tree=DecisionTreeClassifier(
    max_depth=2,
    criterion="gini",   #try aslo:entropy
    random_state=42
)

print(tree.fit(x,y))



# display how the tree split
print("\n Decision tree structure:")
print(export_text(tree,feature_names=feature_names))



# show feature importance (which feature is best)
print("\n feature importance (how much each feature was used):")
for name,importance in zip(feature_names,tree.feature_importances_):
    print(f"{name}:{importance:.3f}")
    