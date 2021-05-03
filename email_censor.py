class Email:
    def __init__(self, email_file):
        self.email_content = open(email_file).read()
    def __repr__(self):
        return self.email_content
    def censor(self, censor_words=None, neg_words=None, all=False):        
        
        # Internal Method 1: Censor words in censor_words list
        def terms_censor(email_content=self.email_content):
            censored_content = email_content
            for word in censor_words:
                censored_content = censored_content.replace(word, '__________')
                censored_content = censored_content.replace(word.title(), '__________')
            return censored_content
        
        # Internal Method 2: Censor words in neg_words list
        def neg_censor(email_content=self.email_content):
            
            # Break the content into a list of separate words and punctuations
            censored_content = email_content
            censored_content_list = censored_content.split()
            neg_word_count = 0
            for word_index in range(len(censored_content_list)):
                word = censored_content_list[word_index]              
                
                # Check if each word (both lower case and title case) 
                # of the email match words in negative words list
                # If neg_word count is < 2, increase 1
                if word in neg_words and neg_word_count < 2:
                    neg_word_count += 1
                elif word.title() in neg_words and neg_word_count < 2:
                    neg_word_count += 1
                
                # If neg_word_count is 2, then replace the next match
                elif word in neg_words and neg_word_count == 2:
                    censored_content_list[word_index] = '__________'
                elif word.title() in neg_words and neg_word_count == 2:
                    censored_content_list[word_index] = '__________'
            
            # Join the list
            censored_content = ' '.join(censored_content_list)
            return censored_content
        
        # Internal Method 3: Censor words before and after censored words:
        def all_censor(email_content=self.email_content):
            output = terms_censor()
            output = neg_censor(output)
            word_list = output.split()
            for word_index in range(len(word_list)):
                word = word_list[word_index]
                if word.find('__________') > -1:
                    try:
                        word_list[word_index - 1] = '____T____'
                        word_list[word_index + 1] = '____T____'
                    except:
                        pass
            output = ' '.join(word_list).replace('____T____', '__________')
            return output
        
        # Conditions to run relevant internal methods
        if censor_words and neg_words is None and all is False:
            print('\nTERMS CENSOR OUTPUT:\n')
            return terms_censor()
        # elif censor_words is not None and neg_words is not None and all is False:
        elif censor_words and neg_words and all is False:
            output = terms_censor()
            output = neg_censor(output)
            print('\nTERMS AND NEGATIVE WORDS CENSOR OUTPUT:\n')
            return output
        else:
            output = all_censor()
            print('\nCENSOR-ALL OUTPUT:\n')
            return output
        
                   
                

        
        
## Test code from here
# email_one = Email('email_one.txt')
# email_two = Email('email_two.txt')
# email_three = Email('email_three.txt')
# email_four = Email('email_four.txt')

# proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]
# negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressing", "distressed", "concerning", "horrible", "horribly", "questionable"]

# print(email_three.censor(censor_words=proprietary_terms, neg_words=negative_words, all=True))
