import random

'''cookiePool = [
    'BAIDUID=680AFBE017326080BDCF6635A15BB9F6:FG=1; BDUSS=pCenNmQTJIR1Q2Q0VFOWVhQmdHT1VvQ0g5UDlFYkNLRjBIR1VvNGZNT2RZLXhhQVFBQUFBJCQAAAAAAAAAAAEAAAAASecu2K2--M377OFvdmVyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ3WxFqd1sRaZV; HMACCOUNT=8AD8C971808461F7; BIDUPSID=680AFBE017326080BDCF6635A15BB9F6; PSTM=1523968363; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1534129820|; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1457_26908_21078_18560_20698_26920_22074'
    '__cfduid=d38f1705eba0a098e1be6044c431d41271534158096; yjs_id=dab06f654ded894804ef438b13605c52; ctrl_time=1; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1534158100,1534158145; PHPSESSID=dffb4527772689bb29b521c27cd02ac0; zkhanmlusername=qq_alive640; zkhanmluserid=551690; zkhanmlgroupid=1; zkhanmlrnd=GtFyyzUTPbfjuCJIJa0E; zkhanmlauth=7fdcd19feb0e74b2ff9a19ed3574146b; zkhanecookieclassrecord=%2C53%2C; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1534164784'
    '__cfduid=d38f1705eba0a098e1be6044c431d41271534158096; yjs_id=dab06f654ded894804ef438b13605c52; ctrl_time=1; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1534158100,1534158145; PHPSESSID=dffb4527772689bb29b521c27cd02ac0; zkhanecookieclassrecord=%2C53%2C; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1534165047'
    ''
]'''





User_agent = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
]
def getHeaders():
    #cookie = random.choice(cookiePool)
    agent = random.choice(User_agent)
    header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'pic.netbian.com',
            'Upgrade - Insecure - Requests': '1',
            'User-Agent': agent
        }
    return header
