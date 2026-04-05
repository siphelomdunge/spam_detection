from file_handling import email_dict
import string 
from pprint import pprint


def clean_email(email_to_clean):
    """Takes in email as string remmoves all punctuation and stop words and return the message as a list of words
    in the sentence"""

    # A list of braek words to be removed from the email
    break_words = [
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
    "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both",
    "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't",
    "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
    "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll",
    "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's",
    "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on",
    "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own",
    "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some",
    "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then",
    "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this",
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we",
    "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's",
    "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with",
    "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your",
    "yours", "yourself", "yourselves"
     ]

    translator = str.maketrans("","",string.punctuation )
    cleaned_enail = []
    
    clean_text = email_to_clean.translate(translator)
    clean_text_list = clean_text.split()
    for word in clean_text_list:
        if word not in break_words:
            cleaned_enail.append(word.lower())


    return cleaned_enail


def count_words(cleaned_email):
    """Takes in a list of words and returns a list of 1s or 0s or 1s and 0s that are going to be feed in the neural 
    Network"""
    vector_lis = []

    for word in spam_vocab:
        if word in cleaned_email:
            vector_lis.append(1)
        else :
            vector_lis.append(0)
    
    return vector_lis

def get_email_vector(email):
    """Takes in the email pass is to the clean email for cleaning and to the count email for vector fixtures"""
    cleaned_email = clean_email(email)
    return count_words(cleaned_email)

# A list of words in spam emails
spam_vocab =[
    "free", "win", "winner", "prize", "cash", "money", "offer", "buy", "cheap", "discount",
    "deal", "credit", "loan", "urgent", "limited", "click", "here", "subscribe", "guarantee", "trial",
    "risk", "bonus", "save", "investment", "earn", "income", "profit", "promotion", "gift", "exclusive",
    "access", "reward", "apply", "claim", "password", "account", "update", "verify", "security", "alert",
    "notification", "important", "deadline", "approval", "congratulations", "refund", "sale", "opportunity",
    "lowest", "special", "clearance", "order", "fast", "shipping", "delivery", "tracking", "service",
    "customer", "support", "help", "contact", "message", "reply", "action", "required", "confirm",
    "verification", "response", "please", "attention", "earnings", "fastcash", "workfromhome", "income",
    "luxury", "million", "overnight", "cashbonus", "clickbelow", "now", "offerexpires", "limitedtime",
    "urgentresponse", "buydirect", "cheapmeds", "miracle", "weightloss", "diet", "noexperience", "easy",
    "instant", "100percent", "winner", "congratulations", "double", "freegift", "riskfree", "cashback",
    "investment", "stocks", "earnings", "passive", "profit", "guaranteed", "getpaid", "workathome",
    "accessnow", "claimprize", "dearfriend", "specialpromotion", "winner", "prizes", "urgent",
    "actnow", "creditcard", "lowrate", "refinance", "nohidden", "fees", "buydirect", "discounted",
    "clearance", "savebig", "orderonline", "callnow", "limitedoffer", "hurry", "exclusiveoffer",
    "applynow", "cashprize", "winbig", "earnfast", "easycash", "freeaccess", "instantapproval",
    "limitedtimeoffer", "lowcost", "discountprice", "guaranteedapproval", "hotdeal", "actfast",
    "bestprice", "100percentfree", "cheapprices", "specialdeal", "freeconsultation", "buyonegetone",
    "onlinesale", "clearanceprice", "cashreward", "urgentmessage", "congratulationsyou", "arewinner",
    "promotionaloffer", "limitedsupply", "newcustomers", "riskfreetrial", "applytoday", "noobligation",
    "calltollfree", "getstarted", "quickcash", "earningsdaily", "workfromyourhome", "financialfreedom",
    "makemoney", "easyincome", "extraincome", "onlinebusiness", "passiveincome", "getrich", "fastmoney",
    "unlimited", "incomeopportunity", "bestoffer", "clicklink", "onlineprofit", "earnnow", "earncash",
    "instantmoney", "quickapproval", "fastapproval", "lowestrates", "nofees", "calltoday", "finalnotice",
    "actnow", "urgentresponse", "lastchance", "limitedavailability", "exclusiveaccess", "riskfreemoney",
    "100percentguaranteed", "dontdelete", "pleaseopen", "winner", "freegiftcard", "instantwin",
    "doubleyourincome", "getpaidtoday", "earncashnow", "creditreport", "loanapproval", "mortgage",
    "refinance", "debtconsolidation", "taxrefund", "irs", "lottery", "jackpot", "milliondollars",
    "inheritance", "funds", "trust", "bankruptcy", "hiddenfees", "urgenthelp", "immediateaction",
    "passwordreset", "accountupdate", "securityalert", "phishing", "scam", "fake", "fraud", "virus",
    "malware", "spyware", "ransomware", "clickbait", "unlimitedaccess", "exclusiveinvite", "vip",
    "luxury", "freevacation", "getaway", "holiday", "allinclusive", "deal", "offerexpires", "sale",
    "clearance", "lowestprice", "specialdiscount", "buyone", "getone", "bonus", "freebonus",
    "noexperienceneeded", "workathomejob", "earnfromhome", "onlinejob", "makefastmoney", "financial",
    "success", "millionaire", "businessopportunity", "wealth", "cashflow", "investmentopportunity",
    "cryptocurrency", "bitcoin", "forex", "trading", "stockmarket", "realestate", "passiveincome",
    "affiliate", "marketing", "networkmarketing", "mlm", "referral", "commission", "earnings",
    "residualincome", "sideincome", "parttimejob", "fulltimejob", "joboffer", "hiring", "applynow",
    "resume", "interview", "salary", "workfromanywhere", "workonline", "onlinebusiness", "success",
    "financialfreedom", "retirement", "investmentplan", "wealthbuilding", "getrichquick", "quickmoney",
    "easywork", "instantaccess", "freeaccess", "specialpromotion", "exclusiveoffer", "discountcoupon",
    "couponcode", "promo", "dealalert", "limitedstock", "clearanceitem", "saleendssoon", "freequote",
    "getpaid", "startnow", "urgent", "important", "confidential", "password", "account", "login",
    "verify", "confirmation", "security", "alert", "alertmessage", "notice", "warning", "actionrequired",
    "updateaccount", "resetpassword", "urgentupdate", "accountlocked", "contactus", "customerservice",
    "supportteam", "helpdesk", "technicalsupport", "billing", "payment", "invoice", "receipt",
    "transaction", "orderconfirmation", "shippingupdate", "deliveryconfirmation", "package", "trackingnumber",
    "refund", "cancellation", "returnpolicy", "guarantee", "warranty", "satisfaction", "riskfree",
    "noobligation", "freeoffer", "bonusoffer", "doubleyourmoney", "easycash", "workathome",
    "makemoneyonline", "earnmoneyfast", "extraincome", "quickcash", "cashbonus", "winmoney",
    "getpaid", "freeaccess", "clickhere", "actnow", "limitedtime", "exclusive", "vipaccess",
    "bestdeal", "lowestprice", "specialoffer", "dealofaday", "freegift", "prizewinner",
    "congratulations", "youhavewon", "jackpot", "lottery", "milliondollar", "inheritance",
    "fundsavailable", "urgentnotice", "legalnotice", "finalnotice", "lastchance", "deadline",
    "importantmessage", "confidentialinformation", "protected", "encrypted", "secure",
    "trusted", "verified", "approved", "official", "government", "irs", "tax", "refund",
    "debt", "consolidation", "bankruptcy", "loan", "mortgage", "creditcard", "lowrate",
    "refinance", "approval", "nohiddenfees", "applyonline", "callnow", "tollfree",
    "urgentresponse", "contactimmediately", "actfast", "dontmissout", "exclusiveaccess",
    "vipoffer", "membersonly", "limitedsupply", "specialpromotion", "newcustomers",
    "riskfreetrial", "satisfactionguaranteed", "moneyback", "freeconsultation",
    "noobligation", "starttoday", "getstarted", "quickapproval", "fastapproval",
    "instantapproval", "earningsdaily", "workfromhome", "financialfreedom", "makemoney",
    "easyincome", "passiveincome", "onlinebusiness", "affiliatemarketing", "networkmarketing",
    "cryptocurrency", "bitcoin", "forextrading", "stockmarket", "realestateinvesting",
    "wealthbuilding", "investmentopportunity", "limitedoffer", "specialdeal", "coupon",
    "discount", "sale", "clearance", "bestprice", "hotdeal", "dealalert", "freequote",
    "moneybackguarantee", "riskfreeoffer", "urgentactionrequired", "accountupdate",
    "securityalert", "passwordreset", "phishingalert", "scamwarning", "virusalert",
    "malwarealert", "spywarealert", "ransomwarealert"
]




# spam_emails = email_dict()[0]
# ham_emails = email_dict()[1]

# empty_dict_1 = {}
# for key , item in ham_emails.items():
#     empty_dict_1[key] = item
    
# empty_dict_2 = {}
# for key, item_2 in spam_emails.items():
#     empty_dict_2[key] = item_2


# def ham_vector_features():
#     cleaned_email = clean_email(empty_dict_1)
#     #pprint(cleaned_email)
#     return count_words(cleaned_email , spam_vocab , 0)
# def spam_vector_features():
#     cleaned_email_2 = clean_email(empty_dict_2)
#     return count_words(cleaned_email_2 , spam_vocab , 1)

#print(list_ham_emails)
#print(count_words(list_ham_emails , spam_vocab))

#print(spam_vector_features())

# def ham_vector_features():
#     cleaned_email = clean_email(empty_dict_1 ,0)
#     return count_words(cleaned_email)


# def spam_vector_features():
#     cleaned_email = clean_email(empty_dict_2,1)
#     return count_words(cleaned_email)
