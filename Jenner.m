%In excel use CTRL+Shift+S then select csv to save as a csv file.
%This is approximated.
%save csv as | voltage (V) | current (A) | power (W) | with headers.
filename =input('Please type the path of the csv file to use: ','s');
b=importdata(filename); %Importing the columns from the csv file.
a=b.data;
area=input('Please input the area in cm^2: ');
V=a(1:length(a)); %Voltage
A=a(length(a)+1:2*length(a)); %Current
W=a(2*length(a)+1:3*length(a)); %Power
c=polyfit(V,A,9999); %Polynomial fit to approximately estimate Jsc and its slope.
q = polyder(c);
Jscslope=q(end);
Jsc1=c(10000);
Jsc=1000*(Jsc1/area);
b=polyfit(A,V,199); %Polynomial fit to approximately estimate Voc and its slope.
i=polyder(b);
Vocslope=i(end);
Voc=b(200);

Pmax=min(W); %Max power
FF=Pmax/(Jsc1*Voc); %Field factor
PCE=abs(Pmax*1000/area); %PCE
z=find(W==min(W),1); %This and the next two lines is to find the Jmp and Vmp.
Jmp=A(z);
Vmp=V(z);


fprintf('The Area is %2.8f cm^2.\n',area) %All fprintf lines print the info.
fprintf('The Field Factor is %2.8f. \n',FF)
fprintf('Jsc (Current Density) is %2.8f mA/cm^2. \n',Jsc)
fprintf('The Jsc slope is %2.8f. \n',Jscslope)
fprintf('The Voc slope is %2.8f. \n',Vocslope)
fprintf('Voc is %2.8f V\n',Voc)
fprintf('The maximum power output is %2.8f mW. \n',abs(1000*Pmax))
fprintf('Jmp is %2.8f mA. \n',abs(1000*Jmp))
fprintf('Vmp is %2.8f V. \n',abs(Vmp))
fprintf('PCE is %2.8f%% \n',PCE)

plot(V,(A/area)) %The following lines plot the data.
line([0 0], ylim, 'color','k') %y-axis
line(xlim,[0 0], 'color','k') %x-axis
title('Voltage vs. Current Density')
xlabel('Voltage(V)')
ylabel('Current Density (J)')