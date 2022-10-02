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
2. Removing Abbrevations
   Abbrevations are a major cause of the model training. The words causes redundancy and loss of accuracy while model testing and trainng.
   Handling abbrevations can be done by replacing them with their full forms. Then the next steps can be to find keywords, and remove the rest unnecessary ones. 
   Replace the abbrevations with this function:
   ```
   def word_abbrev(word):
    return abbreviations[word.lower()] if word.lower() in abbreviations.keys() else word
   ```

    Apply the above function on dataframe column
   ```
   df['columnname']=df['columnname'].apply(word_abbrev)
   ```



3. 
4. 
5. 