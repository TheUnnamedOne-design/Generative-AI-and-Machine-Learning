import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

df=pd.read_csv('IMDB Dataset.csv')
print(df.head())

X=df['review']
Y=df['sentiment']

Y=Y.map({'positive':1,'negative':0})

vectorizer=CountVectorizer(stop_words='english',max_features=10000)
X_vectorized=vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test=train_test_split(X_vectorized,Y,test_size=0.2,random_state=42)

model=LogisticRegression(max_iter=10000)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print(classification_report(y_test,y_pred))


cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

