# decision tree-prunning techniques
# prunnimg methods-->:
# pre-prunning-->early stoping
# A method where the tree-building process is stopped early using predefined critiria or hyperparameter limits
# critiria:maximum depth,minimum number of samples required for diffrenet class
# minimum number ofsamples required to define a leaf node
# statistical methods

# Advatntages:
# faster computational performance
# more efficient
# produces simpler and more genralized trees
# disadvantgaes:
# it may stop optimal barnches from growing,also known as the horizon effect

# post prunning-->after make tree then decide to prune
# first build the full tree,then removes the weak barnches

# applies validation crititria to each subtree
# replace insignifcant branches with lead node
# exhuastive approch
# disadvantages:
# computationally complex



# lez move towrad coding

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


x,y=make_moons(n_samples=600,noise=0.25,random_state=42)
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.3,random_state=42
)


# Part A----pre prunning (early stopping)

depths=list(range(1,15))
train_acc_pre=[]
test_acc_pre=[]

for d in depths:
    tree=DecisionTreeClassifier(
        max_depth=d,  #pre prunning control
        min_samples_leaf=5,  # another pre prunning control
        random_state=42
    )
    tree.fit(x_train,y_train)
    train_acc_pre.append(accuracy_score(y_train,tree.predict(x_train)))
    test_acc_pre.append(accuracy_score(y_test,tree.predict(x_test)))

print(test_acc_pre)



# part2-----post-prunning techniques(cost complexity prunning)
full_tree=DecisionTreeClassifier(random_state=42)
full_tree.fit(x_train,y_train)


# compute prunning path
path=full_tree.cost_complexity_pruning_path(x_train,y_train)
ccp_alphas=path.ccp_alphas
train_acc_post=[]
test_acc_post=[]


for alpha in ccp_alphas:
    pruned_tree=DecisionTreeClassifier(
        ccp_alpha=alpha,
        random_state=42
    )
    pruned_tree.fit(x_train,y_train)
    train_acc_post.append(
        accuracy_score(y_train,pruned_tree.predict(x_train))
    )
    test_acc_post.append(
        accuracy_score(y_test,pruned_tree.predict(x_test))

    )

print(test_acc_post)



# plot results

plt.figure(figsize=(8,5))
plt.plot(depths,train_acc_pre,label="train(pre prunning)")
plt.plot(depths,test_acc_pre,label="test(pre prunning)")
plt.xlabel("tree depth")
plt.ylabel("accuracy")
plt.title("pre prunning :depth vs overfitting")
plt.legend()
plt.grid(True)
plt.tight_layout
plt.show()


plt.figure(figsize=(8,5))
plt.plot(ccp_alphas,train_acc_post,label="train(pre prunning)")
plt.plot(ccp_alphas,test_acc_post,label="test(pre prunning)")
plt.xscale("log")
plt.xlabel("ccp_alpha (prunning strength)")
plt.ylabel("accuracy")
plt.title("post prunning:cost complexity prunning")
plt.legend()
plt.grid(True)
plt.tight_layout
plt.show()

# key takeway
best_alpha=ccp_alphas[np.argmax(test_acc_post)]
print(f"\n best ccp_alpha based on test accuracy:{best_alpha:.6f}")
print("larger ccp_alpha=more agressive prunning")