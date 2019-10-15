import pandas
import numpy
filename=input("insert the path of the file to be processed, include its name at the end and please include .csv ")
y=pandas.read_csv(filename, sep=",", usecols=(3,4,10))

Source_Current=y["Source Current"].values
Gate_Voltage=y["Gate Voltage"].values
vg0=[]
vg10=[]
vg20=[]
vg30=[]
vg40=[]
vg50=[]
vg60=[]
vg70=[]
vg80=[]
vg90=[]
vg100=[]
for x in Gate_Voltage:
    if x>-1:
        vg0.append(x)
    elif x==-10:
        vg10.append(x)
    elif x==-20:
        vg20.append(x)
    elif x==-30:
        vg30.append(x)
    elif x==-40:
        vg40.append(x)
    elif x==-50:
        vg50.append(x)
    elif x==-60:
        vg60.append(x)
    elif x==-70:
        vg70.append(x)
    elif x==-80:
        vg80.append(x)
    elif x==-90:
        vg90.append(x)
    elif x==-100:
        vg100.append(x)

a=len(vg0)-1
b=len(vg0)+len(vg10)-1
c=len(vg0)+len(vg10)+len(vg20)-1
d=len(vg0)+len(vg10)+len(vg20)+len(vg30)-1
e=len(vg0)+len(vg10)+len(vg20)+len(vg30)+len(vg40)-1
f=len(vg0)+len(vg10)+len(vg20)+len(vg30)+len(vg40)-1+len(vg50)
g=len(vg0)+len(vg10)+len(vg20)+len(vg30)+len(vg40)-1+len(vg50)+len(vg60)
h=len(vg0)+len(vg10)+len(vg20)+len(vg30)+len(vg40)-1+len(vg50)+len(vg60)+len(vg70)
i=len(vg0)+len(vg10)+len(vg20)+len(vg30)+len(vg40)-1+len(vg50)+len(vg60)+len(vg70)+len(vg80)
j=len(vg0)+len(vg10)+len(vg20)+len(vg30)+len(vg40)-1+len(vg50)+len(vg60)+len(vg70)+len(vg90)+len(vg80)
k=len(vg0)+len(vg10)+len(vg20)+len(vg30)+len(vg40)-1+len(vg50)+len(vg60)+len(vg70)+len(vg90)+len(vg80)+len(vg100)

vg01=list(Source_Current[0:len(vg100)])
vg101=list(Source_Current[a:b])
vg1101=vg101[0:len(vg100)]
vg201=list(Source_Current[b:c])
vg2101=vg201[0:len(vg100)]
vg301=list(Source_Current[c:d])
vg3101=vg301[0:len(vg100)]
vg401=list(Source_Current[d:e])
vg4101=vg401[0:len(vg100)]
vg501=list(Source_Current[e:f])
vg5101=vg501[0:len(vg100)]
vg601=list(Source_Current[f:g])
vg6101=vg601[0:len(vg100)]
vg701=list(Source_Current[g:h])
vg7101=vg701[0:len(vg100)]
vg801=list(Source_Current[h:i])
vg8101=vg801[0:len(vg100)]
vg901=list(Source_Current[i:j])
vg9101=vg901[0:len(vg100)]
vg11z01=list(Source_Current[j:k])
vg11001=vg11z01[0:len(vg100)]
Source_Voltage=(y["Source Voltage"].values)[0:len(vg100)]
df=pandas.DataFrame({'VDS':Source_Voltage,'vg=0':vg01,'vg=-10':vg1101,'vg=-20':vg2101,'vg=-30':vg3101,'vg=-40':vg4101,'vg=-50':vg5101,'vg=-60':vg6101,'vg=-70':vg7101,'vg=-80':vg8101,'vg=-90':vg9101,'vg=negative one-hundred':vg11001})
pandas.set_option('display.max_columns', 90000)
df.to_csv('p-type_processed.csv',index=False)
print("the processed file should be in the same folder as this program")
