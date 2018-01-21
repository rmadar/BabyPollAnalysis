# Disable warnings
import warnings
warnings.filterwarnings('ignore')

# Basic tools
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt
import matplotlib        as mpl
import matplotlib.dates  as mdates

print('------------')
print('Tool version: ')
print(' - matplotlib : ' + str(mpl.__version__))
print(' - pandas     : ' + str(pd .__version__))
print(' - numpy      : ' + str(np .__version__))
print('------------')

# Plot settings
mpl.rcParams['legend.frameon'  ] = False
mpl.rcParams['legend.fontsize' ] = 'xx-large'
mpl.rcParams['xtick.labelsize' ] = 16
mpl.rcParams['ytick.labelsize' ] = 16
mpl.rcParams['axes.titlesize'  ] = 18
mpl.rcParams['axes.labelsize'  ] = 18
mpl.rcParams['lines.linewidth' ] = 2.5
mpl.rcParams['lines.markersize'] = 10
figure_size=(7,5)
png_dpi=200



# Load the data
featureName = ['stamp','YourName','date','time','gender','weight','size','name','HairAmount','HairColor','HairStyle','Sign']
mydata = pd.read_csv('Responses.csv', names=featureName, parse_dates=[['date', 'time']])
mydata = mydata[1:]
print('\nSize of the dataset: {}'.format(len(mydata)))

# Making binary sex column
binary_sex = mydata['gender']
binary_sex = [int('boy' in s) for s in binary_sex]
mydata['gender'] = binary_sex

# Adding time difference with expected delivery time (14 Oct - 12h)
mydata['dt']     = pd.to_datetime(mydata['date_time']) - pd.to_datetime('10-14-2017 12:00:00')
mydata['dtresp'] = pd.to_datetime(mydata['stamp'])     - pd.to_datetime('09-02-2017 09:00:00')
mydata['date']   = pd.to_datetime(mydata['date_time']).dt.date
mydata['hour']   = pd.to_datetime(mydata['date_time']).dt.hour
mydata['minute'] = pd.to_datetime(mydata['date_time']).dt.minute

# Adding answer time as date
mydata['stamp'] = pd.to_datetime(mydata['stamp'])
mydata.sort_values('stamp',inplace=True)

# Re-arrange the columns
old_cols = mydata.columns.tolist()
new_cols = [old_cols[1]] + old_cols[len(old_cols)-3:len(old_cols)] + [old_cols[0]] + old_cols[2:len(old_cols)-3]
mydata   = mydata[new_cols]

# Final conversions & printing
mydata = mydata.convert_objects(convert_numeric=True)
print( mydata.head() )



# Gender
plt.figure(figsize=figure_size)
plt.hist(mydata['gender'], bins=(-0.3,0.3,0.7,1.3) )
plt.xlim(-0.5,1.5)
plt.xticks([0,0.5,1],['girl','','boy'])
plt.axvline(x=1.0, color='black', linewidth=5.0)
plt.tight_layout()
plt.savefig('gender-distribution.png', dpi=png_dpi)

# Size
plt.figure(figsize=figure_size)
plt.hist(mydata['size'], bins=15, range=(35,65))
plt.xlabel('Size (cm)')
plt.axvline(x=53.0, color='black', linewidth=5.0)
plt.tight_layout()
plt.savefig('size-distribution.png', dpi=png_dpi)

# Weight
plt.figure(figsize=figure_size)
plt.hist(mydata['weight'], bins=15, range=(2,5))
plt.xlabel('Weight (kg)')
plt.axvline(x=3.040, color='black', linewidth=5.0)
plt.tight_layout()
plt.savefig('weight-distribution.png', dpi=png_dpi)

# Hair Amount
plt.figure(figsize=figure_size)
plt.hist(mydata['HairAmount'], bins=5, range=(0.5,5.5))
plt.xticks([1,1.5,2,3,5],['bold','','','','well equiped'])
plt.axvline(x=3, color='black', linewidth=5.0)
plt.tight_layout()
plt.savefig('hairamount-distribution.png', dpi=png_dpi)

# Hair Color
plt.figure(figsize=figure_size)
plt.hist(mydata['HairColor'], bins=5, range=(0.5,5.5))
plt.xticks([1,1.5,2,3,5],['blond','','','','dark'])
plt.axvline(x=2, color='black', linewidth=5.0)
plt.tight_layout()
plt.savefig('haircolor-distribution.png', dpi=png_dpi)

# Hair Style
plt.figure(figsize=figure_size)
plt.hist(mydata['HairStyle'], bins=5, range=(0.5,5.5))
plt.xticks([1,1.5,2,3,5],['straight','','','','curly'])
plt.axvline(x=1, color='black', linewidth=5.0)
plt.tight_layout()
plt.savefig('hairstyle-distribution.png', dpi=png_dpi)

