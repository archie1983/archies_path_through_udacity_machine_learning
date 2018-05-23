def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)

#    print "ftr = "+str(features_train)
#    print "ltr = "+str(labels_train)
#    print "ftst = "+str(features_test)
#    print "ltst = "+str(labels_test)
#    print "pred = "+str(pred)
#    print "len of pred: " + str(len(pred))
#    print "len of ltst: " + str(len(labels_test))

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    from sklearn.metrics import accuracy_score

    accuracy = accuracy_score(labels_test, pred)
#    print "acc: "+str(accuracy)
    # another way apparently: print clf.score(features_test, labels_test)
    return accuracy
