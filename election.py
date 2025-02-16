import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "/mnt/data/indian-election-cleaned.csv"
df = pd.read_csv(file_path)

# 1. Voter Turnout Percentage
df['voter_turnout'] = (df['totvotpoll'] / df['electors']) * 100
plt.figure(figsize=(10, 6))
sns.histplot(df['voter_turnout'], bins=20, kde=True, color='blue')
plt.title('Voter Turnout Distribution')
plt.xlabel('Voter Turnout (%)')
plt.ylabel('Frequency')
plt.savefig("voter_turnout_distribution.png")
plt.show()

# 2. Winning Party Trend
plt.figure(figsize=(12, 6))
winning_party_counts = df['partyname'].value_counts().head(10)  # Top 10 parties
sns.barplot(x=winning_party_counts.index, y=winning_party_counts.values, palette='coolwarm')
plt.xticks(rotation=45)
plt.title('Top 10 Winning Parties')
plt.xlabel('Party')
plt.ylabel('Number of Wins')
plt.savefig("winning_parties.png")
plt.show()

# 3. Top 5 States by Voter Turnout
state_turnout = df.groupby('st_name')['voter_turnout'].mean().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=state_turnout.index, y=state_turnout.values, palette='viridis')
plt.title('Top 5 States by Voter Turnout')
plt.xlabel('State')
plt.ylabel('Average Voter Turnout (%)')
plt.savefig("top_states_voter_turnout.png")
plt.show()

# 4. Gender Representation
plt.figure(figsize=(6, 6))
gender_counts = df['cand_sex'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightblue', 'pink'], startangle=90)
plt.title('Gender Representation of Candidates')
plt.savefig("gender_representation.png")
plt.show()

# 5. Winning Margin Distribution
df['winning_margin'] = df.groupby('pc_name')['totvotpoll'].diff().fillna(0).abs()
plt.figure(figsize=(10, 6))
sns.histplot(df['winning_margin'], bins=20, kde=True, color='green')
plt.title('Winning Margin Distribution')
plt.xlabel('Winning Margin (Votes)')
plt.ylabel('Frequency')
plt.savefig("winning_margin_distribution.png")
plt.show()

import pandas as pd
import numpy as np
# Load the dirty dataset
file_path = "indian_election_dataset.csv"
df = pd.read_csv(file_path)
# 1. Handling NULL Values
print("Missing values before:")
print(df.isnull().sum())
df.fillna({'pc_type': 'Unknown', 'cand_sex': 'Unknown'}, inplace=True)
df.dropna(inplace=True)  # Dropping remaining rows with NULLs
print("Missing values after:")
print(df.isnull().sum())

Missing values before:
st_name        3587
year           3686
pc_no          3590
pc_name        3538
pc_type       11366
cand_name      3613
cand_sex       4194
partyname      3576
partyabbre     3563
totvotpoll     3573
electors       3744
dtype: int64
Missing values after:
st_name       0
year          0
pc_no         0
pc_name       0
pc_type       0
cand_name     0
cand_sex      0
partyname     0
partyabbre    0
totvotpoll    0
electors      0
dtype: int64

# 2. Removing Duplicates
print("Duplicates before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates after:", df.duplicated().sum())

Duplicates before: 70
Duplicates after: 0

# 3. Standardizing Data Formats
df['partyname'] = df['partyname'].str.replace("_", " ").str.title()
df['pc_name'] = df['pc_name'].str.title()
df['st_name'] = df['st_name'].str.title()

# 4. Correcting Inconsistent Data
df['cand_sex'] = df['cand_sex'].replace({
    'M': 'Male', 'MALE': 'Male', 'F': 'Female', 'FEMALE': 'Female'
})

# 5. Data Type Conversion
df['totvotpoll'] = pd.to_numeric(df['totvotpoll'], errors='coerce')
df['electors'] = pd.to_numeric(df['electors'], errors='coerce')

# Final Check
print("Final Data Types:")
print(df.dtypes)
print("Cleaned Dataset Preview:")
print(df.head())

Final Data Types:
st_name        object
year          float64
pc_no         float64
pc_name        object
pc_type        object
cand_name      object
cand_sex       object
partyname      object
partyabbre     object
totvotpoll    float64
electors      float64
dtype: object
Cleaned Dataset Preview:
                      st_name    year  pc_no                    pc_name  \
1   Andaman & Nicobar Islands  1977.0    1.0  Andaman & Nicobar Islands   
4   Andaman & Nicobar Islands  1980.0    1.0  Andaman & Nicobar Islands   
6   Andaman & Nicobar Islands  1980.0    1.0  Andaman & Nicobar Islands   
7   Andaman & Nicobar Islands  1980.0    1.0  Andaman & Nicobar Islands   
10  Andaman & Nicobar Islands  1980.0    1.0  Andaman & Nicobar Islands   

   pc_type           cand_name cand_sex                           partyname  \
1      GEN   Manoranjan Bhakta     Male            Indian National Congress   
4      GEN         Kannu Chemy     Male                        Independents   
6      GEN  Rajender Lall Saha  Unknown               Janta Party (Secular)   
...
4         IND       405.0   96084.0  
6      JNP(S)       717.0   96084.0  
7         IND      1123.0   96084.0  
10        CPM     16014.0   96084.0  
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...

# Save the cleaned dataset
cleaned_file_path = "indian_election_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)
