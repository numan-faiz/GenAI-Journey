# decison tree-data splitting and feature selection

# important component of decision tree:
# root node-->where start from the decison tree 
# decision node mean internal node--- put condition on diffrent feature to split data
# leaf node mean terminal node-->its final decision or predicted class 
# branch:a possible outcome of a decision rule leading to the next node


# structure of decision tree
# the sturcture is hierarchical enabling step by step classification


# splitting critiria
# information gain: measures reduction in entropy(noise) after a split (used in ID3).higher gain
#  means after a better split

# gini index:measure the impurity of dataset(used in CART).lower gini value indicates pure subsets
# entropy: mean quantifies uncertainity in the dataset
# entropy=0 means perfectly pured nodes

# maximum purity gain selection: the algorithm chooses the feature that maximizes purity improvement at each step

# overfitting:occurs  when a decision tree becomes too complex and larn noise instead of patterns


# methods to avaoid overfitiing:
# pre-prunning-->(early stopping)
# define tree depth---put limit
# minimum  samples per node
# minimum information gain

# post-prunning-->reduced error prunning
# build the full tree first
# removes weak branches that do not improve performance

# generalization through prunning-->:proper prunning imporves generalization and prevents the 
# tree from memorizing the training data