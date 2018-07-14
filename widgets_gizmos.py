#Widgets and Gizmos

#Weight of Widgets and Gizmos.
widg_weig=75
giz_weig=112

#Get the number of widgets and gizmos
widg_no=int(input('Number of widgets:'))
giz_no=int(input('Number of gizmos:'))
#Calculate the total weight
total_weig= widg_weig*widg_no + giz_weig*giz_no
#print the output
print('Total weight of the order is %d' %total_weig)
