# What is Confusion Matrix? - It is a table that is used in classsification problems to asses where errors in the model where made. here the rows represent actual classes that outcome should have been. while the columns represent the prediction.
# now we will create a confusion matrix.

import numpy
import matplotlib.pyplot as plt
from sklearn import metrics

actual= numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9,size=1000)

confusion_metrix = metrics.confusion_matrix(actual,predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix= confusion_metrix, display_labels=[False, True])
cm_display.plot()
plt.show()

