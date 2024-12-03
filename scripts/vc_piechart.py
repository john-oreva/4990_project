import matplotlib.pyplot as plt


categories = ['Generative AI', 'Biotech/Healthcare AI', 'Autonomous Driving', 'AI Infrastructure', 'Others']
funding_distribution = [35, 25, 15, 15, 10]  

plt.figure(figsize=(8, 8))
plt.pie(funding_distribution, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20c.colors)
plt.title('AI Funding Distribution in Canada (2024)', fontsize=14)
plt.show()
