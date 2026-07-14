# ANN--model evaluation metrics:
# accuracy:
# overall correctness
# formula:
# accuracy:tp+tn/tp+tn+fn+fp

# good when dataset is balanced
# misleading when classes are imbalanced

# example;
# disease detection 99% accuracy  but misses real pateint?--useless
# precison:
# how many predictive positive re correct?
# precison=tp/tp+fp

# high precison:low false alarms
# yse case:
# spam detection-->avoid labeling real emails as spam


# recall(sensitivity):how  many real positive were correctly found?
# recall=tp/tp+fn

# high recall=low missed cases
# use case
# cancer of fraud detection:
# better to catch all positive cases,even with some false alarms

# F!-score=harmonic mean of precison and recall
# f1=2*precison*recall/precison+recall
# usefull when classes are highly imbalanced
# best when we need balance between precuison and recall

# numerical example;
# binary classification:
# result:
# tp=40
# fp=1
# fn=5
# tn=45


# accuracy:0.85
# precison:0.89
# recall:0.89
# f1-score:0.84


# key reminder
# accuracy asnwers:how often right
# precison answers:how often correct when predicting positive
# recall answers--how many actual positive find
# f1 balance precison and recall