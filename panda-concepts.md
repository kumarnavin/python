import pandas as pd

<pre>
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
pd.Series(data=my_list)
pd.Series(data=my_list,index=labels)
pd.Series(my_list,labels)
pd.Series(arr,labels)
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])                                   
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])                                   
ser1 + ser2
</pre>

<pre>
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
df.columns
df.index
df['new'] = df['W'] + df['Y'] — add columns
df.drop('new',axis=1) — does not drop columns inplace
df.drop('new',axis=1,inplace=True) — forcibly
df.drop('E',axis=0) — X-axis
df.loc['A'] — locate a row or column
df.loc[['A','B'],['W','Y']] — Selecting subset of rows and columns
</pre>

## Conditionals
<pre>
df[df>0]
df[df['W']>0]
df[df['W']>0][‘Y’,’X’]
df[(df['W']>0) & (df['Y'] > 1)] — multiple conditions
df.reset_index()

Set new index:
newind = 'CA NY WY OR CO'.split()
df['States'] = newind
df.set_index('States')
df.set_index('States',inplace=True)


# Multiple index; Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df.loc['G1']
df.loc['G1'].loc[1]
df.index.names = ['Group','Num']
df.index.names
df.xs('G1') — grab the cross-section
</pre>

<pre>
df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})
df.dropna()
df.dropna(axis=1)
df.dropna(thresh=2)
df.fillna(value='FILL VALUE')
df['A'].fillna(value=df['A'].mean())
</pre>

<pre>
by_comp = df.groupby("Company")
by_comp.describe()
by_comp.describe().transpose()
by_comp.describe().transpose()['GOOG']
</pre>

## Concatenation
<pre>
pd.concat([df1,df2,df3])
pd.concat([df1,df2,df3],axis=1)
pd.merge(left,right,how='inner',on='key')
pd.merge(left, right, on=['key1', 'key2'])
left.join(right)
left.join(right, how='outer')
</pre>

<pre>
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
df.pivot_table(values='D',index=['A', 'B'],columns=['C'])
</pre>

## Data input and output
<pre>
df = pd.read_csv('example')
df.to_csv('example',index=False)
pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
</pre>

<pre>
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('data', engine)
sql_df = pd.read_sql('data',con=engine)
</pre>

<pre>
sal = pd.read_csv('Salaries.csv')
sal.head(2)
Id	EmployeeName	JobTitle	BasePay	OvertimePay	OtherPay	Benefits	TotalPay	TotalPayBenefits	Year	Notes	Agency	Status
0	1	NATHANIEL FORD	GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY	167411.18	0.00	400184.25	NaN	567595.43	567595.43	2011	NaN	San Francisco	NaN
1	2	GARY JIMENEZ	CAPTAIN III (POLICE DEPARTMENT)	155966.02	245131.88	137811.38	NaN	538909.28	538909.28	2011	NaN	San Francisco	NaN

sal.info()
sal['BasePay'].mean()
sal['OvertimePay'].max()
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName']
sal.groupby('Year').mean()['BasePay']
sal['JobTitle'].nunique() — ** How many unique job titles are there? **
sal['JobTitle'].value_counts().head(5) — ** How many unique job titles are there? **
sal.groupby('JobTitle').count().sort_values(by='EmployeeName',ascending=False).head(5) —** What are the top 5 most common jobs? **
sal['JobTitle'].value_counts().head(5)
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1) —How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) 
sum(sal['JobTitle'].apply(lambda x: str(x).lower().__contains__('chief'))) —How many people have the word Chief in their job title?
</pre>

<pre>
def chief_match(s):
    if 'chief' in s.lower():
        return True
    else:
        return False
sum(sal['JobTitle'].apply(lambda s: chief_match(s)))

sal['lenth'] = sal['JobTitle'].apply(lambda a: len(a))
sal[['lenth','TotalPayBenefits']].corr() —Bonus: Is there a correlation between length of the Job Title string and Salary?
</pre>

## Filter Expressions

<pre>
Filter data based on column: newdf = df[(df.origin == "JFK") & (df.carrier == "B6")]
Filter based on query: newdf = df.query('origin == "JFK" & carrier == "B6"')
Filter using loc function: newdf = df.loc[(df.origin == "JFK") & (df.carrier == "B6")]
Filter by row and column position: df.iloc[1:5,:5] #Second to Fifth row, first 5 columns
loc considers rows based on index labels. Whereas iloc considers rows based on position in the index so it only takes integers. 
Filter based on row position and column names: df.loc[df.index[0:5],["origin","dest"]]
Filter on multiple values: newdf = df[df.origin.isin(["JFK", "LGA"])]
Select rows where column value does not match: newdf = df.loc[(df.origin != "JFK") & (df.carrier == "B6")]
Negate the whole condition: newdf = df[~((df.origin == "JFK") & (df.carrier == "B6"))]
Select non-missing data: newdf = df[df.origin.notnull()]
Filter based on string length: df[df['var1'].str.len()>3]
Filter based on contains: df[df['var1'].str.contains('A|B')]
Rename a column: df.rename(columns={'var1':'var 1'}, inplace = True)
Lambda to filter: l1 = list(filter(lambda x: x["origin"] == 'JFK' and x["carrier"] == 'B6', lst_df))
newdf = df[df.apply(lambda x: x["origin"] == 'JFK' and x["carrier"] == 'B6', axis=1)]
What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) 
ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

Awesome site: https://www.listendata.com/2019/06/pandas-read-csv.html

</pre>
