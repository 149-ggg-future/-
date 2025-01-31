import requests
import json
max_page = 4
def pagein(page):
    base_url = ('https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=')
    b_url = '&num=80&sort=symbol&asc=1&node=hs_bjs&symbol=&_s_r_a'
    new_url = f"{base_url}{page}{b_url}"
    return new_url
def codein(code,q):
    #q=1获取具体网页，2获取内部实时刷新数据网址
    if q==1:
        base_url = 'https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/'
        b_url = '/displaytype/4.phtml'
        new_url = f"{base_url}{code}{b_url}"
    elif q==2:
        base_url = 'https://quotes.sina.cn/cn/api/openapi.php/CompanyFinanceService.getFinanceReport2022?paperCode='
        b_url = '&source=gjzb&type=0&page=1&num=10&callback=hqccall78'
        new_url = f"{base_url}{code}{b_url}"
    return new_url
def getjsondate(url,q):
    if q==1:
        response = requests.get(url)
        date=response.json()
        return date
    if q==2:
        response = requests.get(url)
        response=response.text
        response = response.lstrip("/*<script>location.href='//sina.com';</script>*/")
        json_str = response[len("hqccall78(("):-2]
        return json_str
def jiexijson(jsondate):
    json_data = json.loads(jsondate)
    its = ["营业总收入", "营业成本"]
    for i in json_data["result"]["data"]["report_list"]:
        gupiaos = json_data["result"]["data"]["report_list"][i]["data"]
        print(i)
        for gupiao in gupiaos:
            if gupiao["item_title"] in its:
                print(gupiao["item_title"])
                print(gupiao["item_value"])
for page in range(1,max_page+1):
    pagejsons=getjsondate(pagein(page),1)
    for pagejson in pagejsons:
        dateurl=codein(pagejson['symbol'],2)
        result=getjsondate(dateurl,2)
        print(pagejson['name'])
        jiexijson(result)








