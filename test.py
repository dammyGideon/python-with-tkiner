import tkinter as tk
from tkinter import * 
import pandas as pd
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from matplotlib import pyplot as plt
import seaborn as sns
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import seaborn as sns




EnergyCallCenter = pd.read_excel("EnergyCallCentre.xlsx")
print(EnergyCallCenter)
#Generating a sample from the dataset randomly
EnergyCallCenter_Sample = EnergyCallCenter.sample(n=100,random_state=8642)
# Viewing the sample data
print(EnergyCallCenter_Sample)
#Checking the columns in the sample data frame
EnergyCallCenter.columns
#Describing dataset and converting to a CSV file
Descriptivestat =EnergyCallCenter_Sample.describe().round()
Descriptivestat.to_csv('Descriptivestat.csv')

# Calculating number of call abandoned as a percentage of total call offered for more logical interpretation
EnergyCallCenter_Sample['Callabandoned%']= (EnergyCallCenter_Sample['CallsAbandoned']/EnergyCallCenter_Sample['CallsOffered'])*100

# Data Exploration: Vetical Bar Chart using mean and groupby
EnergyCallCenter_Sample.groupby(["VHT"])['Callabandoned%'].mean().plot.bar(color='red')
plt.xlabel('VHT Status')
plt.ylabel('Percentage of calls Offered abandoned(%)')
plt.show()

# Data Exploration: Vetical Bar Chart using mean and groupby
EnergyCallCenter_Sample.groupby(["Month"])['CallsOffered','CallsAbandoned'].mean().plot.bar(color=['Green','blue'])
plt.xlabel('Month')
plt.ylabel('Number of calls')
plt.show()

# Data Exploration: Vetical Bar Chart use mean and groupby
fig, ax = plt.subplots(figsize=(8,6))
EnergyCallCenter_Sample.boxplot(column=['CallsAbandoned'], by="VHT", ax=ax,)
plt.title('')
plt.xlabel('VHT Status')
plt.ylabel('Number of calls abandoned')
plt.show()

# Data Exploration: Scattered plots of number of agents and percentatge of calls abandoned with 'Month' and 'VHS status' used for grouging
sns.lmplot(x='Agents',y='Callabandoned%', data=EnergyCallCenter_Sample,ci=None,hue='Month',col='VHT')

# Data Exploration: Scattered plots of 'Average handle time' and 'percentatge of calls abandoned' with 'Time of the day' and 'VHS status' used for grouging
sns.lmplot(x='Avehandletime',y='Callabandoned%', data=EnergyCallCenter_Sample,ci=None,hue='ToD',col='VHT')

# Data Exploration: Horizontal bar chart of 'Time of the day' and 'percentatge of calls abandoned' compared an horizontal bar chart showng the 'Time of the day','Number of times VHT was and on and off' with 'Time of the day' and 'VHS status' used for grouging
import random

plt.subplot(2, 1, 1)
EnergyCallCenter_Sample.groupby(["ToD"])['Callabandoned%'].mean().plot.barh(color=(random.random(),random.random(),random.random()))
plt.xlabel('Percentage of calls Offered abandoned(%)')
plt.ylabel('Time of the Day')

plt.subplot(2, 1, 2)
EnergyCallCenter_Sample.groupby(["ToD"])['VHT'].value_counts().plot.barh(color=(random.random(),random.random(),random.random()))
plt.xlabel('Number of time VHT is on and off')
plt.ylabel('Time of the Day')
plt.show()

# Vertical barchart comparing 'Average Speed of Answer' and 'Percentage of calls abandoned'
EnergyCallCenter_Sample.groupby(["Month"])['ASA','Callabandoned%'].mean().plot.bar(color=['purple','pink'])
plt.xlabel('Month')
plt.ylabel('Value')
plt.show()

#Using Minimum as statistics

# Data Exploration: Vetical Bar Chart using mean and groupby
EnergyCallCenter_Sample.groupby(["VHT"])['Callabandoned%'].min().plot.bar(color='red')
plt.xlabel('VHT Status')
plt.ylabel('Percentage of calls Offered abandoned(%)')
plt.show()

# Data Exploration: Vetical Bar Chart using mean and groupby
EnergyCallCenter_Sample.groupby(["Month"])['CallsOffered','CallsAbandoned'].mean().plot.bar(color=['Green','blue'])
plt.xlabel('Month')
plt.ylabel('Number of calls')
plt.show()

# Data Exploration: Vetical Bar Chart use mean and groupby
fig, ax = plt.subplots(figsize=(8,6))
EnergyCallCenter_Sample.boxplot(column=['CallsAbandoned'], by="VHT", ax=ax,)
plt.title('')
plt.xlabel('VHT Status')
plt.ylabel('Number of calls abandoned')
plt.show()

# Data Exploration: Scattered plots of number of agents and percentatge of calls abandoned with 'Month' and 'VHS status' used for grouging
sns.lmplot(x='Agents',y='Callabandoned%', data=EnergyCallCenter_Sample,ci=None,hue='Month',col='VHT')

# Data Exploration: Scattered plots of 'Average handle time' and 'percentatge of calls abandoned' with 'Time of the day' and 'VHS status' used for grouging
sns.lmplot(x='Avehandletime',y='Callabandoned%', data=EnergyCallCenter_Sample,ci=None,hue='ToD',col='VHT')

# Data Exploration: Horizontal bar chart of 'Time of the day' and 'percentatge of calls abandoned' compared an horizontal bar chart showng the 'Time of the day','Number of times VHT was and on and off' with 'Time of the day' and 'VHS status' used for grouging
import random

plt.subplot(2, 1, 1)
EnergyCallCenter_Sample.groupby(["ToD"])['Callabandoned%'].mean().plot.barh(color=(random.random(),random.random(),random.random()))
plt.xlabel('Percentage of calls Offered abandoned(%)')
plt.ylabel('Time of the Day')

plt.subplot(2, 1, 2)
EnergyCallCenter_Sample.groupby(["ToD"])['VHT'].value_counts().plot.barh(color=(random.random(),random.random(),random.random()))
plt.xlabel('Number of time VHT is on and off')
plt.ylabel('Time of the Day')
plt.show()

# Vertical barchart comparing 'Average Speed of Answer' and 'Percentage of calls abandoned'
EnergyCallCenter_Sample.groupby(["Month"])['ASA','Callabandoned%'].mean().plot.bar(color=['purple','pink'])
plt.xlabel('Month')
plt.ylabel('Value')
plt.show()

EnergyCallCenter = pd.read_excel("EnergyCallCentre.xlsx")
pf = EnergyCallCenter.sample(n=100,random_state=8642)
pf['Callabandoned%']= (pf['CallsAbandoned']/pf['CallsOffered'])*100
           



# data that filled up the loop of radio button and select box
Months =("Oct-Nov","Feb-Mar","Dec-Jan","All")
Vht =   ("On","Off","All")
ToD =   ("morning", "afternoon","evening","All")
stats = ("Min","Max","Mean","value_counts")


buttons = [tk.SINGLE, tk.MULTIPLE]

groups_by=('Month','VHT','ToD',"None")
Dates = ["Agents","CallsOffered","CallsAbandoned",
         "CallsHandled","ASA","Avehandletime","Callabandoned%"]

class DatamangementApp(tk.Tk):
    #  constructor 
     def __init__(self):
        
         super().__init__()
         # frontend title page 
         self.title("EnergyCallCentre")
         #lenght of the screen  
         self.minsize(600,400)
         
         # output that show the details of the project   
         self.mylable = tk.Label(self,text="EnergyCallCenter",font=("Arial", 25))
         self.mylable.grid()
         
         self.group_1 = tk.LabelFrame(self, padx=15, pady=10,
                                      text="Dimension and Statistics",font=("Arial",15),
                                      bg="#48887b")
         self.group_1.grid(row=1,column=0,padx=10, pady=5)
         
         
         self.group_3 = tk.LabelFrame(self, padx=50, pady=50,
                                      text="Dimension and Statistics", font=("Arial",15 ), bg="#48887b")
         self.group_3.grid(row=1,column=2,padx=10, pady=5)
         
         
         self.group_2 = tk.LabelFrame(self, padx=15, pady=10,text="Fact",
                                      font=("Arial",15),
                                      bg="#48887b")
         self.group_2.grid(row=1,column=1,padx=10, pady=5)
         
       
      
         self.checked = tk.BooleanVar()
         self.checked.trace("w", self.mark_checked)
         self.radio = tk.StringVar()
         self.radio.set("1")
         self.radio.trace("w", self.mark_radio)
         menu = tk.Menu(self)
         submenu = tk.Menu(menu, tearoff=0)
         submenu.add_checkbutton(label="Add", onvalue=True,
         offvalue=False, variable=self.checked,)
         submenu.add_separator()
         submenu.add_radiobutton(label="Delete", value="1",
         variable=self.radio)
         menu.add_cascade(label="Menu", menu=submenu)
         menu.add_command(label="Quit", command=self.destroy)
         self.config(menu=menu)

                
      
      

         self.month_var()
         self.Vht_var()
         self.Tod_var()
         self.stats_var()
         self.group_var()
         
     
         self.collect_data()
       
         
      #    labels 
         self.month_label()
         self.vht_label()
         self.Tod_label()
         self.stats_label()
         self.group_label()
         
         self.select_box()
         self.Enter()
         
         self.filter_by_label()
         
         
     # function that uploads the   
     def mark_checked(self, *args):
         file = filedialog.askopenfile(mode='r', filetypes=[('csv', '*.xlsx',)])
        
         if file:
            filepath = os.path.abspath(file.name)
            result=pd.read_excel(filepath)
            
            print(result)
           

     def mark_radio(self, *args):
                pass
            

         
         
         
    #  filter by heading 
     def filter_by_label(self):
        self.filter_label = ttk.Label(self.group_1, text="Filter By", font=("Arial",10))
        self.filter_label.grid(row=0,columnspan=2)
        
     def month_var(self):
        #  self.label=ttk.Label(self.group_1).grid(row=0, column=0)
         self.combo = ttk.Combobox(self.group_1, values=Months)
         self.combo.grid(row=1,column=1, sticky=W)
         
        # lable for the month   
     def month_label(self):
           btn_submit = ttk.Label(self.group_1, text="Month")
           btn_submit.grid(row=1, column=0)
        #display month 
     def month_display(self, *args):
         
            month_detail = self.combo.get()
            dec_jan = pf[pf["Month"]==month_detail]
            if not len(dec_jan):
               msg = "Nothing was selected"
               mb.showinfo("Information", msg)
            subnet = dec_jan[["Agents","CallsOffered","CallsAbandoned","CallsHandled","ASA","Avehandletime"]]
            print(subnet)
            
     
     
     #vht display
     def Vht_var(self):
         self.label = ttk.Label(self, text="Energy Call Centre Evaluation System")
         self.combo_2 = ttk.Combobox(self.group_1, values=Vht)
         self.combo_2.grid(row=2,column=1,sticky=W, pady=10)
      #vht label    
     def vht_label(self):
           btn_submit = ttk.Label(self.group_1, text="VHT")
           btn_submit.grid(row=2, column=0)
           
         #vht display  
     def vht_display(self, *args):
            vht_detail = self.combo_2.get()
            vht_details = pf[pf["VHT"]==vht_detail]
            if not len(vht_details):
               msg = "Nothing was selected"
               mb.showinfo("Information", msg)

            subset= vht_details[["Agents","CallsOffered","CallsAbandoned","CallsHandled","ASA","Avehandletime"]]
            
            print(subset)
            
            #tod select box
     def Tod_var(self):
         self.label = ttk.Label(self, text="Energy Call Centre Evaluation System")
         self.combo_3 = ttk.Combobox(self.group_1, values=ToD)
         self.combo_3.grid(row=3,column=1,sticky=W, pady=10)
          #tod label box
     def Tod_label(self):
           btn_submit = ttk.Label(self.group_1, text="ToD")
           btn_submit.grid(row=3, column=0)
           # display box
     def Tod_display(self, *args):
            ToD_detail = self.combo_3.get()
            ToD_details = pf[pf["ToD"]==ToD_detail]
            if not len(ToD_details):
               msg = "Nothing was selected"
               mb.showinfo("Information", msg)

            subset= ToD_details[["Agents","CallsOffered","CallsAbandoned","CallsHandled","ASA","Avehandletime"]]
            
            print(subset)
              
   
     def group_var(self):
         self.label = ttk.Label(self, text="Energy Call Centre Evaluation System")
         self.combo_6 = ttk.Combobox(self.group_1, values=groups_by)
         self.combo_6.grid(row=1,column=2)
         
     def group_label(self):
           btn_submit = ttk.Label(self.group_1, text="Group By")
           btn_submit.grid(row=0, column=2, pady=20)
           
     def group_display(self, *args):
            ToD_detail = self.combo_5.get()
            ToD_details = pf[pf["ToD"]==ToD_detail]
            if not len(ToD_details):
               msg = "Nothing was selected"
               mb.showinfo("Information", msg)

            subset= ToD_details[["Agents","CallsOffered","CallsAbandoned","CallsHandled","ASA","Avehandletime"]]
            
            print(subset)
              

              
              
              
              
              
              
              
              #statics value
     def stats_var(self):
         self.label = ttk.Label(self, text="Energy Call Centre Evaluation System")
         self.combo_4 = ttk.Combobox(self.group_3, values=stats)
         self.combo_4.grid(row=1,column=0)
         #statics label
         
     def stats_label(self):
           btn_submit = ttk.Label(self.group_3, text="Select Statics")
           btn_submit.grid(row=0, column=0, pady=20)
           
        #   static fuction diplay  
     def stats_display(self, *args):
            ToD_detail = self.combo_4.get()
            ToD_details = pf[pf["ToD"]==ToD_detail]
            if not len(ToD_details):
               msg = "Nothing was selected"
               mb.showinfo("Information", msg)

            subset= ToD_details[["Agents","CallsOffered","CallsAbandoned","CallsHandled","ASA","Avehandletime"]]
            
            print(subset)                
                
             
     def month_statics(self):
         month_detail = self.combo.get() 
         group_status = self.combo_6.get()
           
          
         if month_detail:
                if month_detail :
                    if group_status == "Month":
                        msg = "Group by other options"
                        mb.showinfo("Information", msg)
             
                    selection = self.list.curselection()
                    facts=[self.list.get(i) for i in selection]
                    for x in range(len(facts)):
                        total_details = pf[(pf["Month"]==month_detail)]
            
                if facts[x] in pf.columns:  
                        fact_result=facts[x]
                        subnet=total_details[["Month","VHT","ToD","Agents",
                                            "CallsOffered","CallsAbandoned",
                                            "CallsHandled","ASA","Avehandletime","Callabandoned%"
                                            ]]
                        
                        if group_status in pf.columns:
                            
                                mean_result = self.combo_4.get()        
                                if mean_result =="Mean":
                                    subnet.groupby(f"{group_status}")[f"{fact_result}"].mean().plot.bar(color='red')
                                    plt.xlabel('VHT Status')
                                    plt.ylabel(f'Percentage of {fact_result}(%)')
                                    plt.show()
                                elif mean_result =="Min":
                                        subnet.groupby(f"{group_status}")[f"{fact_result}"].min().plot.bar(color='red')
                                        plt.xlabel('VHT Status')
                                        plt.ylabel(f'Percentage of {fact_result}(%)')
                                        plt.show()
                                elif mean_result == "Max":
                                        subnet.groupby(f"{group_status}")[f"{fact_result}"].max().plot.bar(color='red')
                                        plt.xlabel('VHT Status')
                                        plt.ylabel(f'Percentage of {fact_result}(%)')
                                        plt.show()
                                elif mean_result =="value_counts":
                                        msg = "Not Applicable"
                                        mb.showinfo("Information", msg)
        
                    
                
     def vht_statics(self):
           vht_detail   = self.combo_2.get()
           group_status = self.combo_6.get()
          
           if vht_detail:
                if group_status == "VHT":
                    msg = "Group by other options"
                    mb.showinfo("Information", msg)
                        
                selection = self.list.curselection()
                facts=[self.list.get(i) for i in selection]
                for x in range(len(facts)):
                                total_details = pf[(pf["VHT"]==vht_detail)]
                                
                if facts[x] in pf.columns:  
                                    fact_result=facts[x]
                                    subnet=total_details[["Month","VHT","ToD" ,"Agents",
                                                        "CallsOffered","CallsAbandoned",
                                                        "CallsHandled","ASA","Avehandletime","Callabandoned%"
                                                        ]]
                                    
                                    if group_status in pf.columns:
                                        
                                            mean_result = self.combo_4.get()        
                                            if mean_result =="Mean":
                                                subnet.groupby(f"{group_status}")[f"{fact_result}"].mean().plot.bar(color='red')
                                                plt.xlabel('VHT Status')
                                                plt.ylabel(f'Percentage of {fact_result}(%)')
                                                plt.show()
                                            elif mean_result =="Min":
                                                    subnet.groupby(f"{group_status}")[f"{fact_result}"].min().plot.bar(color='red')
                                                    plt.xlabel('VHT Status')
                                                    plt.ylabel(f'Percentage of {fact_result}(%)')
                                                    plt.show()
                                            elif mean_result == "Max":
                                                    subnet.groupby(f"{group_status}")[f"{fact_result}"].max().plot.bar(color='red')
                                                    plt.xlabel('VHT Status')
                                                    plt.ylabel(f'Percentage of {fact_result}(%)')
                                                    plt.show()
                                            elif mean_result =="value_counts":
                                                    msg = "Not Applicable"
                                                    mb.showinfo("Information", msg)

    
     def tod_statics(self): 
           tod_detail   = self.combo_3.get()
           group_status = self.combo_6.get()
          
           if tod_detail:
                if group_status == "ToD":
                    msg = "Group by other options"
                    mb.showinfo("Information", msg)
                        
                selection = self.list.curselection()
                facts=[self.list.get(i) for i in selection]
                for x in range(len(facts)):
                                total_details = pf[(pf["VHT"]==tod_detail)]
                                
                if facts[x] in pf.columns:  
                                    fact_result=facts[x]
                                    subnet=total_details[["Month","VHT","ToD" ,"Agents",
                                                        "CallsOffered","CallsAbandoned",
                                                        "CallsHandled","ASA","Avehandletime","Callabandoned%"
                                                        ]]
                                    
                                    if group_status in pf.columns:
                                        if group_status == "None":
                                            pass
                                        else:
                                            mean_result = self.combo_4.get()        
                                            if mean_result =="Mean":
                                                subnet.groupby(f"{group_status}")[f"{fact_result}"].mean().plot.bar(color='red')
                                                plt.xlabel('VHT Status')
                                                plt.ylabel(f'Percentage of {fact_result}(%)')
                                                plt.show()
                                            elif mean_result =="Min":
                                                    subnet.groupby(f"{group_status}")[f"{fact_result}"].min().plot.bar(color='red')
                                                    plt.xlabel('VHT Status')
                                                    plt.ylabel(f'Percentage of {fact_result}(%)')
                                                    plt.show()
                                            elif mean_result == "Max":
                                                    subnet.groupby(f"{group_status}")[f"{fact_result}"].max().plot.bar(color='red')
                                                    plt.xlabel('VHT Status')
                                                    plt.ylabel(f'Percentage of {fact_result}(%)')
                                                    plt.show()
                                            elif mean_result =="value_counts":
                                                    msg = "Not Applicable"
                                                    mb.showinfo("Information", msg)

            
     def equality(self):
            month_detail = self.combo.get()
            vht_detail   = self.combo_2.get()
            tod_detail   = self.combo_3.get()
            
            
            selection = self.list.curselection()
            facts=[self.list.get(i) for i in selection]
            for x in range(len(facts)):
                        total_details = pf[(pf["VHT"]==vht_detail) & (pf["Month"]==month_detail)
                                     & (pf["ToD"]==tod_detail)]
            if facts[x] in pf.columns:  
                        fact_result=facts[x]
                        subset=total_details[['Month','VHT','ToD',f'{fact_result}']]
                        
                        
                        mean_result = self.combo_4.get()        
                        if mean_result =="Mean":
                            result=subset[f'{fact_result}'].mean()
                            msg =f"The Mean is {round(result)}"
                            mb.showinfo("Information", msg)
                            
                        elif mean_result == "Min":
                            result=subset[f'{fact_result}'].min()
                            msg =f"The Minimum  is {round(result)}"
                            mb.showinfo("Information", msg)
                            
                        elif mean_result =="Max":
                            result=subset[f'{fact_result}'].mean()
                            msg =f"The Maximum  is {round(result)}"
                            mb.showinfo("Information", msg)
                         
                        elif mean_result =="value_counts":
                            msg = "Not Applicable"
                            mb.showinfo("Information", msg)
       
     def dual_entry(self,value_1,value_2):
          month_detail = value_1
          vht_detail   = value_2
          selection = self.list.curselection()
          facts=[self.list.get(i) for i in selection]
          for x in range(len(facts)):
                        total_details = pf[(pf["VHT"]==vht_detail) & (pf["Month"]==month_detail)]
          if facts[x] in pf.columns:  
                        fact_result=facts[x]
                        subset=total_details[['Month','VHT',f'{fact_result}']]
                        
                        
                        mean_result = self.combo_4.get()        
                        if mean_result =="Mean":
                            result=subset[f'{fact_result}'].mean()
                            msg =f"The Mean is {round(result)}"
                            mb.showinfo("Information", msg)
                            
                        elif mean_result == "Min":
                            result=subset[f'{fact_result}'].min()
                            msg =f"The Minimum  is {round(result)}"
                            mb.showinfo("Information", msg)
                            
                        elif mean_result =="Max":
                            result=subset[f'{fact_result}'].mean()
                            msg =f"The Maximum  is {round(result)}"
                            mb.showinfo("Information", msg)
                         
                        elif mean_result =="value_counts":
                            msg = "Not Applicable"
                            mb.showinfo("Information", msg)
     def single_entry(self,value):
          month_detail = value
          selection = self.list.curselection()
          facts=[self.list.get(i) for i in selection]
          for x in range(len(facts)):
                        total_details = pf[(pf["Month"]==month_detail)]
          if facts[x] in pf.columns:  
                        fact_result=facts[x]
                        subset=total_details[['Month','VHT',f'{fact_result}']]
                        
                        
                        mean_result = self.combo_4.get()        
                        if mean_result =="Mean":
                            result=subset[f'{fact_result}'].mean()
                            msg =f"The Mean is {round(result)}"
                            mb.showinfo("Information", msg)
                            
                        elif mean_result == "Min":
                            result=subset[f'{fact_result}'].min()
                            msg =f"The Minimum  is {round(result)}"
                            mb.showinfo("Information", msg)
                            
                        elif mean_result =="Max":
                            result=subset[f'{fact_result}'].mean()
                            msg =f"The Maximum  is {round(result)}"
                            mb.showinfo("Information", msg)
                         
                        elif mean_result =="value_counts":
                            msg = "Not Applicable"
                            mb.showinfo("Information", msg)
    

    # label names 
     def label_name_creation(self):
          selection = self.list.curselection()
          facts=[self.list.get(i) for i in selection]
          
                
     
     
     
         
     def select_box(self):
            self.list = tk.Listbox(self.group_2)
            self.list.insert(0, *Dates)
           
            self.list.grid(row=0,column=1,padx=40)
        
    
            selection = self.list.curselection()
            print([self.list.get(i) for i in selection])
            
            
            
    
    
     def Enter(self):
           btn_submit = ttk.Button(self.group_2, text="Enter",command=self.collect_data)
           btn_submit.grid(row=5,column=10)
           
             
           
     def collect_data(self):  
       month_result = self.combo.get()
       
              
       if month_result == "All":
                 pass
       else:
        if month_result =="Oct-Nov" or month_result == "Feb-Mar" or month_result =="Dec-Jan" :
            mean_result = self.combo_4.get()        
            if mean_result =="Mean":
               self.month_statics()
            elif mean_result =="Min":
                self.month_statics()
            elif mean_result == "Max":
                self.month_statics()
            elif mean_result =="value_counts":
                self.month_statics()
        
       vht_result = self.combo_2.get()
       if vht_result == "All":
                   pass
    
       else:
            if vht_result :
                
                    mean_result = self.combo_4.get()        
                    if mean_result =="Mean":
                        self.vht_statics()
                    elif mean_result =="Min":
                        self.vht_statics()
                    elif mean_result == "Max":
                        self.vht_statics()
                    elif mean_result =="value_counts":
                        self.vht_statics()
        
       tod_result =self.combo_3.get()
      
       if tod_result == "All":
                  pass
       else:
            if tod_result :
                    mean_result = self.combo_4.get()        
                    if mean_result =="Mean":
                            self.tod_statics()
                    elif mean_result =="Min":
                            self.tod_statics()
                    elif mean_result == "Max":
                            self.tod_statics()
                    elif mean_result =="value_counts":
                            self.tod_statics()
       
       if month_result and vht_result and tod_result :
           self.equality()
       elif month_result and vht_result :
           self.dual_entry(month_result,vht_result)
       elif month_result :
           self.single_entry(month_result)
           
           
       elif month_result =="All" and vht_result == "All" and tod_result :
            print("work")
       elif vht_result == "All"  and tod_result == "All" and month_result:
           print("iokay")
       elif tod_result =="All"   and month_result== "All" and vht_result:
           print("okay")
       elif month_result =="All" and vht_result and tod_result :
           print("urio")
       elif vht_result =="All" and tod_result and month_result:
           print('yor')
       elif tod_result =="All" and month_result and vht_result:
           print("euru")
       elif month_result and vht_result and tod_result :
           print("perfect")
      
       

if __name__ == "__main__":
 app = DatamangementApp()
 app.mainloop()
 
 
 
 

