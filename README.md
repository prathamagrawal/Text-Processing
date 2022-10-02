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

    ```
    def replace_abbrev(text):
    string = ""
    for word in text.split():
        string += word_abbrev(word) + " "        
    return string
    ```

    Apply the above function on dataframe column
   ```
    text = replace_abbrev(text)
   ```
3. Removing URLS, HTTPS, NON-ASCII Characters:
   URLS and HTML tags elements must be removed during the preprocessing of any text data. 
   These elements contain <,>,https:,//,www/ and other elements which may cause error while training. 
   NON-ASCII Characters must also be removed.

   Remove the URLS, HTML, ASCII content with the following functions:

    ```
    def remove_URL(text):
        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'URL',text)
    
    def remove_HTML(text):
        html=re.compile(r'<.*?>')
        return html.sub(r'',text)

    def remove_not_ASCII(text):
        text = ''.join([word for word in text if word in string.printable])
        return text
    ```

    These function can be called as:
    ```
    text = remove_URL(text)
    text = remove_HTML(text)
    text = remove_not_ASCII(test)
    ```
4. Removing Emojis / Smileys / mentions / Numbers: 
   Emojis and smileys must be removed since these characters can influence the output of the model. 
   functions to remove the emojis:

    ```
    def remove_mention(text):
        at=re.compile(r'@\S+')
        return at.sub(r'USER',text)

   
    def remove_number(text):
        num = re.compile(r'[-+]?[.\d]*[\d]+[:,.\d]*')
        return num.sub(r'NUMBER', text)

    def remove_emoji(text):
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'EMOJI', text)

    def transcription_sad(text):
        eyes = "[8:=;]"
        nose = "['`\-]"
        smiley = re.compile(r'[8:=;][\'\-]?[(\\/]')
        return smiley.sub(r'SADFACE', text)

    def transcription_smile(text):
        eyes = "[8:=;]"
        nose = "['`\-]"
        smiley = re.compile(r'[8:=;][\'\-]?[)dDp]')
        #smiley = re.compile(r'#{eyes}#{nose}[)d]+|[)d]+#{nose}#{eyes}/i')
        return smiley.sub(r'SMILE', text)

    def transcription_heart(text):
        heart = re.compile(r'<3')
        return heart.sub(r'HEART', text)
    ```
   
   Apply these functions with the following:
   ```
    text = remove_emoji(text)
    text = transcription_sad(text)
    text = transcription_smile(text)
    text = transcription_heart(text)
   ```

### Apply all functions all together:

Applying all functions together can be problematic, it's better to create a single function which can call all functions in the same function. 

Thanks to the developer of pandas, you can apply user-defined functions to particular columns. 

Single Function to call all functions:
```
def clean_tweet(text):
    
    # Remove non text
    text = remove_URL(text)
    text = remove_HTML(text)
    text = remove_not_ASCII(text)
    
    # replace abbreviations, @ and number
    text = replace_abbrev(text)  
    text = remove_mention(text)
    text = remove_number(text)
    
    # Remove emojis / smileys
    text = remove_emoji(text)
    text = transcription_sad(text)
    text = transcription_smile(text)
    text = transcription_heart(text)
  
    return text
```

The above function must be called on the column of the dataset which needs text to be processed. 
One can execute the above function with this command.
```
train["clean_text"] = train["clean_text"].apply(clean_tweet)
```