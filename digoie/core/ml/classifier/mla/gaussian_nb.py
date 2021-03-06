
from sklearn.naive_bayes import GaussianNB

from digoie.core.ml.classifier.mla.base import MLAlgorithm


class MLGaussianNaiveBayes(MLAlgorithm):

    # ML_NAME = K_NEIGHBORS

    def __init__(self, training_dataset, training_label):
        self.classifier = GaussianNB()
        super(MLGaussianNaiveBayes, self).__init__(self.classifier, training_dataset, training_label)

    def generate(self):
        
        super(MLGaussianNaiveBayes, self).generate()
        # print 'model for (' + self.ML_NAME + ') has been generated'
        # save_model(self.ML_NAME, classifier)
        return self.classifier

        






