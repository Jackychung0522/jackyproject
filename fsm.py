from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    #def is_going_to_restart(self, event):
    #    text = event.message.text
     #   return text.lower() == 'restart'
    def is_going_to_age(self, event):
        text = event.message.text
        return text.lower() == '想要'
    
        
    

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "離開"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"
    def is_going_to_beginner(self, event):
        text = event.message.text
        return text.lower() =='初學者'
    def is_going_to_medium(self, event):
        text = event.message.text
        return text.lower() =='中級'
    def is_going_to_highlevel(self, event):
        text = event.message.text
        return text.lower() =='高手'
    def is_going_to_bserve(self, event):
        text = event.message.text
        return text.lower() =='發球'
    def is_going_to_bfinish(self, event):
        text = event.message.text
        return text.lower() =='學會了'
    def is_going_to_mserve(self, event):
        text = event.message.text
        return text.lower() =='發球'
    def is_going_to_mfinish(self, event):
        text = event.message.text
        return text.lower() =='學會了'
    def is_going_to_hserve(self, event):
        text = event.message.text
        return text.lower() =='發球'
    def is_going_to_hfinish(self, event):
        text = event.message.text
        return text.lower() =='學會了'
    def is_going_to_bserved(self, event):
        text = event.message.text
        return text.lower() =='接發球'
    def is_going_to_mserved(self, event):
        text = event.message.text
        return text.lower() =='接發球'
    def is_going_to_hserved(self, event):
        text = event.message.text
        return text.lower() =='接發球'
    def is_going_to_bkiller(self, event):
        text = event.message.text
        return text.lower() =='必殺技'
    def is_going_to_mkiller(self, event):
        text = event.message.text
        return text.lower() =='必殺技'
    def is_going_to_hkiller(self, event):
        text = event.message.text
        return text.lower() =='必殺技'
    def is_going_to_bservedtop(self, event):
        text = event.message.text
        return text.lower() =='上旋'
    def is_going_to_bservedunder(self, event):
        text = event.message.text
        return text.lower() =='下旋'
    def is_going_to_bservedside(self, event):
        text = event.message.text
        return text.lower() =='側旋'
    def is_going_to_mservedtop(self, event):
        text = event.message.text
        return text.lower() =='上旋'
    def is_going_to_mservedunder(self, event):
        text = event.message.text
        return text.lower() =='下旋'
    def is_going_to_mservedside(self, event):
        text = event.message.text
        return text.lower() =='側旋'
    def is_going_to_hservedtop(self, event):
        text = event.message.text
        return text.lower() =='上旋'
    def is_going_to_hservedunder(self, event):
        text = event.message.text
        return text.lower() =='下旋'
    def is_going_to_hservedside(self, event):
        text = event.message.text
        return text.lower() =='側旋'


    

    
    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "您已經離開囉如果要繼續請輸入任意文字")
        self.go_back(event)
    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_enter_age(self, event):
        print("I'm entering age")
        text='你覺得你的等級在哪裡勒?'
        btn = [
                    MessageTemplateAction(
                        label = '初學者',
                        text ='初學者'
                    ),
                    MessageTemplateAction(
                        label = '中級',
                        text = '中級'
                    ),
                    MessageTemplateAction(
                        label = '高手',
                        text ='高手'
                    ),


                ]
        send_button_message(event.reply_token,text, btn)
        #send_text_message(event.reply_token,'請輸入您的等級(＂初學者＂，＂中級＂或＂高手＂)')
    def on_enter_beginner(self, event):
        print("I'm entering beginner")
        text ='歡迎您來到桌球世界，今天想從哪裡開始學呢？'
        btn = [
                    MessageTemplateAction(
                        label = '發球',
                        text ='發球'
                    ),
                    MessageTemplateAction(
                        label = '接發球',
                        text = '接發球'
                    ),
                    MessageTemplateAction(
                        label = '必殺技',
                        text ='必殺技'
                    ),

                ]
        send_button_message(event.reply_token,text, btn)
        #send_text_message(event.reply_token,'歡迎您來到桌球世界，今天想從哪裡開始學呢？（請輸入＂發球＂，＂接發球＂或是"必殺技"）')
    def on_enter_medium(self, event):
        print("I'm entering medium")
        text='看來你打過一段時間了呢，今天想加強什麼呢？'
        btn = [
                    MessageTemplateAction(
                        label = '發球',
                        text ='發球'
                    ),
                    MessageTemplateAction(
                        label = '接發球',
                        text = '接發球'
                    ),
                    MessageTemplateAction(
                        label = '必殺技',
                        text ='必殺技'
                    ),

                ]
        send_button_message(event.reply_token,text, btn)
        #send_text_message(event.reply_token,'看來你打過一段時間了呢，今天想加強什麼呢？（請輸入＂發球＂，＂接發球＂或是"必殺技"）')
    def on_enter_highlevel(self, event):
        print("I'm entering highlevel")
        text='唉唷看來你滿強的喔，今天想還想讓什麼更強？'
        btn = [
                    MessageTemplateAction(
                        label = '發球',
                        text ='發球'
                    ),
                    MessageTemplateAction(
                        label = '接發球',
                        text = '接發球'
                    ),
                    MessageTemplateAction(
                        label = '必殺技',
                        text ='必殺技'
                    ),

                ]
        send_button_message(event.reply_token,text, btn)
        #send_text_message(event.reply_token,'唉唷看來你滿強的喔，今天想還想讓什麼更強？（請輸入＂發球＂，＂接發球＂或是"必殺技"）')
    def on_enter_bserve(self, event):
        print("I'm entering bserve")
        send_text_message(event.reply_token,'發球嗎,既然你是初學者,今天來教你個側旋好了  https://www.youtube.com/watch?v=mruG2VKlRuA   學會請打 "學會了"')
    def on_enter_bfinish(self, event):
        print("I'm entering bfinish")
        text='恭喜你學到新技能，還想要學什麼呢?'
        btn = [
                    MessageTemplateAction(
                        label = '發球',
                        text ='發球'
                    ),
                    MessageTemplateAction(
                        label = '接發球',
                        text = '接發球'
                    ),
                    MessageTemplateAction(
                        label = '必殺技',
                        text ='必殺技'
                    ),
                    MessageTemplateAction(
                        label = '離開',
                        text ='離開'
                    ),


                ]
        send_button_message(event.reply_token,text, btn)
        #send_text_message(event.reply_token,'恭喜你學到新技能，還想要學什麼呢?(請輸入＂發球＂，＂接發球＂或是"必殺技",如果要休息的話請輸入 "")')
    def on_enter_mserve(self, event):
        print("I'm entering mserve")
        send_text_message(event.reply_token,'發球嗎,既然你是中級玩家,今天來教你個下蹲好了  https://www.youtube.com/watch?v=SLox-awCVCE 學會請打 "學會了"')
    def on_enter_mfinish(self, event):
        print("I'm entering mfinish")
        text='恭喜你學到新技能，還想要學什麼呢?'
        btn = [
                    MessageTemplateAction(
                        label = '發球',
                        text ='發球'
                    ),
                    MessageTemplateAction(
                        label = '接發球',
                        text = '接發球'
                    ),
                    MessageTemplateAction(
                        label = '必殺技',
                        text ='必殺技'
                    ),
                    MessageTemplateAction(
                        label = '離開',
                        text ='離開'
                    ),


                ]
        send_button_message(event.reply_token,text, btn)
        #send_text_message(event.reply_token,'恭喜你學到新技能，還想要學什麼呢?(請輸入＂發球＂，＂接發球＂或是"必殺技",如果要休息的話請輸入 "離開")')
    def on_enter_hserve(self, event):
        print("I'm entering hserve")
        send_text_message(event.reply_token,'發球嗎,既然你是高手玩家,今天來教你個逆側旋好了  https://www.youtube.com/watch?v=K_XnnDNRPeo&t=412s 學會請打 "學會了"')
    def on_enter_hfinish(self, event):
        print("I'm entering hfinish")
        text='恭喜你學到新技能，還想要學什麼呢?'
        btn = [
                    MessageTemplateAction(
                        label = '發球',
                        text ='發球'
                    ),
                    MessageTemplateAction(
                        label = '接發球',
                        text = '接發球'
                    ),
                    MessageTemplateAction(
                        label = '必殺技',
                        text ='必殺技'
                    ),
                    MessageTemplateAction(
                        label = '離開',
                        text ='離開'
                    ),


                ]
        send_button_message(event.reply_token,text, btn)
        #send_text_message(event.reply_token,'恭喜你學到新技能，還想要學什麼呢?(請輸入＂發球＂，＂接發球＂或是"必殺技",如果要休息的話請輸入 "離開")')
    def on_enter_bserved(self, event):
        print("I'm entering bserved")
        text='接發球嗎!?你遇到哪種球不太會接?'
        btn = [
                    MessageTemplateAction(
                        label = '上旋',
                        text ='上旋'
                    ),
                    MessageTemplateAction(
                        label = '下旋',
                        text = '下旋'
                    ),
                    MessageTemplateAction(
                        label = '側旋',
                        text ='側旋'
                    ),

                ]
        send_button_message(event.reply_token,text, btn)
    def on_enter_hserved(self, event):
        print("I'm entering hserved")
        text='接發球嗎!?你遇到哪種球不太會接?'
        btn = [
                    MessageTemplateAction(
                        label = '上旋',
                        text ='上旋'
                    ),
                    MessageTemplateAction(
                        label = '下旋',
                        text = '下旋'
                    ),
                    MessageTemplateAction(
                        label = '側旋',
                        text ='側旋'
                    ),

                ]
        send_button_message(event.reply_token,text, btn)
    def on_enter_mserved(self, event):
        print("I'm entering mserved")
        text='接發球嗎!?你遇到哪種球不太會接?'
        btn = [
                    MessageTemplateAction(
                        label = '上旋',
                        text ='上旋'
                    ),
                    MessageTemplateAction(
                        label = '下旋',
                        text = '下旋'
                    ),
                    MessageTemplateAction(
                        label = '側旋',
                        text ='側旋'
                    ),

                ]
        send_button_message(event.reply_token,text, btn)
    def on_enter_bservedtop(self, event):
        print("I'm entering bservedtop")
        send_text_message(event.reply_token,'上旋嗎，初級的話就是"反手推球"或是"正手攻球" 看看這個影片 https://www.youtube.com/watch?v=e76Mq2CWsmg 學會的話打"學會了"')
    def on_enter_mservedtop(self, event):
        print("I'm entering mservedtop")
        send_text_message(event.reply_token,'上旋嗎，中等程度的我們可以直接正手拉球,反手彈球給質量,這樣才會是主動方!! 看看這個影片 https://www.youtube.com/watch?v=5Lm5hmFAjOc&list=PLww3rcJxeCkFZpX8yCcz9BV9W91Whg0l6&index=18 https://www.youtube.com/watch?v=bS2-T28sEkQ 學會的話打"學會了"')
    def on_enter_hservedtop(self, event):
        print("I'm entering hservedtop")
        send_text_message(event.reply_token,'上旋嗎，高手的話直接側砍,上旋變側下,對方直接不知道回去該怎麼接好!只是這個技術很吃手感喔^^ https://www.youtube.com/watch?v=XmHS3EmC_MQ  學會的話打"學會了"')
    def on_enter_bservedunder(self, event):
        print("I'm entering bservedunder")
        send_text_message(event.reply_token,'下旋嗎?初級的話我們可以使用擺短的技術唷!看看這個影片 https://www.youtube.com/watch?v=JYRrk1kK2G0 學會的話打"學會了"')
    def on_enter_mservedunder(self, event):
        print("I'm entering mservedunder")
        send_text_message(event.reply_token,'下旋嗎?中等程度的話我們可以使用切球銜接正手拉的技術喔,第一顆不一定要給到很有質量這樣也可以減少接發球的失誤!看看這個影片 https://www.youtube.com/watch?v=1Mt7E8SRvXA 學會的話打"學會了"')
    def on_enter_hservedunder(self, event):
        print("I'm entering hservedunder")
        send_text_message(event.reply_token,'下旋嗎?高手的話我覺得可以直接爆擰了,我們看看這個影片 https://www.youtube.com/watch?v=6Nm-fVDKsSc 學會的話打"學會了"')
    def on_enter_bservedside(self, event):
        print("I'm entering bservedside")
        send_text_message(event.reply_token,'側旋嗎?初級的話我們可以藉由調整拍面來抑制球往旁邊的旋轉 看看這個影片 https://www.youtube.com/watch?v=b7j8CtP90f8 學會的話打"學會了"')
    def on_enter_mservedside(self, event):
        print("I'm entering mservedside")
        send_text_message(event.reply_token,'側旋嗎?中等程度的話我們可以藉由拉球的摩擦去止住側旋的旋轉 看看這個影片 https://www.youtube.com/watch?v=iPjP27VATa0 學會的話打"學會了"')
    def on_enter_hservedside(self, event):
        print("I'm entering hservedside")
        send_text_message(event.reply_token,'側旋嗎?高手的話我覺得可以直接側身爆拉了 看看這個影片 https://www.youtube.com/watch?v=rJ956YY7d20 學會的話打"學會了"')
    def on_enter_bkiller(self, event):
        print("I'm entering bkiller")
        send_text_message(event.reply_token,'初級必殺技，把球從網子旁邊打進去，這樣球一定比網子低，對手很難去接這個球呢 來看看這個影片: https://www.youtube.com/watch?v=7ngGvgyCIbU"學會了"')
    def on_enter_mkiller(self, event):
        print("I'm entering mkiller")
        send_text_message(event.reply_token,'中級必殺技，左右開弓，在腳跑不到的時候很好用，對手以為你來不及的時候突然一版回去!來看看這個影片:https://www.youtube.com/watch?v=HTJapimz9XA,學會的話打"學會了"')
    def on_enter_hkiller(self, event):
        print("I'm entering hkiller")
        send_text_message(event.reply_token,'高手必殺技，直接殺完繞整個球桌回來再把球打進，對手直接嚇到不知所措 來看看怎麼打: https://www.youtube.com/watch?v=QBrzu0wgNi8"學會了"')
    def on_exit_state1(self,event):
        print("Leaving state1")
    def on_exit_state2(self,event):
        print("Leaving state2")
    def on_exit_restart(self,event):
        print("Leaving restart")
    def on_exit_age(self,event):
        print("Leaving age")
    def on_exit_beginner(self,event):
        print("Leaving beginner")
    def on_exit_medium(self,event):
        print("Leaving medium")
    def on_exit_highlevel(self,event):
        print("Leaving highlevel")
    def on_exit_bserve(self,event):
        print("Leaving bserve")
    def on_exit_bfinish(self,event):
        print("Leaving bfinish")
    def on_exit_mfinish(self,event):
        print("Leaving mfinish")
    def on_exit_mserve(self,event):
        print("Leaving mserve")
    def on_exit_hserve(self,event):
        print("Leaving hserve")
    def on_exit_hfinish(self,event):
        print("Leaving hfinish")
    def on_exit_mserved(self,event):
        print("Leaving mserved")
    def on_exit_hserved(self,event):
        print("Leaving hserved")
    def on_exit_bserved(self,event):
        print("Leaving bserved")
    def on_exit_bkiller(self,event):
        print("Leaving bkiller")
    def on_exit_mkiller(self,event):
        print("Leaving mkiller")
    def on_exit_hkiller(self,event):
        print("Leaving hkiller")




