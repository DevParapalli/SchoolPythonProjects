import re
phishing_email_1 = "Robocalls are on the rise. Be wary of any pre-recorded messages you might receive"
phishing_email_2 = "our access to your library account is expiring soon due to inactivity. To continue to have access to the library services account, you must reactivate your account. For this purpose, click the web address below or copy and paste it into your web browser. A successful login will activate your account and you will be redirected to your library profile"
phishing_email_3 = "We detected unknown IP access on our date base computer system our security requires you to verify your account for secure security kindly Click Here and verify your account"
phishing_email_4 = "Password will expire in 2 days  Click Here To Validate E-mail account"
phishing_email_5 = "As we prepare to start the 2016 Tax filling season, we have undergone slight changes in the filling process to make filling for your refund easier and to prevent unnecessary delays. "
phishing_email_6 = "Hello, You have an important email from the Human Resources Department with regards to your December 2015 Paycheck"
phishing_email_7 = "Your parcel (shipping document) arrived at the post office. Here is your Shipping Document/Invoice and copy of DHL receipt for your tracking which includes the bill of lading and DHL tracking number, the new Import/Export policy supplied by DHL Express. Please kindly check the attached to confirm accordingly if your address is correct, before we submit to our outlet office for dispatch to your destination"
phishing_email_8 = "Your Itunes-ID has been disabled. You've place your account under the risk of termination by not keeping the correct informations. Please verify your account as soon as possible. Ready to check ?Click here to get back your account."
phishing_email_9 = "Hello,  Please refer to the vital info I've shared with you using Google Drive.  Click https://www.example.com and sign in to view details. "
phishing_email_10 = "I recently read your last article and it was very useful in my field of research. I wonder, if possible, to send me these articles to use in my current research:This email is enclosed in the Marquette University secure network, hence access it below. Access the documents here https://www.example.com, Ensure your login credentials are correct to avoid cancellations Part of the changes include updating our database with your information."
words1 = (
    phishing_email_1.split() +
    phishing_email_2.split() +
    phishing_email_3.split() +
    phishing_email_4.split() +
    phishing_email_5.split() +
    phishing_email_6.split() +
    phishing_email_7.split() +
    phishing_email_8.split() +
    phishing_email_9.split() +
    phishing_email_10.split()
)  # auto concat to string

common_not_words = ['to', 'the', 'and', 'or', 'you', 'your', 'with',
                    'have', 'had', 'has', 'of', 'in', 'our', 'is', 'for', 'it', 'will','here', 'we']


def clean_word(unclean_word: str) -> str:
    return re.sub('[._, ?]', "", unclean_word.lower())


words2 = [clean_word(i) for i in words1 if i.lower() not in common_not_words] # add cleaned words to the list
counting_dict = {}
for word in words2:
    if word not in counting_dict.keys():
        counting_dict[word] = 1
    elif word in counting_dict.keys():
        counting_dict[word] = counting_dict[word] + 1

# now we create a list with tuples in them and sort based on the counts
ranking_list = []
for key in counting_dict:
    ranking_list.append((key, counting_dict[key]))

sorted_ranking = sorted(ranking_list, key=lambda x: -1 * x[1]) # we multiple by -1 to make them in the reverse order


print(sorted_ranking[0:5])
