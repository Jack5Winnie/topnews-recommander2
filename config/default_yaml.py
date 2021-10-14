import yaml
from collections import defaultdict

def config_yaml_gen():
    dict_file = [
        {'api_key': ["112c9b2a21544785ac573f0221cff7ed", "3ce897ffb4bc49bcb5ca9dd364e9a79e", "4cd6e413c31d4ab99f623f6aaedf42bb","afd69464ff3b4c1797ebc028ebb1bfb5", "b15eab96a2514381bbe527deaf3722ea", "ca3e3bf276f44abbbf5e78402fe42202"] },
        {'sources' : ['the-wall-street-journal','fortune','financial-post','business-insider','business-insider-uk','australian-financial-review','hacker-news','wired','crypto-coins-news']},
        {'keywords' : ['(NOT (election OR cyber OR (network)))', '(us AND fed)', '(eurodollar)', 'etf', 'bond', 'nasdaq', 'semiconductor', 'libor', '(book AND ratio)' ,'(ted AND spread)' ,'(stake AND in)', '((stock OR shares) AND (worth OR value))' ,'((join OR added OR inclusion) AND (index OR msci))', '((share OR stock) AND (split OR ipo))', '(electric AND (vehicle OR car))', '((solar AND power) OR energy)', 'currency','(exchange AND dollars)', '(economic AND indicators)']},
        {'KeyWord_Posit' : ['esg', 'bond', 'treasur', 'yield', 's&p' , 'nyse','dow', 'gdp', 'repo', 'ppp', 'earning', 'revenue', 'nikkei', 'capital', 'eps', 'p/b', 'p/e', 'bank', 'roa', 'stock', 'ipo', 'split', 'dividend', 'fed','etf','nasdaq', 'brexit', 'tsmc', 'iphone', 'telsa', '5g', 'ai', 'iot', 'blockchain','semiconductor', 'join', 'inclusion', 'added', 'index', 'e-commerce', 'msci', 'oil', 'brent', 'opec', 'imf', 'electric', 'vehicle', 'car', 'solar', 'exchange', 'dollars', 'pound', 'economic', 'indicators', 'crash', 'bdi', 'cpi', 'ppi']},
        {'KeyWord_Negat' : ['elect', 'soccer', 'cyber', 'sport', 'vote', 'voting', 'vot', 'kick', 'covid', 'Corona' ,'Coronavirus', 'nurs','attacks', 'directx', 'biden', 'race', 'battery', 'racing', 'career', 'offers', 'campus', 'eviction', 'college', 'sex', 'breakthrough', 'pandemic', 'spy', 'hacker','writer', 'ban', 'republican', 'veteran', 'uaw']},
        {'sort_by': 'popularity'},
        {'language': 'en'},
        {'page_size': 100},
        {'hoursAgo': 24},
        {'TNewsSize': 20}
    ]

    with open(r'./config/config.yaml', 'w') as file:
        documents = yaml.dump(dict_file, file)
        print(documents)
    return

def config_yaml_test():
    with open(r'./config/config.yaml') as file:
        cfg = yaml.full_load(file)

    api_key=  cfg[0]['api_key']
    sources=  ', '.join(tuple(cfg[1]['sources']))
    keywords= ' OR '.join(tuple(cfg[2]['keywords']))
    KeyWord_Posit =cfg[3]['KeyWord_Posit']
    KeyWord_Negat =cfg[4]['KeyWord_Negat']
    sort_by=  cfg[5]['sort_by']     # 'popularity'
    language= cfg[6]['language']
    page_size=cfg[7]['page_size']
    hoursAgo= cfg[8]['hoursAgo']
    TNewsSize=cfg[9]['TNewsSize']
    MaxNewsSize=cfg[10]['MaxNewsSize']

    print('api_key=', api_key)
    print('\nsources=', sources)
    print('\nkeywords=', keywords)
    print('\nKeyWord_Posit=', KeyWord_Posit)
    print('\nKeyWord_Negat=', KeyWord_Negat)
    print('sort_by=', sort_by)
    print('language=', language)
    print('page_size=', page_size)
    print('hoursAgo=', hoursAgo)
    print('TNewsSize=', TNewsSize)
    print('MaxNewsSize=', MaxNewsSize)
    return

#from newscatcher import Newscatcher,urls
def newscatcher_sources_all_gen():
    dict_file = [
        {'sources' : ['marketwatch.com', 'investopedia.com', 'seekingalpha.com', 'xe.com', 'thestreet.com', 'financialpost.com', 'investing.com', 'kiplinger.com', 'benzinga.com', 'thisismoney.co.uk', 'cityam.com', 'daveramsey.com', 'fin24.com', 'smartasset.com', 'investorplace.com', 'institutionalinvestor.com', 'ritholtz.com', 'marketrealist.com', 'pionline.com', 'efinancialcareers.com', 'marketoracle.co.uk', 'moneymorning.com', 'financial-planning.com', 'citywire.co.uk', 'wealthmanagement.com', 'investmentwatchblog.com', 'moneytalksnews.com', 'morningstar.co.uk', 'insidermonkey.com', 'risk.net', 'realclearmarkets.com', 'financialsamurai.com', 'worldfinance.com', 'armstrongeconomics.com', 'savingadvice.com', 'fool.co.uk', 'elliottwave.com', 'simplywall.st', 'kitces.com', 'etfdailynews.com', 'investmentweek.co.uk', 'globalcapital.com', 'interest.co.nz', 'ai-cio.com', 'fool.ca', 'learnbonds.com', 'wallstreetdaily.com', 'abladvisor.com', 'fool.com.au', 'investmentexecutive.com', 'investmentu.com', 'finanzen.ch', 'financeasia.com', 'mybudget360.com', 'wallstreetpit.com', 'swfinstitute.org', 'wealthdaily.com', 'waterstechnology.com', 'smallcaps.com.au', 'finews.asia', 'marketsmedia.com', 'moneymanagement.com.au', 'smarteranalyst.com', 'moneyobserver.com', 'trustnet.com', 'themiddlemarket.com', 'finews.com', 'insidefutures.com', 'stockmarketwire.com', 'dailyreckoning.com.au', 'thetradenews.com', 'equitymaster.com', 'financialreporter.co.uk', 'ringgitplus.com', 'hedgeco.net', 'brokernews.com.au', 'theadviser.com.au', 'cnafinance.com', 'asianinvestor.net', 'dailyalts.com']
        }]
    with open(r'./config/newscatcher_sources_all.yaml', 'w') as file:
        documents = yaml.dump(dict_file, file)
    return

if __name__ == "__main__":
    newscatcher_sources_all_gen()
    config_yaml_gen()
    config_yaml_test()