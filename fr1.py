from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


def random_forest(Headache1, Job_Awareness1, Academic_Pressure1, Vocal_Expression1,Unhealhty_Influence1, Workload1, Anxiety1, Physical_Health1,Relationship_at_Work1, Work_Stress1, Digital_Distraction1,Sleep_Hours1, Time_Pressure1, Financial_Pressure1,Tech_Obligations1):
    global list3
    
    data = pd.read_csv('Updated.csv')
    data.drop(['Unnamed: 0','Age','Gender','Class','Year','Weather','Seeking_Help','Faking','Self_Awareness','Screen_Time','Parental_Pressure'],axis=1,inplace=True)
    data.to_csv('Update1.csv')
    dp = pd.read_csv("Update1.csv")
    dp.columns.values
    features = dp.columns[1:16]
    X = dp[features]
    X 
    Y = dp['Result']
    Y
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)
    X_train
    Y_train
    regressor = RandomForestRegressor(n_estimators=20, random_state=0)
    regressor.fit(X_train,Y_train)
    Y.pred= regressor.predict(X_test)
    r2=r2_score(Y_test,Y.pred)
    print(r2)
    global a 
    a = regressor.predict([[Headache1, Job_Awareness1, Academic_Pressure1, Vocal_Expression1,Unhealhty_Influence1, Workload1, Anxiety1, Physical_Health1,Relationship_at_Work1, Work_Stress1, Digital_Distraction1,Sleep_Hours1, Time_Pressure1, Financial_Pressure1,Tech_Obligations1]])
    
    print(type(a))
    print(a)

def raise_frame(frame):
    frame.tkraise()

def fetch():
    Headache1 = Headache.get()
    Job_Awareness1 = Job_Awareness.get()
    Academic_Pressure1 = Academic_Pressure.get()
    Vocal_Expression1 = Vocal_Expression.get()
    Unhealhty_Influence1 = Unhealhty_Influence.get()
    Workload1 = Workload.get()
    Anxiety1 = Anxiety.get()
    Physical_Health1 = Physical_Health.get()
    Relationship_at_Work1 = Relationship_at_Work.get()
    Work_Stress1 = Work_Stress.get()
    Digital_Distraction1 = Digital_Distraction.get()
    Sleep_Hours1 = Sleep_Hours.get()
    Time_Pressure1 = Time_Pressure.get()
    Financial_Pressure1 = Financial_Pressure.get()
    Tech_Obligations1 = Tech_Obligations.get()
    pred = random_forest(Headache1, Job_Awareness1, Academic_Pressure1, Vocal_Expression1,Unhealhty_Influence1, Workload1, Anxiety1, Physical_Health1,Relationship_at_Work1, Work_Stress1, Digital_Distraction1,Sleep_Hours1, Time_Pressure1, Financial_Pressure1,Tech_Obligations1)

    show = Tk()
    show.geometry("850x500")
    show.config(bg="alice blue")
    show.resizable(False,True)
    show.title("Details")
    vary=80
    headlb=Label(show,text="Your Stress Score",font="Times 25 bold",bg="alice blue").grid(row=0,column=1,padx=200)
           
    #-------------------------------Label of the Table---------------------------------#
    
    lb1 = Label(show,text="Your stress level is : ",width=20,bd=5,bg="alice blue").place(x=2,y=50)
    lb2 = Label(show,text="Recommendation :",width=20,bd=5,bg="alice blue").place(x=2,y=200)

    if(a>=1.00 and a<=2.33):
        lb1 = Label(show,text="Low Stress",width=20,bd=5,bg="alice blue").place(x=2,y=80)
        lb2 = Label(show,text="* Stay Positive: Keep up the optimistic approch towards different situations.",width=60,bd=5,bg="alice blue").place(x=5,y=230) 
        lb3 = Label(show,text="* Eat a Balanced Diet: A poor diet can bring greater reactivity toward stress.",width=60,bd=5,bg="alice blue").place(x=5,y=260)
        lb4 = Label(show,text="* Make Time for Leisure Activities:Leisure activities can be a wonderful way to relieve stress.",width=72,bd=5,bg="alice blue").place(x=5,y=290)
        lb5 = Label(show,text="""* Cut Out Things That Add to Your Stress: Get rid of the things that are adding to your
        stress so you can experience more peace. """,width=68,bd=5,bg="alice blue").place(x=5,y=320)
        lb6 = Label(show,text="""* Exercise: follow a systematic exercise routine.""",width=40,bd=5,bg="alice blue").place(x=5,y=360)

                
    if(a>=2.34 and a<=3.67):
        lb1 = Label(show,text="Moderate Stress",width=20,bd=5,bg="alice blue").place(x=2,y=80)
        lb2 = Label(show,text="* Try yoga: Yoga brings together physical and mental disciplines which may help you achieve peacefulness of body and mind.",width=95,bd=5,bg="alice blue").place(x=5,y=230) 
        lb3 = Label(show,text="""* Enjoy Aromatherapy: whether you enjoy candles, diffusers, or body products, consider
        incorporating some aromatherapy into your day.""",width=66,bd=5,bg="alice blue").place(x=5,y=260)
        lb4 = Label(show,text="""* Laugh more: Laughter fires up and then cools down your stress response. So read some jokes, tell
        some jokes, watch a comedy or hang out with your funny friends.""",width=73,bd=5,bg="alice blue").place(x=5,y=300)
        lb5 = Label(show,text="""* Reduce Your Caffeine Intake: Caffeine is a stimulant found in coffee, tea, chocolate and energy
         drinks. High doses can increase anxiety.""",width=72,bd=5,bg="alice blue").place(x=5,y=340)
        lb6 = Label(show,text="""* Get musical and be creative: Listening to or playing music is a good stress reliever because it
        can provide a mental distraction.If music isn't one of your interests, turn your attention to
        another hobby you enjoy, such as gardening, sewing, sketching .""",width=70,bd=5,bg="alice blue").place(x=5,y=380)


    if(a>=3.68 and a<=5.00):
        lb1 = Label(show,text="High Stress",width=20,bd=5,bg="alice blue").place(x=2,y=80)
        lb2 = Label(show,text="* Seek counseling: Professional counselors or therapists can help you identify sources of your stress and learn new coping tools.",width=95,bd=5,bg="alice blue").place(x=5,y=230) 
        lb3 = Label(show,text="* Develop a Positive Self-Talk Habit: It's important to learn to talk to yourself in a more realistic manner and introspect.",width=88,bd=5,bg="alice blue").place(x=5,y=260)
        lb4 = Label(show,text="""* Meditate: Meditation can instill a sense of calm, peace and balance that can benefit both your
        emotional well-being and your overall health.""",width=72,bd=5,bg="alice blue").place(x=5,y=290)
        lb5 = Label(show,text="""* Connect with others: Reach out to family and friends and make social connections.Social contact
        is a good stress reliever because it can offer distraction""",width=75,bd=5,bg="alice blue").place(x=5,y=330)
        lb6 = Label(show,text="""* Get active: Any form of physical activity can act as a stress reliever. Even if you're not an
        athlete or you're out of shape, exercise can still be a good stress reliever.""",width=68,bd=5,bg="alice blue").place(x=5,y=370)

   
win=Tk()
win.title("Stress Analysis")
win.geometry("1000x500")


f0=Frame(win)
f0.config(bg="alice blue")
f1=Frame(win)
f1.config(bg="alice blue")
f2=Frame(win)
f2.config(bg="alice blue")
f3=Frame(win)
f3.config(bg="alice blue")
f4=Frame(win)
f4.config(bg="alice blue")
f5=Frame(win)
f5.config(bg="alice blue")
f6=Frame(win)
f6.config(bg="alice blue")
f7=Frame(win)
f7.config(bg="alice blue")
f8=Frame(win)
f8.config(bg="alice blue")
f9=Frame(win)
f9.config(bg="alice blue")
f10=Frame(win)
f10.config(bg="alice blue")
f11=Frame(win)
f11.config(bg="alice blue")
f12=Frame(win)
f12.config(bg="alice blue")
f13=Frame(win)
f13.config(bg="alice blue")
f14=Frame(win)
f14.config(bg="alice blue")
f15=Frame(win)
f15.config(bg="alice blue")

for frame in (f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15):
    frame.grid(row=0,column=0,sticky=N+S+E+W)
    
lb=Label(f0,text="STRESS ANALYSIS",font=("arial",30,"bold","underline","italic"),bg="alice blue").pack(anchor="w",padx=350,pady=12)
lb1=Label(f0,text='''Stress is called "THE INVISIBLE" as it is often overlooked but one of the major reason behind
deteriorating mental health is stress. It affects one's mental and physical well being.''',font=("arial",15,"italic"),bg="alice blue").pack(anchor="w",padx=5,pady=12)
lb2=Label(f0,text='• Answer carefully, You cannot jump back to the previous question.',font=("arial",15,"italic"),bg="alice blue").pack(anchor="w",padx=5,pady=12)
lb3=Label(f0,text='• Select the best suited option as per real life scenarios',font=("arial",15,"italic"),bg="alice blue").pack(anchor="w",padx=5,pady=12)
lb4=Label(f0,text='• Answer the questions with utmost honesty',font=("arial",15,"italic"),bg="alice blue").pack(anchor="w",padx=5,pady=12)
lb5=Label(f0,text= 'To test your stress level take up this test.',font=("arial",15,"italic"),bg="alice blue").pack(anchor="w",padx=5,pady=12)
btn=Button(f0,text="Start Test",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f1)).pack(anchor="w",padx=370,pady=12)




lb=Label(f1,text="""1.When a person is constantly shouting at you, your head starts aching very much.
On a general basis when you suffer from a headache, what symptoms most likely occur""",font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Headache=IntVar()
#var.set(1)
r1=Radiobutton(f1,text='''Just headache, nothing else''',padx=14,variable=Headache,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f1,text='''A pounding, throbbing pain and irritation due to light''',padx=14,variable=Headache,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f1,text='''Pain along with piercing pain behind the eye(s)''',padx=14,variable=Headache,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f1,text='''I usually have pain in the chest or bridge of the nose area as well''',padx=14,variable=Headache,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f1,text='''I usually go through more than one symptoms from the above options''',padx=14,variable=Headache,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f1,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f2)).pack(anchor="w",padx=400,pady=14)

lb=Label(f2,text='''2.You are new to a job, you’ve been here since a few months.Its a little different from your previous office,
the office culture and procedures and a little different.Your new boss has put you on a bigger assignment.
In this different situation, what will you do?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=12).pack(anchor="w")
Job_Awareness=IntVar()
#var.set(1)
r1=Radiobutton(f2,text='''Will you be able to understand all the different situations and expectations and
work your way through this different environment.''',font=("arial",14,"italic"),bg="alice blue",padx=14,variable=Job_Awareness,value=1,pady=5).pack(anchor="w")
r1=Radiobutton(f2,text='''Will you understand most tasks and ask for help from others or
try to understand yourself.''',padx=14,variable=Job_Awareness,value=2,font=("arial",14,"italic"),bg="alice blue",pady=5).pack(anchor="w")
r1=Radiobutton(f2,text='''Will you have difficulty with most tasks but you’ll be able to
ask for help from your colleagues.''',padx=14,variable=Job_Awareness,value=3,font=("arial",14,"italic"),bg="alice blue",pady=5).pack(anchor="w")
r1=Radiobutton(f2,text='''Will you not ask anyone but stay at the same job hoping you’ll
figure it out.''',padx=14,variable=Job_Awareness,value=4,font=("arial",14,"italic"),bg="alice blue",pady=5).pack(anchor="w")
r1=Radiobutton(f2,text='''will you leave the job.''',padx=14,variable=Job_Awareness,value=5,font=("arial",14,"italic"),bg="alice blue",pady=5).pack(anchor="w")
btn=Button(f2,text="Next ",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f3)).pack(anchor="w",padx=400)

lb=Label(f3,text='''3.Even after studying for long you failed a subject.Now you are putting in extra efforts for all the subjects.
Fear of failure to do well in studies in general makes you feel?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Academic_Pressure=IntVar()
#var.set(1)
r1=Radiobutton(f3,text="Motivated to do better",padx=14,variable=Academic_Pressure,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f3,text="Unpleasant but I recover from it in a healthy way.",padx=14,variable=Academic_Pressure,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f3,text="Put in the same effort and time as before.",padx=14,variable=Academic_Pressure,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f3,text="Confused as I am unable to judge myself.",padx=14,variable=Academic_Pressure,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f3,text="Really anxious and unable to cope up.",padx=14,variable=Academic_Pressure,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f3,text="Next ",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f4)).pack(anchor="w",pady=14,padx=400)
lb=Label(f4,text='''4.You have been having a really hard time lately, you feel very tired mentally and physically. You
come home from work/college/school one day and your mother just asks how your day has been.
What will you do in this situation?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Vocal_Expression=IntVar()
#var.set(1)
r1=Radiobutton(f4,text='Will you just tell her how you’ve been feeling,including everything and seek professional help.',padx=14,variable=Vocal_Expression,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f4,text='Will you open up a little about the underlying problems but not entirely at once.',padx=14,variable=Vocal_Expression,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w") 
r1=Radiobutton(f4,text="will you tell her that your day was shitty and talk to her a little.",padx=14,variable=Vocal_Expression,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f4,text="will you just reply something like “it was fine”.",padx=14,variable=Vocal_Expression,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f4,text="will you not say anything and go to the room.",padx=14,variable=Vocal_Expression,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f4,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f5)).pack(anchor="w",padx=400,pady=14)

lb=Label(f5,text='''5.You open your instagram/facebook account and see your friends posting their vacation pictures and
all of them look happy .Whereas you were at your home for the whole period of vacations.
What will be your first reaction after seeing them?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Unhealhty_Influence=IntVar()
#var.set(1)
r1=Radiobutton(f5,text="Not at all get affected by them as it was your own choice to be at home.",padx=14,variable=Unhealhty_Influence,value=1,font=("lucida",15),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f5,text="Like all of their pictures but with envy.",padx=14,variable=Unhealhty_Influence,value=2,font=("lucida",15),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f5,text="Get upset and let the pictures affect your whole day.",padx=14,variable=Unhealhty_Influence,value=3,font=("lucida",15),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f5,text="Get upset and pick a fight with them as they didnt ask you to join them.",padx=14,variable=Unhealhty_Influence,value=4,font=("lucida",15),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f5,text="Cringe on their back and try to stay happy with them in their happiness.",padx=14,variable=Unhealhty_Influence,value=5,font=("lucida",15),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f5,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f6)).pack(anchor="w",padx=400,pady=14)

lb=Label(f6,text='''6.Wanting to do many a things you take up more than you can handle at the moment.Do you neglect some
of the work taken by you when you feel you have a lot to do?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Workload=IntVar()
#var.set(1)
r1=Radiobutton(f6,text="I complete all the work that I take.",padx=14,variable=Workload,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f6,text='I tend not to drop out something, but then I prioritize and may leave the work at the least priority.',padx=14,variable=Workload,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f6,text="I drop the work sometimes when I feel it is too much to handle.",padx=14,variable=Workload,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f6,text="I drop off majority of the work I take.",padx=14,variable=Workload,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f6,text="I dont take up work at all as I have much to do already.",padx=14,variable=Workload,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f6,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f7)).pack(anchor="w",padx=400,pady=14)

lb=Label(f7,text='''7.You are very much worthy of a job but just before your interview a random person looks down at you
and start laughing at your resume. What will you do?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Anxiety=IntVar()
#var.set(1)
r1=Radiobutton(f7,text='Get a boost in your confidence from it and try to perform better in the interview.',padx=14,variable=Anxiety,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f7,text='Be a little bit nervous before the interview and gain your confidence back in the interview.',padx=14,variable=Anxiety,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f7,text="Not let anyone affect your self confidence.",padx=14,variable=Anxiety,value=3,font=("arial",14,"italic"),bg="alice blue").pack(anchor="w")
r1=Radiobutton(f7,text="Get a little bit affected by it and a little bit of nervousness creeps in.",padx=14,variable=Anxiety,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f7,text="Get completely rattled by the person and lose all your confidence.",padx=14,variable=Anxiety,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f7,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f8)).pack(anchor="w",padx=400,pady=14)

lb=Label(f8,text='8.If given an option to work out 4-5 days in a week or not working out at all,what will you do?',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Physical_Health=IntVar()
#var.set(1)
r1=Radiobutton(f8,text="I will be working out 6 days a week no matter what.",padx=14,variable=Physical_Health,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f8,text="If the time permits I will work out.",padx=14,variable=Physical_Health,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f8,text="I will work out 2-3 days in a week.",padx=14,variable=Physical_Health,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f8,text="I will rarely work out.",padx=14,variable=Physical_Health,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f8,text="I will sleep in that time.",padx=14,variable=Physical_Health,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f8,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f9)).pack(anchor="w",padx=400,pady=14)

lb=Label(f9,text='''9.Relationships amongst the friends/teachers/colleagues are most of the time under a lot of distress.
How often do you encounter such instances?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Relationship_at_Work=IntVar()
#var.set(1)
r1=Radiobutton(f9,text="Such things never happened with me.",padx=14,variable=Relationship_at_Work,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f9,text="Such situations can be handled on a personal understanding.",padx=14,variable=Relationship_at_Work,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f9,text='It may happen when there are different point of views that a little bit of distress in the relationships may come.',padx=14,variable=Relationship_at_Work,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f9,text="Many a times such situations arise which lead to quarrels.",padx=14,variable=Relationship_at_Work,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f9,text="I am in a fight almost all the time.",padx=14,variable=Relationship_at_Work,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f9,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f10)).pack(anchor="w",padx=400,pady=14)

lb=Label(f10,text='''10.Your company seems to be growing and doing better.Your company just got a lot of new assignments
and projects. Everyone has a lot of workload. How will you deal with this situation?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=12).pack(anchor="w")
Work_Stress=IntVar()
#var.set(1)
r1=Radiobutton(f10,text='''Will you deal with the stress at work in a healthy way and work your way through this difficult
times at the office.''',padx=14,variable=Work_Stress,value=1,font=("arial",14,"italic"),bg="alice blue",pady=7).pack(anchor="w")
r1=Radiobutton(f10,text='Will you deal with your stress on a surface level and try to work through things for time being.',padx=14,variable=Work_Stress,value=2,font=("arial",14,"italic"),bg="alice blue",pady=7).pack(anchor="w")
r1=Radiobutton(f10,text="Will you just keep working without working on dealing with your stress.",padx=14,variable=Work_Stress,value=3,font=("arial",14,"italic"),bg="alice blue",pady=7).pack(anchor="w")
r1=Radiobutton(f10,text='''Will you work on some assignments but not others and let this affect your efficiency and productivity
without dealing with the stress.''',padx=14,variable=Work_Stress,value=4,font=("arial",14,"italic"),bg="alice blue",pady=7).pack(anchor="w")
r1=Radiobutton(f10,text="Will you just stop working.",padx=14,variable=Work_Stress,value=5,font=("arial",14,"italic"),bg="alice blue",pady=7).pack(anchor="w")
btn=Button(f10,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f11)).pack(anchor="w",padx=400,pady=7)

lb=Label(f11,text='''11.After taking up a work, just after 5 minutes into it you are wanting to check up on your phone.
How often do you give up on the need to check the device?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Digital_Distraction=IntVar()
#var.set(1)
r1=Radiobutton(f11,text='I will first complete all the chores then if time permitts then use my device.',padx=14,variable=Digital_Distraction,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f11,text="I will first get the job done on the hand then use the device.",padx=14,variable=Digital_Distraction,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f11,text="I will try not to open it up unless the work is done.",padx=14,variable=Digital_Distraction,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f11,text="After fighting the urge for sometime I'll open it up.",padx=14,variable=Digital_Distraction,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f11,text="I will leave the work in between and dwell into the device at that instant itself",padx=14,variable=Digital_Distraction,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f11,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f12)).pack(anchor="w",padx=400,pady=14)

lb=Label(f12,text='''12.You are a student and you want everything in your day to day agenda from studies to friends
to playing games and working out. After involving in so many activities you are not able to keep
up with your sleeping schedule. How often do you get a good nights sleep?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Sleep_Hours=IntVar()
#var.set(1)
r1=Radiobutton(f12,text="Juggling between the activities and sleep on day to day basis.",padx=14,variable=Sleep_Hours,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f12,text="Leave out a few of the things to get sleep.",padx=14,variable=Sleep_Hours,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f12,text="Ration my sleep throughout the day.",padx=14,variable=Sleep_Hours,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f12,text="Complete my sleep on weekends.",padx=14,variable=Sleep_Hours,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f12,text="Not able to cope up with sleep.",padx=14,variable=Sleep_Hours,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f12,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f13)).pack(anchor="w",padx=400,pady=14)
lb=Label(f13,text='''13.You are to submit your project in a week. Your group is not working as per the requirement
and things are not going according to the deadline.How is this situation going to affect your completion
before or on the deadline?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Time_Pressure=IntVar()
#var.set(1)
r1=Radiobutton(f13,text="If no one listens to me will try to complete the project myself in the deadline.",padx=14,variable=Time_Pressure,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f13,text="Will try to convince everyone to start working as the deadline is coming near.",padx=14,variable=Time_Pressure,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f13,text="I will be working with the same amount of rigour.",padx=14,variable=Time_Pressure,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f13,text="Will delay the work a bit more but start working as the deadline comes near.",padx=14,variable=Time_Pressure,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f13,text="I will go with flow and procastinate.",padx=14,variable=Time_Pressure,value=5,font=("arial",14,"italic"),bg="alice blue").pack(anchor="w",pady=14)
btn=Button(f13,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f14)).pack(anchor="w",padx=400,pady=14)

lb=Label(f14,text='''14.Your father recently lost his job. He's looking for a source of income. You're in your final year
of your college and there is your farewell party after a week.Your father calls you explaining the situatuion.
What will you do?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Financial_Pressure=IntVar()
#var.set(1)
r1=Radiobutton(f14,text="""You completely understand the situation and offer a helping hand by telling him you'll be taking up an
internship to help in sustaining the household.""",padx=14,variable=Financial_Pressure,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f14,text="You tell him about the party and ask him for more money so that you'll be able to enjoy the last year of college.",padx=14,variable=Financial_Pressure,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f14,text="You act infront of him as you are still in the college and it is his duty to help you.",padx=14,variable=Financial_Pressure,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f14,text="You fight with him that he is not fulfilling his responsibilities and start a ruckus.",padx=14,variable=Financial_Pressure,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f14,text="You quietly take out some money from his wallet and add your savings and enjoy your party.",padx=14,variable=Financial_Pressure,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f14,text="Next",bd=10,width=10,relief="raised",bg="green yellow",command=lambda:raise_frame(f15)).pack(anchor="w",padx=400,pady=12)

lb=Label(f15,text='''15.Due to work/personal commitments you are not able to let go of the devices and are surrounded by
them all the time. How often does that happen that youre not able to let go of them?''',font=("arial",14,"bold","italic"),bg="alice blue",pady=16).pack(anchor="w")
Tech_Obligations=IntVar()
#var.set(1)
r1=Radiobutton(f15,text="There is no such obligation to use technology all the time.",padx=14,variable=Tech_Obligations,value=1,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f15,text='There are times when i have to use the devices to complete some tasks.',padx=14,variable=Tech_Obligations,value=2,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f15,text="I am using it occasionaly to help me complete the work as well at glance at social media.",padx=14,variable=Tech_Obligations,value=3,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f15,text="I am more often surrounded with devices.",padx=14,variable=Tech_Obligations,value=4,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
r1=Radiobutton(f15,text="If given an option i could use devices in my sleep.",padx=14,variable=Tech_Obligations,value=5,font=("arial",14,"italic"),bg="alice blue",pady=14).pack(anchor="w")
btn=Button(f15,text="Show Result",bd=10,width=10,relief="raised",bg="green yellow",command=fetch).pack(anchor="w",padx=400,pady=14)

raise_frame(f0)
win.mainloop()
