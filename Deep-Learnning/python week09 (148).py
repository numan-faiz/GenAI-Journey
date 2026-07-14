# ANN-training parameter and learning rate

# under-trained/underfitting
# model has not enough learn from data
# high training error 
# high testing error

# model too simple/trained for too few epochs

# causes:
# too few epochs
# too few layers /neurons
# high learning rate
# insufficeint feature

# result:
# model fail to capture patterns

# over fitting/over tarinning
# model learns too much,including noise
# low training error
# high testing error (poor generalization)

# causes:
# too many epochs
# too complex model
# not enough training data
# no regularization
# (dropout,l2)
# result:
# perform weel on training data but bad on new daata
# confusion matrix:
# how model confused

# TP:correctly predicted positive
# TN: correctly predicted negataive
# FP :wrongly predicted positive
# FN:missed positve case

# accurcy:tp+tn/total
#  precision:tp/tp+fp
#  recall:tp/tp+fn
# F1-score=harmonic mean (precison and recall)

# key takways:
# confusin matrix help to evaluate how well model distinghushes classes


# ==================================================================================
# ANN-TRAINING PARAMETER AND LEARNING RATE - NOTES WITH EXPLANATIONS
# ==================================================================================

# ----------------------------------------------------------------------------------
# Under-trained / Underfitting
# ----------------------------------------------------------------------------------
# - Model has not enough learn from data
# ----------------------------------------------------------------------------------
# EXPLANATION: Model ne data ko sahi tarah se parha hi nahi hai, is liye uski learning 
# adhuri reh gayi hai.
# ----------------------------------------------------------------------------------
# - High training error 
# - High testing error
# ----------------------------------------------------------------------------------
# EXPLANATION: Model khud training ke dauran bhi gande marks (high error) lata hai aur 
# jab naye data par test kiya jaye toh wahan bhi fail hota hai.
# ----------------------------------------------------------------------------------
# - Model too simple / trained for too few epochs
# ----------------------------------------------------------------------------------
# EXPLANATION: Ya toh model ka structure boht zyada aasan/chota hai, ya phir humne use 
# boht kam chakaron (epochs) ke liye train kiya.


# ----------------------------------------------------------------------------------
# Causes (Underfitting Ki Wajah):
# ----------------------------------------------------------------------------------
# - Too few epochs
# ----------------------------------------------------------------------------------
# EXPLANATION: Model ko parhne ke liye poora time nahi diya gaya (jaldi training rok di).
# ----------------------------------------------------------------------------------
# - Too few layers / neurons
# ----------------------------------------------------------------------------------
# EXPLANATION: Network boht chota hai, complex patterns samajhne ki salahiyat hi nahi hai.
# ----------------------------------------------------------------------------------
# - High learning rate
# ----------------------------------------------------------------------------------
# EXPLANATION: Speed boht tez thi (η high tha), jiski wajah se model sahi weights par 
# rukne ke bajaye aage nikal gaya (overshoot kar gaya).
# ----------------------------------------------------------------------------------
# - Insufficient features
# ----------------------------------------------------------------------------------
# EXPLANATION: Data ke andar kaam ki information (columns/features) boht kam thin, jisse 
# model kuch seekh nahi paya.


# ----------------------------------------------------------------------------------
# Result:
# ----------------------------------------------------------------------------------
# - Model fail to capture patterns
# ----------------------------------------------------------------------------------
# EXPLANATION: Aakhiri nateeja yeh nikalta hai ke model data ke aasan trends aur 
# patterns ko bhi pehchanne me nakaam rehta hai.


# ----------------------------------------------------------------------------------
# Overfitting / Over-training
# ----------------------------------------------------------------------------------
# - Model learns too much, including noise
# ----------------------------------------------------------------------------------
# EXPLANATION: Model parhai me had se aage nikal gaya hai, woh kaam ke patterns ke sath 
# sath data ka faltu kachra (noise) bhi yaad kar raha hai.
# ----------------------------------------------------------------------------------
# - Low training error
# ----------------------------------------------------------------------------------
# EXPLANATION: Training data par iska error na hone ke barabar hota hai (yaani 100% score).
# ----------------------------------------------------------------------------------
# - High testing error (poor generalization)
# ----------------------------------------------------------------------------------
# EXPLANATION: Lekin jab naye real-world data (test data) par parhaoge toh buri tarah 
# fail ho jayega kyunke yeh nayi situations ko samajh nahi pata (poor generalization).


# ----------------------------------------------------------------------------------
# Causes (Overfitting Ki Wajah):
# ----------------------------------------------------------------------------------
# - Too many epochs
# ----------------------------------------------------------------------------------
# EXPLANATION: Model ko boht lambe arse tak baar baar sabaq ratawaya gaya.
# ----------------------------------------------------------------------------------
# - Too complex model
# ----------------------------------------------------------------------------------
# EXPLANATION: Network me zarurat se zyada hidden layers aur neurons thons diye gaye hain.
# ----------------------------------------------------------------------------------
# - Not enough training data
# ----------------------------------------------------------------------------------
# EXPLANATION: Seekhne ke liye data boht thoda tha, isliye model ne usi thode se data ko 
# poora chaat liya/ratt liya.
# ----------------------------------------------------------------------------------
# - No regularization (dropout, l2)
# ----------------------------------------------------------------------------------
# EXPLANATION: Training par koi jhatka ya brake (jaise neurons ko randomly band karna ya 
# penalty lagana) nahi lagayi gayi.


# ----------------------------------------------------------------------------------
# Result:
# ----------------------------------------------------------------------------------
# - Perform well on training data but bad on new data
# ----------------------------------------------------------------------------------
# EXPLANATION: Purane ratey-rateye sawalon par champion hai, par naye sawal aate hi 
# dher ho jata hai.


# ==================================================================================
# CONFUSION MATRIX: How model confused
# ==================================================================================
# EXPLANATION: Yeh ek aisa table hai jo saaf dikhata hai ke classification karte waqt 
# model kahan dhoka kha gaya aur kahan sach bol gaya.
# ----------------------------------------------------------------------------------
# - TP: correctly predicted positive
# ----------------------------------------------------------------------------------
# EXPLANATION: True Positive -> Banda sach me bimar tha, aur AI ne bhi sahi bimar bataya.
# ----------------------------------------------------------------------------------
# - TN: correctly predicted negative
# ----------------------------------------------------------------------------------
# EXPLANATION: True Negative -> Banda bilkul theek/sehatmand tha, AI ne bhi sahi sehatmand bataya.
# ----------------------------------------------------------------------------------
# - FP: wrongly predicted positive
# ----------------------------------------------------------------------------------
# EXPLANATION: False Positive -> Banda sehatmand tha, par AI ne ghalti se keh diya "Bimar hai" 
# (Ghalat Alarm / Type 1 Error).
# ----------------------------------------------------------------------------------
# - FN: missed positive case
# ----------------------------------------------------------------------------------
# EXPLANATION: False Negative -> Banda bimar tha, par AI ne miss kar diya aur kaha "Theek hai" 
# (Khatarnak Ghalati / Type 2 Error).


# ----------------------------------------------------------------------------------
# Metrics Formulas:
# ----------------------------------------------------------------------------------
# - Accuracy: (tp + tn) / total
# ----------------------------------------------------------------------------------
# EXPLANATION: Poore dataset me se model ne total kitne sahi faisle (TP aur TN) kiye.
# ----------------------------------------------------------------------------------
# - Precision: tp / (tp + fp)
# ----------------------------------------------------------------------------------
# EXPLANATION: Jab bhi model ne kaha "Positive hai", toh us me se kitne feesad dawa sach nikli. 
# (FP ko kam karne ke liye dekha jata hai).
# ----------------------------------------------------------------------------------
# - Recall: tp / (tp + fn)
# ----------------------------------------------------------------------------------
# EXPLANATION: Asli bimaron me se model kitne feesad logon ko dhoond paaya aur kitne miss (FN) kiye.
# ----------------------------------------------------------------------------------
# - F1-score = harmonic mean (precision and recall)
# ----------------------------------------------------------------------------------
# EXPLANATION: Precision aur Recall ka ek darmayana balance balance score naapne ka scale.


# ----------------------------------------------------------------------------------
# Key Takeaways:
# ----------------------------------------------------------------------------------
# - Confusion matrix help to evaluate how well model distinguishes classes
# ----------------------------------------------------------------------------------
# EXPLANATION: Sabse zaroori baat yeh hai ke matrix se humein yeh aaina dikhta hai ke 
# model alag alag classes (jaise bimari ya sehat) ke beech farq sahi se kar pa raha hai ya nahi.
# ==================================================================================