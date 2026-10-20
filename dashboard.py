"""The Soloist: standalone mock dashboard. Synthetic data; not an AI model."""
import tkinter as tk

W, H = 800, 600
BG, CARD, WHITE, MUTED = '#1a1a2e', '#16213e', '#ffffff', '#a0aec0'
TEAL, PURPLE, AMBER, RED, BLUE = '#1d9e75', '#7c6cf8', '#f59e0b', '#e24b4a', '#378add'
metrics = [('Active Learners','142','+18',PURPLE),('Avg Completion','73%','+9pp',TEAL),('Sentiment Score','8.1/10','+0.6',AMBER),('Retention Rate','96%','+3pp',TEAL)]
learners = [('Arjun J.','ADHD',88,PURPLE),('Sofia R.','Dyslexia',62,TEAL),('Kai M.','Autism',95,AMBER),('Priya L.','ADHD',54,RED),('Tariq O.','Dyscalculia',38,BLUE)]
sentiment = [('Engagement',82,PURPLE),('Confidence',76,TEAL),('Belonging',70,BLUE),('Stress level',34,RED),('Mgr support',88,TEAL),('Accommodation',65,AMBER)]
alerts = [('!','Priya L. stalled 14+ days - check in',AMBER),('!','ADHD cohort session length down 22%',AMBER),('!','6 employees below accommodation threshold',RED),('*','Autism cohort +12pp on assessments',TEAL),('i','2 employees ready for next module',BLUE)]
outcomes = [('Task Completion','91%','+7pp',TEAL),('Python Projects','34','+11',PURPLE),('Avg Focus Session','38 min','-4m',AMBER),('Certifications','19','+8',TEAL)]
root=tk.Tk();root.title('Neurodivergent Learning & Sentiment Dashboard — The Soloist')
c=tk.Canvas(root,width=W,height=H,bg=BG,highlightthickness=0);c.pack()
def rect(x,y,w,h,fill): c.create_rectangle(x,y,x+w,y+h,fill=fill,outline='')
def txt(x,y,s,size=10,color=WHITE,weight='normal'):
    c.create_text(x,y,text=s,anchor='nw',fill=color,font=('Arial',size,weight))
def bar(x,y,w,pct,col):
    rect(x,y,w,10,'#2d3748');rect(x,y,w*min(max(pct,0),100)/100,10,col)
def panel(x,y,w,h,title):
    rect(x,y,w,h,CARD);txt(x+12,y+11,title,10,MUTED,'bold')
def draw():
    c.delete('all');rect(0,0,W,H,BG);rect(0,0,W,60,'#0f0f23')
    txt(20,12,'Neurodivergent Learning & Sentiment Dashboard',17,WHITE,'bold')
    txt(20,39,'The Soloist | Goa Institute of Management | SYNTHETIC DEMO',9,MUTED)
    txt(706,20,'● DEMO',11,TEAL,'bold')
    for i,(label,val,delta,col) in enumerate(metrics):
        x=20+i*194;panel(x,75,180,80,'');txt(x+11,85,label,10,MUTED);txt(x+11,106,val,20,WHITE,'bold');txt(x+11,139,delta+' vs prior qtr',9,col)
    panel(20,175,370,220,'LEARNER PROGRESS — Python Track')
    for i,(name,profile,pct,col) in enumerate(learners):
        y=213+i*35;txt(33,y,name,10);txt(33,y+15,profile,8,MUTED);bar(138,y+10,205,pct,col);txt(349,y+5,str(pct)+'%',9,col)
    panel(410,175,370,220,'SENTIMENT BREAKDOWN')
    for i,(label,pct,col) in enumerate(sentiment):
        y=215+i*29;txt(424,y,label,9,MUTED);bar(531,y+3,190,pct,col);txt(728,y,str(pct)+'%',9,col)
    panel(20,415,370,167,'ATTENTION SIGNALS')
    for i,(icon,msg,col) in enumerate(alerts):
        y=449+i*25;rect(32,y,20,19,col);txt(38,y+1,icon,10,'#000000','bold');txt(59,y+2,msg,9)
    panel(410,415,370,167,'WORKFORCE OUTCOMES')
    for i,(label,val,delta,col) in enumerate(outcomes):
        y=451+i*29;txt(424,y,label,10,MUTED);txt(640,y,val,12);txt(727,y,delta,9,col)
    rect(0,585,W,15,'#0f0f23');txt(20,585,'Press R to replay refresh | ESC to quit | Fictional examples only',8,MUTED)
def key(event):
    if event.keysym.lower()=='r':
        c.delete('all');rect(0,0,W,H,BG);txt(300,280,'Refreshing display...',16,TEAL,'bold');root.after(500,draw)
    elif event.keysym=='Escape':root.destroy()
root.bind('<Key>',key);draw()
if __name__=='__main__':root.mainloop()
