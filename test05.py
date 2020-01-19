'''
问卷调查
'''
import easygui as G
import sys

questions =(
[
	{
		'question' : '你更喜欢下面哪个游戏？',
		'title' : '游戏倾向',
		'choices' : ['dota2', 'LOL']
	},
	{
		'question' : '你更喜欢下面哪个类型游戏？',
		'title' : '游戏类型倾向',
		'choices' : ['MMORPG', 'STG']
	}	
])
	
def ShowRes(res):
	res_str = ''
	for resitem in res:
		res_str += ('问题：' + resitem['question'] + '\n'
			+ '标题：' + resitem['title'] + '\n'
			+ '可选项：' + str(resitem['choices']) + '\n'
			+ '选择：' + resitem['selected'] + '\n')
		res_str += '-----------------------------------------\n'
	return res_str

def Questionnaire(questions):	
		
	G.msgbox('开始游戏调查问卷！', '开始')
	
	for question in questions:
		msg = question['question']
		title = question['title']
		choices = question['choices']
		choice = G.choicebox(msg, title, choices)
		question['selected'] = str(choice)
	G.msgbox('您以为完成本次问卷调查的所有问题！')
	msg = '是否列出本次调查问卷详细情况？'
	if G.ccbox(msg):
		G.msgbox(ShowRes(questions), '结果')
	else:
		sys.exit(0)


Questionnaire(questions)
	

