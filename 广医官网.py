import webbrowser
import re

str='''url1:'https://www.gzhmu.edu.cn/',#官网
url2:'https://jwc.gzhmu.edu.cn/',#教务处
url3:'https://gzhmu.fanya.chaoxing.com/portal',#e学中心
url4:'https://zs.gzhmu.edu.cn/',#本科招生网
url5:'https://www.yiban.cn/school/index/id/18143',#易班
url6:'https://yjs.gzhmu.edu.cn/',#研究生院
url7:'https://mks.gzhmu.edu.cn/',#马克思主义学院
url8:'https://xxgk.gzhmu.edu.cn/',#信息公开网
url9:'https://xfjs.gzhmu.edu.cn/',#学风建设网
url10:'https://jwc.gzhmu.edu.cn/pgrz/',#评估认证网
url11:'https://jfzx.gzhmu.edu.cn/',#教师教学与发展研究中心
url12:'https://kcsz.gzhmu.edu.cn/',#课程思政教学研究中心
url13:'https://nsxz.gzhmu.edu.cn/',#南山学者
url14:'https://news.gzhmu.edu.cn/',#新闻网
url15:'https://cwc.gzhmu.edu.cn/',#财务处
url16:'https://kyc.gzhmu.edu.cn/',#科研处
url17:'https://dev.gzhmu.edu.cn/',#发展规划处
url18:'https://jxms.gzhmu.edu.cn/',#教学名师网
url19:'https://ytjx.gzhmu.edu.cn/',#遗体捐献纪念网站
url20:'https://jyw.gzhmu.edu.cn/',#就业指导中心
url21:'https://syjxzx.gzhmu.edu.cn/',#基础医学实验教学中心
url22:'https://tw.gzhmu.edu.cn/',#共青团广医委员会
url23:'https://jnzx.gzhmu.edu.cn/',#临床技能实验中心
url24:'https://sky.gzhmu.edu.cn/',#中国科学院广州生物医药与健康研究院联合生命科学学院
url25:'https://lib.gzhmu.edu.cn/',#图书馆
url26:'https://ggwsxy.gzhmu.edu.cn/',#公共卫生学院
url27:'https://bme.gzhmu.edu.cn/',#生物医学工程学院
url28:'https://wsgl.gzhmu.edu.cn/',#卫生管理学院
url29:'https://cgzx.gzhmu.edu.cn/',#招标采购
url30:'https://alumni.gzhmu.edu.cn/',#校友与基金
url31:'https://xxzx.gzhmu.edu.cn/',#信息与现代教育技术中心
url32:'https://yxy.gzhmu.edu.cn/',#药学院
url33:'https://rsc.gzhmu.edu.cn/',#人事处
url34:'https://jxjy.gzhmu.edu.cn/',#全科医学与继续教育学院
url35:'https://hlxy.gzhmu.edu.cn/',#护理学院
url36:'https://kysyzx.gzhmu.edu.cn/',#科研试验中心
url37:'https://sydwzx.gzhmu.edu.cn/',#动物实验中心
url38:'https://jcxy.gzhmu.edu.cn/',#基础医学院
url39:'https://xsc.gzhmu.edu.cn/',#学生工作处
url40:'https://das.gzhmu.edu.cn/',#档案室
url41:'https://majors.gzhmu.edu.cn/',#专业介绍
url42:'https://ygc.gzhmu.edu.cn/',#医院管理处
url43:'https://gzxi.cbpt.cnki.net/WKD/WebPublication/index.aspx?mid:gzxi',#学报
url44:'https://bwc.gzhmu.edu.cn/',#保卫处
url45:'https://president.gzhmu.edu.cn/',#校长信箱
url46:'https://jinyu.gzhmu.edu.cn/',#金域检验学院'''

namelist=re.findall("(\d+):'(.*)',#(.*)\s",str)
weblist={number:web for number,web,name in namelist}
for number,web,name in namelist:
    print(name+':'+number)


num=input('输入网站对应数字：')

webbrowser.open(weblist[num])
