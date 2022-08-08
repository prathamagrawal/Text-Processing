# Learn with me 
# How NLP Model works

## Preprocessing the text 
There are multiple steps and ways to preprocess the unstructured text data. 
The traditional approach consists of various ways:
1. Removing Punctuations
Get all Punctuations from the inbuilt library
```
string.punctuation
```
Remove the text from by declaring a function
```
def clean_text(text):
    clean_text = [char for char in text if char not in string.punctuation]
    clean_text = ''.join(clean_text)
    return clean_text 

```

apply function on dataframe column 
```
df['columnname']=df['columnname'].apply(clean_text)
```
2. 
3. 
4. 
5. 