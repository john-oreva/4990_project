import matplotlib.pyplot as plt


labels = ['AI Knowledge', 'Other Knowledge']
sizes = [1, 99] 
colors = ['skyblue', 'lightgrey']
explode = (0.1, 0)  


plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Financial Jobs Requiring AI Knowledge')
plt.show()
