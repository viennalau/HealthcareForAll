import pandas
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# This is where the dataset is from https://www.kaggle.com/datasets/walterconway/covid-flu-cold-symptoms?resource=download
data = pandas.read_csv("/content/drive/MyDrive/Copy of large_data - large_data.csv")

# Importing data into a pandas dataframe
# Setting the headings and then print out for the first rows and columns to see if it looks correct
df = pandas.DataFrame(data)
df.columns = ['COUGH',	'MUSCLE_ACHES',	'TIREDNESS', 'SORE_THROAT',	'RUNNY_NOSE',	'STUFFY_NOSE',	'FEVER',	'NAUSEA',	'VOMITING',	'DIARRHEA',	'SHORTNESS_OF_BREATH',	'DIFFICULTY_BREATHING',	'LOSS_OF_TASTE',	'LOSS_OF_SMELL',	'ITCHY_NOSE',	'ITCHY_EYES',	'ITCHY_MOUTH',	'ITCHY_INNER_EAR','SNEEZING',	'PINK_EYE', 'TYPE']
print(df.head)


# X = different types of symptoms
X = df[['COUGH',	'MUSCLE_ACHES',	'TIREDNESS', 'SORE_THROAT',	'RUNNY_NOSE',	'STUFFY_NOSE',	'FEVER',	'NAUSEA',	'VOMITING',	'DIARRHEA',	'SHORTNESS_OF_BREATH',	'DIFFICULTY_BREATHING',	'LOSS_OF_TASTE',	'LOSS_OF_SMELL',	'ITCHY_NOSE',	'ITCHY_EYES',	'ITCHY_MOUTH',	'ITCHY_INNER_EAR','SNEEZING',	'PINK_EYE']]

# Y = Symptom type
Y = df['TYPE']

# Now we are splitting the data into a training set vs. the testing set. The training set is what we
# use to train the model and the testing set is used as a comparision to see the similarities.
# Test size = 0.2 which means 20% of the data is used to test the model and 80% is used to train the model
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# This creates a logistic regression classifier, clf = classifier
clf = LogisticRegression(max_iter=100)

# This trains the model via the training set/data
clf.fit(X_train, y_train)

# The model is now trained and we use it to make predictions
predictions = clf.predict(X_test)

# Now we will see how accurate our model is!
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Save the trained model
with open('trained_model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)