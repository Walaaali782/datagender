import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحديد المسار الكامل للملف
file_path = 'C:/Users/MO/Desktop/Gradution Pro/healthcare_dataset.csv'

# قراءة البيانات من ملف CSV
df = pd.read_csv(file_path)

# حساب متوسط القيم لكل عمود عدد
mean_values = df.mean(numeric_only=True)


# رسم بياني للخطوط (Line Plot)
plt.subplot(3, 1, 2)
for column in df.select_dtypes(include=['number']).columns:
    plt.plot(df[column], label=column)
plt.title('Line Plot of Numeric Columns')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()

# رسم بياني دائري (Pie Chart)
# plt.subplot(3, 1, 3)
# # استبدل 'ColumnName' باسم العمود الذي تريد استخدامه
# column_name = 'Test Results'  # استبدله باسم العمود المطلوب
# data = df[column_name].value_counts()
# plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
# plt.title(f'Distribution of {column_name}')

# # عرض جميع الرسوم البيانية
# plt.tight_layout()
# plt.show()


plt.figure(figsize=(8, 6))
sns.set(style="whitegrid")

# Create the count plot with specified palette
plot = sns.countplot(data=df, x='Gender', hue='Gender', palette='Oranges')

# Set the background color
sns.set(rc={'axes.facecolor':'lightblue', 'figure.facecolor':'lightblue'})
#Add a title by 
plt.title('Obsession Type by Gender')
# Add data labels
for p in plot.patches:
    plot.annotate(format(p.get_height(), '.0f'), 
                  (p.get_x() + p.get_width() / 2., p.get_height()), 
                  ha = 'center', va = 'center', 
                  xytext = (0, 10), 
                  textcoords = 'offset points')

# Show the plot
plt.show()
