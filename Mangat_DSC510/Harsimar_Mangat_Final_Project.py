{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import scipy.stats as stats\n",
    "from sklearn import linear_model\n",
    "import statsmodels.api as sm\n",
    "import statsmodels.formula.api as smf\n",
    "from statsmodels import datasets\n",
    "import seaborn as sns\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['hotel', 'is_canceled', 'lead_time', 'arrival_date_year',\n",
       "       'arrival_date_month', 'arrival_date_week_number',\n",
       "       'arrival_date_day_of_month', 'stays_in_weekend_nights',\n",
       "       'stays_in_week_nights', 'adults', 'children', 'babies', 'meal',\n",
       "       'country', 'market_segment', 'distribution_channel',\n",
       "       'is_repeated_guest', 'previous_cancellations',\n",
       "       'previous_bookings_not_canceled', 'reserved_room_type',\n",
       "       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',\n",
       "       'company', 'days_in_waiting_list', 'customer_type', 'adr',\n",
       "       'required_car_parking_spaces', 'total_of_special_requests',\n",
       "       'reservation_status', 'reservation_status_date'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Load csv file into dataframe\n",
    "df=pd.read_csv(r'C:\\Users\\hsman\\OneDrive\\Documents\\hotel_bookings.csv')\n",
    "#list out all columns\n",
    "df.columns\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Check-Out': 1, 'Canceled': 2, 'No-Show': 3}"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create dictionary for conversion of STR MNTH value into INT MNTH value\n",
    "d={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,\n",
    "   'October':10,'November':11,'December':12}\n",
    "df['arrival_date_month']=df['arrival_date_month'].map(d)\n",
    "\n",
    "#Create dictionary for conversion of reservation status\n",
    "d1={'Check-Out':1,'Canceled':2,'No-Show':3}\n",
    "df['reservation_status']=df['reservation_status'].map(d1)\n",
    "d1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0.00918222, 0.005697  , 0.00405859, 0.00342438, 0.00269627,\n",
       "        0.00231786, 0.00225765, 0.00157914, 0.00122475, 0.00103727,\n",
       "        0.00104943, 0.000827  , 0.00060208, 0.00034472, 0.000287  ]),\n",
       " array([-10.        ,  17.33333333,  44.66666667,  72.        ,\n",
       "         99.33333333, 126.66666667, 154.        , 181.33333333,\n",
       "        208.66666667, 236.        , 263.33333333, 290.66666667,\n",
       "        318.        , 345.33333333, 372.66666667, 400.        ]),\n",
       " <a list of 15 Patch objects>)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Hist 1 - Variable Lead Time\n",
    "x=df['lead_time']\n",
    "plt.hist(x,15,range=[-10,400],density=1,edgecolor='k',align='mid')\n",
    "#plt.axvline(df['lead_time'].mean(),color='k',linestyle='dashed',linewidth=1)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    119390.000000\n",
       "mean        104.011416\n",
       "std         106.863097\n",
       "min           0.000000\n",
       "25%          18.000000\n",
       "50%          69.000000\n",
       "75%         160.000000\n",
       "max         737.000000\n",
       "Name: lead_time, dtype: float64"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Descriptive Statistics for Lead Time\n",
    "df['lead_time'].describe()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Median is 69.0\n",
      "The Mode is 0    0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"The Median is\",df['lead_time'].median())\n",
    "print(\"The Mode is\", df['lead_time'].mode())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "xt=df[df['lead_time'] < 100]\n",
    "xtt=xt['lead_time']\n",
    "plt.hist(xtt)\n",
    "\n",
    "xtt.mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([ 1316.,  4665.,  6274., 13943., 12921., 16112., 12604., 11552.,\n",
       "         9217.,  7249.,  5135.,  3963.,  3250.,  1903.,  1977.]),\n",
       " array([ 20.,  32.,  44.,  56.,  68.,  80.,  92., 104., 116., 128., 140.,\n",
       "        152., 164., 176., 188., 200.]),\n",
       " <a list of 15 Patch objects>)"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Hist 2 - Average Daily Rate\n",
    "x11=df[df['adr'] > 20]\n",
    "\n",
    "x1=x11['adr']\n",
    "plt.hist(x1,15,range=[20,200],edgecolor='k',align='mid')\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    119390.000000\n",
       "mean        101.831122\n",
       "std          50.535790\n",
       "min          -6.380000\n",
       "25%          69.290000\n",
       "50%          94.575000\n",
       "75%         126.000000\n",
       "max        5400.000000\n",
       "Name: adr, dtype: float64"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Descriptive Statistics for ADR\n",
    "df['adr'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Median is 94.575\n",
      "The Mode is 0    62.0\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(\"The Median is\",df['adr'].median())\n",
    "print(\"The Mode is\", df['adr'].mode())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'lead_time')"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_sample=df.sample(500)\n",
    "x1=df_sample['adr']\n",
    "y1=df_sample['lead_time']\n",
    "plt.scatter(x1,y1)\n",
    "plt.xlabel('adr')\n",
    "plt.ylabel('lead_time')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2200.63400417  -463.29102852]\n",
      " [ -463.29102852 11898.360204  ]]\n"
     ]
    }
   ],
   "source": [
    "#Covariance\n",
    "data=np.array([x1,y1])\n",
    "covMatrix=np.cov(data,bias=True)\n",
    "print (covMatrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2200.63400417  -463.29102852]\n",
      " [ -463.29102852 11898.360204  ]]\n",
      "The pearsons Coeffecient is: -0.09053915239819718\n"
     ]
    }
   ],
   "source": [
    "#Pearson Coeffecient\n",
    "x1=df_sample['adr']\n",
    "y1=df_sample['lead_time']\n",
    "data=np.array([x1,y1])\n",
    "covMatrix=np.cov(data,bias=True)\n",
    "print (covMatrix)\n",
    "print(\"The pearsons Coeffecient is:\", np.corrcoef(x1,y1)[1,0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, '# of special requests')"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Scatter Plot: # of Special Requests to Stays in Week Nights\n",
    "x1=df['stays_in_week_nights']\n",
    "y1=df['total_of_special_requests']\n",
    "plt.scatter(x1,y1)\n",
    "plt.xlabel('stays in week nights')\n",
    "plt.ylabel('# of special requests')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[3.64152349 0.10316552]\n",
      " [0.10316552 0.62852407]]\n"
     ]
    }
   ],
   "source": [
    "#Covariance\n",
    "data=np.array([x1,y1])\n",
    "covMatrix=np.cov(data,bias=True)\n",
    "print (covMatrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.06819178170957262"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Pearson Coeffecient\n",
    "x1=df['stays_in_week_nights']\n",
    "y1=df['total_of_special_requests']\n",
    "np.corrcoef(x1,y1)[1,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([ 7966., 10661., 11857., 13772., 12719., 17153., 13609., 13094.,\n",
       "         9824.,  8735.]),\n",
       " array([ 1. ,  6.2, 11.4, 16.6, 21.8, 27. , 32.2, 37.4, 42.6, 47.8, 53. ]),\n",
       " <a list of 10 Patch objects>)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Hist 3 - Arrival Date Week #\n",
    "x2=df['arrival_date_week_number']\n",
    "plt.hist(x2,edgecolor='k',align='mid')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([11536., 11913., 11682., 11261., 11760., 12486., 11851., 11205.,\n",
       "        12109., 13587.]),\n",
       " array([ 1.,  4.,  7., 10., 13., 16., 19., 22., 25., 28., 31.]),\n",
       " <a list of 10 Patch objects>)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Hist 4 - Arrival Date Day of Month\n",
    "x3=df['arrival_date_day_of_month']\n",
    "plt.hist(x3,10,edgecolor='k',align='mid')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([  403.,     0.,     0., 23027.,     0.,     0., 89680.,     0.,\n",
       "            0.,  6202.]),\n",
       " array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3. ]),\n",
       " <a list of 10 Patch objects>)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Hist 5 - # of Adults\n",
    "x4=df['adults']\n",
    "plt.hist(x4,range=[0,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([75166.,     0.,     0.,     0.,     0., 43017.,     0.,     0.,\n",
       "            0.,  1207.]),\n",
       " array([1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. ]),\n",
       " <a list of 10 Patch objects>)"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Histogram - Reservation Status\n",
    "x5=df['reservation_status']\n",
    "plt.hist(x5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([7.0318e+04, 0.0000e+00, 3.3226e+04, 0.0000e+00, 1.2969e+04,\n",
       "        0.0000e+00, 2.4970e+03, 0.0000e+00, 3.4000e+02, 4.0000e+01]),\n",
       " array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. ]),\n",
       " <a list of 10 Patch objects>)"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Histogram - Total of special requests\n",
    "x6=df['total_of_special_requests']\n",
    "plt.hist(x6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    119390.000000\n",
       "mean          0.571363\n",
       "std           0.792798\n",
       "min           0.000000\n",
       "25%           0.000000\n",
       "50%           0.000000\n",
       "75%           1.000000\n",
       "max           5.000000\n",
       "Name: total_of_special_requests, dtype: float64"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Descriptive Statistics for special requests\n",
    "df['total_of_special_requests'].describe()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x1ad5ce6fa60>]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Look at what months have the highest bookings\n",
    "ax=df.groupby('arrival_date_month').count()[['adr']]\n",
    "plt.plot(ax)\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.0, 500.0)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#SCATTER PLOT FOR ARRIVAL BY MONTH WITH ADR\n",
    "x=df['arrival_date_month']\n",
    "y=df['adr']\n",
    "plt.scatter(x,y)\n",
    "plt.ylim(0,500)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[   9.55184386   12.38782086]\n",
      " [  12.38782086 2553.84470883]]\n"
     ]
    }
   ],
   "source": [
    "#Covariance Calculation for variables arrival_date_month & adr\n",
    "data=np.array([x,y])\n",
    "covMatrix=np.cov(data,bias=True)\n",
    "print (covMatrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([3.7955e+04, 5.5942e+04, 2.0640e+04, 2.5280e+03, 8.8700e+02,\n",
       "        1.0920e+03, 6.9000e+01, 1.2000e+02, 2.0000e+01, 9.1000e+01]),\n",
       " array([ 0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20.]),\n",
       " <a list of 10 Patch objects>)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Hist  - Stay in Week Nights\n",
    "x6=df['stays_in_week_nights']\n",
    "plt.hist(x6,10,range=[0,20], edgecolor='k')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    119390.000000\n",
       "mean          2.500302\n",
       "std           1.908286\n",
       "min           0.000000\n",
       "25%           1.000000\n",
       "50%           2.000000\n",
       "75%           3.000000\n",
       "max          50.000000\n",
       "Name: stays_in_week_nights, dtype: float64"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Descriptive Statistics for special requests\n",
    "df['stays_in_week_nights'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.33554049 0.10277385]\n",
      " [0.10277385 3.64152349]]\n"
     ]
    }
   ],
   "source": [
    "x10=df['adults']\n",
    "y10=df['stays_in_week_nights']\n",
    "plt.scatter(x10,y10)\n",
    "plt.xlim(0,7)\n",
    "plt.show()\n",
    "\n",
    "#Covariance Calculation for adults and stay in week nights\n",
    "data=np.array([x10,y10])\n",
    "covMatrix=np.cov(data,bias=True)\n",
    "print (covMatrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Pareto Distribution Arrival Date Month\n",
    "import matplotlib.pyplot as plt\n",
    "a, m = 3., 2.  # shape and mode\n",
    "s= df['adr'] \n",
    "count, bins, _ = plt.hist(s, 100, density=True)\n",
    "fit = a*m**a / bins**(a+1)\n",
    "plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')\n",
    "plt.xlim(0,1000)\n",
    "plt.ylim(0,0.010)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 0, 'stays in week night')"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_1=np.sort(df['stays_in_week_nights'])\n",
    "n=x.size\n",
    "y=np.arange(1,n+1)/n\n",
    "plt.scatter(x=x_1,y=y)\n",
    "plt.xlim(0,50)\n",
    "plt.xlabel('stays in week night')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 0, 'average daily rate')"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#CDF\n",
    "x=np.sort(df['adr'])\n",
    "n=x.size\n",
    "y=np.arange(1,n+1)/n\n",
    "plt.scatter(x=x,y=y)\n",
    "plt.xlim(0,500)\n",
    "plt.xlabel('average daily rate')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0.00088089, 0.00646916, 0.01035987, 0.00833034, 0.0042985 ,\n",
       "        0.00213002, 0.00111998, 0.00061132, 0.00028662, 0.00011537]),\n",
       " array([ 11. ,  39.9,  68.8,  97.7, 126.6, 155.5, 184.4, 213.3, 242.2,\n",
       "        271.1, 300. ]),\n",
       " <a list of 10 Patch objects>)"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x=df[df['lead_time'] > 10]\n",
    "n=x['adr']\n",
    "plt.hist(n,10,range=[11,300],density=1,edgecolor='k',align='mid')\n",
    "#plt.axvline(df['lead_time'].mean(),color='k',linestyle='dashed',linewidth=1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Probability Distribution Function for ADR\n",
    "from scipy.stats import norm\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "x=df[df['lead_time'] > 10]\n",
    "x=df[df['adr'] < 250]\n",
    "n=x['adr']\n",
    "\n",
    "ax=n.plot.kde()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"simpletable\">\n",
       "<caption>OLS Regression Results</caption>\n",
       "<tr>\n",
       "  <th>Dep. Variable:</th>           <td>adr</td>       <th>  R-squared (uncentered):</th>      <td>   0.705</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared (uncentered):</th> <td>   0.703</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>          <td>   474.7</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Date:</th>             <td>Tue, 17 Nov 2020</td> <th>  Prob (F-statistic):</th>          <td>1.34e-54</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Time:</th>                 <td>21:12:05</td>     <th>  Log-Likelihood:    </th>          <td> -1092.1</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>No. Observations:</th>      <td>   200</td>      <th>  AIC:               </th>          <td>   2186.</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Residuals:</th>          <td>   199</td>      <th>  BIC:               </th>          <td>   2190.</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>              <td> </td>   \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>              <td> </td>   \n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "           <td></td>             <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>arrival_date_month</th> <td>   11.7997</td> <td>    0.542</td> <td>   21.789</td> <td> 0.000</td> <td>   10.732</td> <td>   12.868</td>\n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "  <th>Omnibus:</th>       <td> 9.201</td> <th>  Durbin-Watson:     </th> <td>   1.624</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Prob(Omnibus):</th> <td> 0.010</td> <th>  Jarque-Bera (JB):  </th> <td>   5.331</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Skew:</th>          <td>-0.217</td> <th>  Prob(JB):          </th> <td>  0.0696</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Kurtosis:</th>      <td> 2.328</td> <th>  Cond. No.          </th> <td>    1.00</td>\n",
       "</tr>\n",
       "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
      ],
      "text/plain": [
       "<class 'statsmodels.iolib.summary.Summary'>\n",
       "\"\"\"\n",
       "                                 OLS Regression Results                                \n",
       "=======================================================================================\n",
       "Dep. Variable:                    adr   R-squared (uncentered):                   0.705\n",
       "Model:                            OLS   Adj. R-squared (uncentered):              0.703\n",
       "Method:                 Least Squares   F-statistic:                              474.7\n",
       "Date:                Tue, 17 Nov 2020   Prob (F-statistic):                    1.34e-54\n",
       "Time:                        21:12:05   Log-Likelihood:                         -1092.1\n",
       "No. Observations:                 200   AIC:                                      2186.\n",
       "Df Residuals:                     199   BIC:                                      2190.\n",
       "Df Model:                           1                                                  \n",
       "Covariance Type:            nonrobust                                                  \n",
       "======================================================================================\n",
       "                         coef    std err          t      P>|t|      [0.025      0.975]\n",
       "--------------------------------------------------------------------------------------\n",
       "arrival_date_month    11.7997      0.542     21.789      0.000      10.732      12.868\n",
       "==============================================================================\n",
       "Omnibus:                        9.201   Durbin-Watson:                   1.624\n",
       "Prob(Omnibus):                  0.010   Jarque-Bera (JB):                5.331\n",
       "Skew:                          -0.217   Prob(JB):                       0.0696\n",
       "Kurtosis:                       2.328   Cond. No.                         1.00\n",
       "==============================================================================\n",
       "\n",
       "Warnings:\n",
       "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
       "\"\"\""
      ]
     },
     "execution_count": 231,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD4CAYAAAAXUaZHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAefElEQVR4nO3df2xc1ZUH8O/x4LIO7eKkBJQMCU6zNJQ0Sw0WCWupWmDTUArEC+qKCCqkVrB/sNuyQt7GS7SEijaR0u22UrddQcuSKmmgIWEIS0qgUKnaiIS1McFNaTaEH0kmKXEbTCtwi7HP/uHnYE/em8x43jtv3vH3I0X2XDt+d2beO3PfvefeK6oKIiLypSHtChARUfwY3ImIHGJwJyJyiMGdiMghBnciIodOS7sCAHDWWWdpS0tL2tUgIsqUnp6e36rqzLCf1UVwb2lpQXd3d9rVICLKFBF5I+pn7JYhInKIwZ2IyCEGdyIihxjciYgcYnAnInKoLrJliGhyCr1FrNuxD0cGBjG7uQmdyxagozWfdrWoDjC4E2VUobeIrq19GBwaBgAUBwbRtbUPABjgid0yRFm1bse+E4F9zODQMNbt2JdSjaieMLgTZdSRgcGqymlqYXAnyqjZzU1VldPUwuBOlFGdyxagqTE3oaypMYfOZQtSqhHVEw6oEmXU2KAps2UoDIM7UYZ1tOYZzCkUu2WIiBxicCcicojBnYjIIQZ3IiKHGNyJiBxicCcicoipkEQZxlUhKQqDO1FGcVVIKofBnShmVq3pcqtCMrgTgztRjCxb01wVksrhgCpRjCzXWOeqkFQOgztRjCxb01wVksphcCeKkWVruqM1jzXXL0K+uQkCIN/chDXXL2J/OwFgnztRrDqXLZjQ5w4k25rmqpAUhcGdKEZcY53qBYM7UczYmqZ6wD53IiKHGNyJiBxicCcicojBnYjIoVMGdxGZIyI/F5GXRWSviHwlKJ8hIk+LyP7g6/Rx/6dLRF4RkX0isizJJ0A0lRV6i2hf+yzmrXwC7WufRaG3mHaVqE5U0nJ/H8CdqvoJAEsA3C4iFwJYCeAZVT0fwDPBYwQ/uxHAQgBXAfieiORC/zIRTdrYOjbFgUEoPljHhgGegAqCu6oeVdUXgu//AOBlAHkAywGsD35tPYCO4PvlAB5S1T+p6msAXgFwadwVJ5rqLNexoeypqs9dRFoAtALYDeAcVT0KjH4AADg7+LU8gEPj/tvhoKz0b90mIt0i0t3f3199zYmmOK4KSeVUHNxF5MMAtgC4Q1V/X+5XQ8r0pALV+1S1TVXbZs6cWWk1iCjAVSGpnIqCu4g0YjSwb1TVrUHxmyIyK/j5LADHgvLDAOaM++/nAjgST3WJaAxXhaRyKsmWEQA/BPCyqn5r3I+2Abgl+P4WAI+NK79RRE4XkXkAzgfwfHxVJqpvVhksHa15XDz3zAllF889k0sfEIDKWu7tAL4A4AoReTH4dzWAtQCWish+AEuDx1DVvQB+AuBXAJ4EcLuqDof/aSJfLDNYVhX6sPPA8QllOw8cx6pCX+zHouwR1ZO6w821tbVpd3d32tUgqln72mdRDBnQzDc3YefKK2I91vyu7RgOuX5zIjiw5upYj0X1SUR6VLUt7GecoUoUI8sMlrDAXq6cphYGd6IYWWaw5CQsMS26nKYWBneiGFlmsKxYPKeqcppauFkHUYwsd2K6t2MRAGDT7kMYVkVOBCsWzzlRTlMbB1SJiDKKA6pERFMMgzsRkUMM7kREDjG4ExE5xOBOROQQUyGJYlboLZqkQhKVw+BOFKOxhcPGdkgaWzgMAAM8mWK3DFGMuPUd1QsGd6IYces7qhcM7kQx4tZ3VC8Y3IlixK3vqF5wQJXMec4msVw4DLB/LT2/d95w4TAyVZpNAoy2bNdcv4hBokqF3iI6N+/B0MgH13Bjg2Dd5y9K5LXke1d/uHAY1Q1mk8Rn9ba9EwI7AAyNKFZv25vI8fjeZQuDO5liNkl8BgaHqiqvFd+7bGFwJ1PMJskuvnfZwuBOpphNEp9pjeGXb1R5rdJ47wq9RbSvfRbzVj6B9rXPotBbTOxY3jBbhkxZZ5N4dnpjDu8OjYSWJyGNTCAu5TB5DO5krqM1z4szBgPvRvS5R5THwfK9KzeAy/Pn1NgtQ5RR3vvAOYBbGwZ3cs9rv6338QvvH15JY3An1wq9RXQ+sgfFgUEoRvttOx/Z4yLAd7Tmseb6Rcg3N0EA5JubXE0o8v7hlTTOUCUAfqeVt37tKbwV0gc9fVojev/1MynUiKrh9byMS7kZqhxQJddZCWGBvVw51RcOvk8eu2WI08qJHGJwJ9dZCc1NjVWVE3nB4E6usxJWX7fwpJO8ISgn8ozBndxnJUiDlH1M5NEpg7uIPCAix0Tkl+PKVotIUUReDP5dPe5nXSLyiojsE5FlSVWc4uM5pe6ex/diuGRZ3OERxT2PJ7MsLmCbV+81h59qV0m2zIMAvgvgRyXl/66q3xxfICIXArgRwEIAswH8TEQ+rqrDoLrmNSvBOlvGMvMojSwnpiZmxylb7qr6CwDHK/x7ywE8pKp/UtXXALwC4NIa6keUKZaZR9ZZTmMfJuMnhHVt7ePdQp2qpc/9H0TkpaDbZnpQlgdwaNzvHA7KTiIit4lIt4h09/f311ANovphmXlkneXElNlsmWxw/z6A+QA+BeAogH8LysNGqkKnwKrqfarapqptM2fOnGQ1iOqLZeaRdZaT55RZjyYV3FX1TVUdVtURAPfjg66XwwDmjPvVcwEcqa2KRJNnnedumXlkneXkOWXWo0kFdxGZNe7h3wIYy6TZBuBGETldROYBOB/A87VVkbyxzPBYfd1CNJakPjY2SGJ57paZR9ZZTt5TZr055cJhIrIJwF8DOAvAmwDuDh5/CqNdLq8D+HtVPRr8/l0AvgjgfQB3qOpPT1UJLhx2Mq9ZCaUZHsBogEgyKHl9LdPA17K+lFs4jKtC1qE0AqCV9rXPohjSR5tvbsLOlVekUKNsY7Cd2soFd85QrUOesxI4KBcfpiZSOQzudchzAJwKg3JWYwqeGwFUOwb3OuQ5AHYuW4DGXMkAZ07cDMpZ7vzkuRFAtWNwr0PusxJKh3nSH/aJzT2P78XQ8MQnNDSczFo2nhsBVDsG9zrkeSGvdTv2YahkIa+hEXXTlWC5lo37RgC4MFotuM1enfK6kBe7EuIzdn54zZbxvP2jBQZ3MjW7uSk0FTLJrgTLdMFpjQ14d2gktDwJXhsBQPkBY6/POU7sliFT1l0J1umCHzotV1U5ReNdXm0Y3MlUR2seN1ySR05GM2ZyIrjhkuRan9bpgm8PhvetR5VTNA4Y14bdMnXKeuah1fEKvUVs6SliOJgZPayKLT1FtJ03I5HjWbf+zmxqxEBIID+TG3JXrXPZgtCZ2l4GjJO+5thyr0PWXQmWx7NuSVu3/iRie9aocormOWvM4ppjcK9D1gHQ8njWLWnrPv6BiJTHqHKamiyuuUwHd685sNYBMCx7pVx5Laxb0tZ9/Ownjk+ht4jOzSWzfTcnM9vXmsU1ntng7nnRJOsAkYvoM4gqr0Ua2TJhffxJnSeXXxC+q1hUea28NnAAYPW2vaET3lZvi3+2r7WmiNTYqPLJyGxw97xoknWAGI5Y9jmqvBbW/ajW58kTLx2tqrwWhd4i7ixp2d7ppGULIHRgulx5lgy+f/JciHLlk5HZbBnPObA//3X4huFR5bXKR0wsyifYVWI1KGZ9nlguP3DXo30YLmnZDo8o7nq0z8Wgo2dR7aY421OZbbl77tv0PuhoyfN58s57w1WVZ830aeHpo1HlWWLRFZrZ4M6AFB/rrhLLfmLP54l3d1+7MHR56LuvTWb/W0srFs+pqnwyMtst43nRpDQmb1h1lVgvBmV9njRHTGJq5iSmqnm+xu/tWAQA2LT7EIZVkRPBisVzTpTHgXuo1imvM1S976E6lr43PsujsUGw7vMXxf56nv8vTyBkjTI0NgD7v/G5WI9F9ancHqqZbbl7ZznoaNma9jwQDti2NhtzDRgaOTm6N+Yy29s6pSTdoGJwJ9OlVdNYe8X6LshK2NLC5cqzyOt7Z9GgYnAn0xmq1muvWPfxe99gYlWhL9F+4vE8v5YWDSrev5HpDFXrtVc8r9PTEPH2RJXXalWhDxt2HZww23fDroNYVehL5HieJypy+QEyYTlD1TrN07qP3/J4IxFvT1R5rTbtPlRVea08j89YXAcM7hQ5EzWJGarWeefWHyaWx7O84wJsGwGA7wloFtcBg3uFPC/Q1PLR8IslqrwW1hOmOpctQGNJP0VjgyT2YWL54WUdbK0/TKzXWLJkcR1wQLUCngd2AGDXq29VVV6r7jeO4zdv/xEK4Ddv/xHdbxxP9HUszR1JMpfEMhVy+rTG0DVrkpqev2LxHGzYdTC0PAnWayxZSzrdmS33Cnge2AFsW4DWg3L3PL43dHGtex7P/rKxFotPjXdvxyLcvGTuhLXxb14yN7FsGc997hbYcq+A95MsJxIayJO43S43KJdEkLBcpRGwvctLYzPuezsWJRbMS82OWK3UQ5+7BbbcK9AccZsbVZ41FosYjbHuJ7ZmeZfnecAR4KJvtWJwr4D17S9gO4B7b8citM+fMaGsff6MRFpo1oNy1izv8qwHi6153iDbArtlKmB9+5vGrMoXDr49oeyFg2+j0FuM/XjWg3LWg47mXQmln4k+PiNPsFxjyRu23CtgffvreVal9aDc3dcuRK6kdZtrSG5NcMuuhHU79mFouGSP0WF1M9BPtTlly11EHgBwDYBjqvrJoGwGgIcBtAB4HcDfqepbwc+6AHwJwDCAL6vqjkRqbsh6fXXPsyoB20E5YLQFM1zyOCmWqZDeB/qteVukrJJumQcBfBfAj8aVrQTwjKquFZGVweOvisiFAG4EsBDAbAA/E5GPq2qm9/2y3jTAeuVEz1kJ63bsm7C2OgAMjWgiK16OsepK8Py+WfM4l+WUjRhV/QWA4yXFywGsD75fD6BjXPlDqvonVX0NwCsALo2prqnqaM1j58or8Nraz2HnyisSfcOtV070nJXguXXr+X2z5nEuy2TvUM9R1aMAEHw9OyjPAxifyHw4KDuJiNwmIt0i0t3f72PGWVysV07saM3jhkvyE/rBb7jEx0CW53RBZpPEx3LZ6zFJZ8TFnS0T1rYMTRhU1fsA3AeMbrMXcz0yzfp2u9BbxMPPH5owa/Th5w+h7bwZiWXnWHVxpbEfrSXrbBJv/dJjLCfyATbdQJNtub8pIrMAIPh6LCg/DGB8Ttu5AI5MvnrleV3My3rBpNXb9ob2S6/eFv8U/bGTujgwCMUHJ3VS7x1bt/Ep9BbR+cieCe9d5yN7XFx31pPrLLqBJtty3wbgFgBrg6+PjSv/sYh8C6MDqucDeL7WSobxOAAyxnrBpLDB23LltbDc0m8Mc6Xjcc/je0NTL+95fG/mX998xN1yEsteA3WyWYeIbALwHIAFInJYRL6E0aC+VET2A1gaPIaq7gXwEwC/AvAkgNuTypTxOAAyxvMgoOfn5p31Oj2WPO4zcMqWu6quiPjRlRG//3UAX6+lUpWwDhKWfY2eU9zSeG5e+4mnAqv3zjrd+fILZobO1I6z6zWzM1QtsyCs+4mtWxFRU/GTmKJvPZ5Q6C2ic3NJP/FmH/3EgO2407TG8HARVV4r6+subJ+BpGztOVxV+WRkNrhbT/O27AKyHgS8+9qFJ22q3CBIZIq+9XiC5WCxNevg96HTclWV18ryurPeZ+DdofAtY6LKJyOzC4d5n+ZtPQiYaxCMjBssK12PJS7Wr6XlYPEYq64E68Fp6wX0LM8V630GLGS25W7J80QYwHYBKu+vpWVr2vqD0vNm49apkBaz0DMb3C1zbtOY5r2q0If5XdvRsvIJzO/antjtIeB7DXLL8QTA92Yd1teB5fiM9T4DNy2eW1X5ZGQ2uJfLuY2b9fR86/4/6yBhuWH13dcuRGOu5MMkl9ySv9YflJbB1nosyHJ8xnI3MsBm6evM9rlb5twWeovY0lOcEGy39BQTm54fliI1Vp5E/5/lFP1yG1Z7SHGzTPW0fm5jx7QaC7L8oGw7bwZ+vOvghIZGQ1CelKSXvs5sy92S5wlTgG2LzPNEGMA+1dOaZeql5R3luh37Qu8os3yNZ7bl3hyx5nlzAmueT4VZlV6n6FsvU2HZlZDGdox3bt5z4s6rODCIOzfvSex4LR8Nvwtq+Wj8wd3jNZ7Zlvs1F82qqrwW1n3SUUM4SW6PadUii/rwTeJDGbC/67IMEtbP7a5H+0K71O56NJmxoF2vvlVVeS08ZnFlNrhbtpCsB65uWhIxkh5RXivL9L3V1y0MzZZZfV32BzgB2yBh/dzeeS98maio8lpZpid63Pgks8HdcnF96ywB602kLVuAHa15XDpv+oSyS+dNT3SAs5ryWlkGCY+tzfEs0xPTWBo6a5t1uGXdJ225ibTlB+WqQh92Hpi4ZsfOA8exqtCX+UwgwDaDpXPZggl94MDozOKknpsgfOedpLoLVyyeE5o5llR6ouU1bjFewuBOprvQWE/z9pwu2P3G8dA+8O43jidy/L84+wzsP/ZOaHkSxs6HTbtHdwnLiWDF4jmZXQ5gPIulIzIb3K23xfLMsm/Tepo34DcTyPqD8tX+d6sqj4PlHaylutiso15ZzyijeFhP8/bM+oMyjQ9mryzGSzIb3K0HHSkeSz42vapyimb9Qen9g9lygpbFGkuZ7ZYB/N6yWbPs4nr9d+G3nVHlFM16wNH6eJbGFiIcW69qbCFCIME9mUsvr5gvt8y23Ck+ll1cHmcCpsX67tXz3bLlQoSAzTLbmW65UzwssxI87w+bBuu7V+vjWW18Yr3mkUX6MYM7AbC7aK3zzim7rNfOsSQChI1Dx9kTyuBOptLIO7dq/VG8LLcRtFyIEAgP7OXKJ4PBvU55DkjeZgKmyfN5Yjk+s3D2R06aOT1WnlUM7nXIe0CyZL2JNGAXcAu9Rdzx8IsnHhcHBk889nCenBnRmj4zgda05QqUgE23DLNl6pD3zUEsWWfnWK6w2bn5xarKs2ZoOHwDxqjyWlhP0LLolmFwr0Pe0wW97uYD2H4wD0XEuKjyrLFcYtjjhDAG9zqUxlKuVgHXsmUL2G975/2D2SvrmdMWdwoM7hVaVejD/K7taFn5BOZ3bceqQjK7zwD2GwdYBlzrLifLTV0A/2usW7Lctct65nQ+4nyIKp8MBvcKrCr0YcOugyc+VYdVsWHXwcQCvPXGAZYB17pla7lWPWD7wdw+f0ZV5VljuZWm9XlpcZ5kOlvGKivBemlVwDZd0PLEtp6har00tGUe/8ZbL8NN9z83IYWvff4MbLz1stiPlQbLuy7r89LiPMlscLdMF/S+1KnliX35BTNDF59Kqg/c+/rxXgJ5GMtGRxozp5M+TzLbLcN0wfhYdiVY94Fb9G1SMizHL9LYQzVpmW25W/eletbRmsfm7oMTbu8vnntmIid2Gn3gXMsmm9LY/zbLwbxUTS13EXldRPpE5EUR6Q7KZojI0yKyP/iaSC6RZV7q9Gnho/NR5VlTbtPquFnnE3tskU0V3t+7pNOP42i5X66qvx33eCWAZ1R1rYisDB5/NYbjTGDZl2oxmyxNlgPG3vvAKV5e3zuLMcMk+tyXA1gffL8eQEcCxzDtS307ZH2LcuVZYxlw2QeebZaziz2zGDOsNbgrgKdEpEdEbgvKzlHVowAQfD077D+KyG0i0i0i3f391Q+mWQ4Cep+Y0hDRIxJVXgvrCVoUH+vZxZ5ZjD3VGtzbVfViAJ8FcLuIfLrS/6iq96lqm6q2zZxZfRqcZX+c94B0+mnhp0FUeS2896N6xgy1+FiMPdXU566qR4Kvx0TkUQCXAnhTRGap6lERmQXgWAz1DGXVH5fGBhOW/hix0lRUea289qN6x3Vz4mPRFTrp4C4iZwBoUNU/BN9/BsDXAGwDcAuAtcHXx+KoaNo8ByTua0qV4HkSn3zEa1kva8ucA+B/RGQPgOcBPKGqT2I0qC8Vkf0AlgaPqUqWA1edyxagMTfxdrAxJ266nSge3rsnLdX12jKq+iqAi0LKfwfgyloqNdWlshNT6d2gkzRPio/37klLHa15dL9xHJt2H8KwKnIiuOGSeHsHMjtD1TPrreHW7diHoZGJ0XxoRBM7nud9P73z3D1pqdBbxJae4oSVZrf0FNF23ozYXt9MB3evQcJ6ir7lQBn3h6VqeL3GLRpwmQ3unoOE9TK1lhsRp7FhNWWT9TVu+UFi0aDiqpB1yHqKftRnRhKfJUyno0pZXuPWE7QsJkZmNrh7DhLWU/QH3g1fRiGqvBbeZ/tSfCyvcevGokW2TGaDu+cgYZ1yZvlaMp2OKmV5XlqPc1nM1M5sn7vndbqtU84sX0um01GlLM9L63EuIPnMo8wGd+9BwjLlzPq1ZDodVcLyvPS4laZoHVS+ra1Nu7u7064GEU1R87u2R7bcD6y5OoUaVUZEelS1Lexnme1zJyKKi8eWO4M7EU15HjeRYXAnoinPYxZXZgdUiYji4jFBg8GdiAj+srjYLUNE5BCDOxGRQwzuREQOMbgTETnE4E5E5BCDOxGRQwzuREQOMbgTETnE4E5E5BCDOxGRQ1x+gCjDCr1FV+uhUHwY3IkyqtBbnLANXXFgEF1b+wCAAZ7YLUOUVet27JuwvygADA4NY92OfSnViOoJgztRRh0ZGKyqnKYWBneijJodsUtQVDlNLQzuRBnlcfcgig8HVIkyyuPuQRQfBneiDPO2exDFh90yREQOMbgTETmUWLeMiFwF4DsAcgB+oKprkzqWR9YzD2+6/znsPHD8xOP2+TOw8dbLEjseZdOqQh827T6EYVXkRLBi8Rzc27Eo7WpRiERa7iKSA/AfAD4L4EIAK0TkwiSO5dHYzMPiwCAUH8w8LPQWEzleaWAHgJ0HjuOm+59L5HiUTasKfdiw6yCGVQEAw6rYsOsgVhX6Uq4ZhUmqW+ZSAK+o6quq+h6AhwAsT+hY7ljPPCwN7Kcqp6lp0+5DVZVTupIK7nkA49/xw0HZCSJym4h0i0h3f39/QtXIJs48pHo01mKvtJzSlVRwl5CyCWeAqt6nqm2q2jZz5syEqpFNnHlI9SgnYZd1dDmlK6ngfhjAnHGPzwVwJKFjuWM987B9/oyqymlqWrF4TlXllK6kgvv/AjhfROaJyIcA3AhgW0LHcqejNY811y9CvrkJAiDf3IQ11y9KLFtm462XnRTImS1Dpe7tWISbl8w90VLPieDmJXOZLVOnRBPqLxORqwF8G6OpkA+o6tejfretrU27u7sTqQcRkVci0qOqbWE/SyzPXVW3A9ie1N8nIqJonKFKROQQgzsRkUMM7kREDjG4ExE5lFi2TFWVEOkH8Eba9ajQWQB+m3YlEuT5+fG5ZZfn51fLcztPVUNngdZFcM8SEemOSj3ywPPz43PLLs/PL6nnxm4ZIiKHGNyJiBxicK/efWlXIGGenx+fW3Z5fn6JPDf2uRMROcSWOxGRQwzuREQOMbhXSETmiMjPReRlEdkrIl9Ju05xE5GciPSKyH+nXZc4iUiziDwiIr8O3j9XaxmLyD8F5+QvRWSTiPxZ2nWaLBF5QESOicgvx5XNEJGnRWR/8HV6mnWsRcTzWxecmy+JyKMi0hzHsRjcK/c+gDtV9RMAlgC43eGm318B8HLalUjAdwA8qaoXALgIjp6jiOQBfBlAm6p+EqNLbN+Ybq1q8iCAq0rKVgJ4RlXPB/BM8DirHsTJz+9pAJ9U1b8E8H8AuuI4EIN7hVT1qKq+EHz/B4wGiGR2z0iBiJwL4HMAfpB2XeIkIn8O4NMAfggAqvqeqg6kW6vYnQagSUROAzANGd71TFV/AaB0Z/blANYH368H0GFaqRiFPT9VfUpV3w8e7sLoznU1Y3CfBBFpAdAKYHe6NYnVtwH8M4CRtCsSs48B6AfwX0GX0w9E5Iy0KxUXVS0C+CaAgwCOAnhbVZ9Kt1axO0dVjwKjjSwAZ6dcnyR9EcBP4/hDDO5VEpEPA9gC4A5V/X3a9YmDiFwD4Jiq9qRdlwScBuBiAN9X1VYA7yDbt/UTBP3PywHMAzAbwBkicnO6taLJEJG7MNr9uzGOv8fgXgURacRoYN+oqlvTrk+M2gFcJyKvA3gIwBUisiHdKsXmMIDDqjp2l/UIRoO9F38D4DVV7VfVIQBbAfxVynWK25siMgsAgq/HUq5P7ETkFgDXALhJY5p8xOBeIRERjPbbvqyq30q7PnFS1S5VPVdVWzA6GPesqrpo/anqbwAcEpEFQdGVAH6VYpXidhDAEhGZFpyjV8LRgHFgG4Bbgu9vAfBYinWJnYhcBeCrAK5T1Xfj+rsM7pVrB/AFjLZqXwz+XZ12pagi/whgo4i8BOBTAL6Rcn1iE9yRPALgBQB9GL2mMztVX0Q2AXgOwAIROSwiXwKwFsBSEdkPYGnwOJMint93AXwEwNNBXPnPWI7F5QeIiPxhy52IyCEGdyIihxjciYgcYnAnInKIwZ2IyCEGdyIihxjciYgc+n+9+nPrHERgGAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "new=df[df['reservation_status']==1]\n",
    "new=df[df['adr'] > 40]\n",
    "new=df[df['adr']< 250]\n",
    "new_1=new.sample(200)\n",
    "x=new_1['arrival_date_month']\n",
    "y=new_1['adr']\n",
    "\n",
    "plt.scatter(x,y)\n",
    "\n",
    "\n",
    "XE=sm.add_constant(x)\n",
    "mod=sm.OLS(y,x)\n",
    "res=mod.fit()\n",
    "res.summary()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:                    adr   R-squared:                       0.007\n",
      "Model:                            OLS   Adj. R-squared:                  0.002\n",
      "Method:                 Least Squares   F-statistic:                     1.437\n",
      "Date:                Tue, 17 Nov 2020   Prob (F-statistic):              0.232\n",
      "Time:                        21:11:45   Log-Likelihood:                -1057.6\n",
      "No. Observations:                 200   AIC:                             2119.\n",
      "Df Residuals:                     198   BIC:                             2126.\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "======================================================================================\n",
      "                         coef    std err          t      P>|t|      [0.025      0.975]\n",
      "--------------------------------------------------------------------------------------\n",
      "Intercept             93.9425      7.720     12.168      0.000      78.718     109.167\n",
      "arrival_date_month     1.2787      1.067      1.199      0.232      -0.825       3.383\n",
      "==============================================================================\n",
      "Omnibus:                       12.552   Durbin-Watson:                   1.948\n",
      "Prob(Omnibus):                  0.002   Jarque-Bera (JB):               13.048\n",
      "Skew:                           0.589   Prob(JB):                      0.00147\n",
      "Kurtosis:                       3.419   Cond. No.                         16.7\n",
      "==============================================================================\n",
      "\n",
      "Warnings:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "results = smf.ols('adr ~ arrival_date_month', data=new_1).fit()\n",
    "print(results.summary())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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XuaPfvQjkpOTMTPMjMzMTKZMmQLAxIkTyczMDOdFTueccw733XcfzZo1q5Ber149fv/73zNu3DhatmwZ7ld5v4899lgKCwtZv3497dq1q1DPzEhJSeHss8+madOmpKWlVWg7EAhgZnTo0IF69epxyy237LENn376aY488kgyMjIYMGAAGzdujPNeq33jxo2joKCA1NRUhg0bFk4vPw4yMzOpX78+SUlJpKSk0KZNG377299ywgknkJSUFJ5yc3N54IEHKCgoICcnh4YNG9KwYcNwfk5ODv379+e4446jQYMGZGdnh/dDVlYWM2bM4J133uHkk0+mQYMGdO7cmbfeeovLLrsMM+Oxxx6jR48eZGdn07x5c375y1+ybdu2A7pNlixZEl6/nJwcevXqxZIlSyrU/fDDDznttNPIzMykWbNm3H///eG8M844g9zcXBo2bMjxxx/PCy+8EM5zd2677Tby8/Np2LAhF198MVu3bq29lXL3Oj+deOKJLiLRFRcXe9u2bf3uu+/2kpISnzVrlqenp/vSpUt95cqVDvill17qRUVFvn79ej/uuOP8/vvv99dff91zc3N90aJFvnv3bh8+fLhnZWX5mDFj3N39jjvu8NTUVL/66qt9+/bt3r9/f09NTfUXXnjB3d1vvvlmb9Sokb/99ts+a9YsT0pK8kAg4CtXrgz3bfbs2V6/fn0HPC8vz+vXr++pqan+6quv+oMPPuiAL1++3E877TQ/6aSTvHfv3j5lyhS/6qqrvGHDhm5mfvXVV/unn37qmZmZ3rVrV587d663bNnSU1NTHfDHHnvMS0tLvXfv3t6nTx/fsWOHv//++37kkUf6448/7rt27fJTTz3VMzIyfMaMGd6vXz8fPXp0hW24aNEiz8zM9Dlz5vi2bdt80KBBftFFFx2oXVhrpkyZ4tOmTfPhw4f70KFDw+nlx8Err7zi+fn5/u6773ppaamvXbvWH330UT/11FMd8NNPP91XrFjhzZs39+TkZP/ggw+8rKzMTzzxRE9OTva8vDyfNGmSZ2Vl+fDhw33+/Pk+Z84cBzwrK8v/+c9/+imnnOLJycmek5PjkydP9pKSEn/yySc9MzPTTznlFAf87rvv9ldeecV37NjhGzdu9D59+vivfvWrA7pNNm3a5CtXrvSysjIvKSnx+++/3zt16hTO//rrrz03N9efeuop37Vrl2/dutWXLFkSzl+wYIEXFxe7u/vcuXM9MzPT161b5+7uTzzxhLdr185Xr17t27Zt8379+vmQIUP2qt/APK8iJh70oHwgJgV+kap9/PHHnpGR4WVlZeG0s88+22+66abwG/6LL74Yzrv++uv9iiuu8Ouuu86vvPLKcPrcuXMd8NmzZ7u7+/Dhw71evXq+ePFid3d/+eWXPTMz0//yl7+4u/v555/vd955p7u7v/fee56SkuKAT5w40d2DH0jat2/vaWlpDnivXr38qKOO8l69elXo25dffulnnXWWX3DBBZ6ZmRnuTyAQ8IyMjHCQHjJkiKelpXmfPn38xRdfdMCB8AeNxo0b+/vvvx+uf9ttt3mPHj28qKjIs7OzvUWLFu7uPnjw4D0C/w033OCDBg0Kzy9fvtyTk5N969ate70/DgV//OMfowb+7t27+z/+8Y89ymdlZXlqamq4zm233eb16tXzd955x5cuXeqBQMC7du3qaWlp7u7eo0cPf/jhh93d/Wc/+5k3bNjQr7rqKh8xYoQvX77cAW/WrFm4/eLiYk9NTfXRo0c74MuWLauw/ClTpvhxxx1Xy1uhosrbJFJxcbGPGzcuvH7uwWPikksuiant9957z1NTU/29995z94r/G+7ub7/9tqempvqOHTti7m91gV+X+kUSXPA9Ys+0RYsWhecvuugiWrZsyYUXXsjLL79Mnz59vj97CHnuuecA2LJlCwCXX345zZo148EHH2TLli08/PDDuDu9evUKL+Pxxx+nfv36dOvWjY4dOwKQnp4OwL333kvXrl3D7X/zzTcMGTIEgEWLFoUvjTZv3pzZs2fzySef0K5du3D5evXq8d1337Ft2zZ27tzJf//7X4qLi0lJSaFJkybhcm3atCE5OZktW7ZQXFwcTt+0aRNvvfUWaWlpbN68mVGjRlW5DRcvXszxxx9foc2UlBQ+++yzKuscjubOncvvfvc7GjZsSIsWLRgxYgRFRUXUq1eP7OxsVq9eTWlpKYsXL6a0tJTOnTvTpUsXSktL+fDDD2nSpAlNmzZlzZo1zJ07F4AvvviC1NRU3nzzTTp27EibNm0wM4qKisLLvffee6lfv3742KrsjTfeCB8/B1p2djb169fnqquu4sYbbwynz507l0aNGnHqqafStGlTzjvvPFavXl2h7rnnnhs+/k8//XQKCgoA9vjfcnd2797NsmXLaqXPCvwiCa59+/Y0bdqUsWPHUlxczH/+8x/mzJnDzp07adKkCZMnT6Z9+/Zs2LCB5557jq1btzJgwADOOeccJk+ezMKFCykqKuKxxx7DzNi5cycAxx57LD/4wQ946KGHyM7O5t///jdXXnklJ510EgB9+/altLSUjz/+mEmTJoWDZLNmzVizZg1///vfuf/++0lNTQVg4cKFHH300eG+XX755XzwwQcsWbKEn//853z22WckJX3/lnb00UdTVlbGPffcQ4MGDfjkk08oKSnhvvvuY+HCheFyc+bMYfbs2ZSWlnLxxRezbds2li9fztSpU0lJSWHw4MF07dqVE044ocptuH37drKysiqkZWVlxe2+84HWpEkTZsyYAUDr1q057bTTaN++PR999BG33norffr0AYIBOCUlhUmTJhEIBMjIyOCRRx4hNTWVtLQ0rr32WlavXk1ubm64vdTUVDZt2sS3337LJZdcwvjx43F3du7cyaRJk1ixYgV33XUXW7ZsCR9bkV599VXGjx/Pn/70pwO3QSJs3ryZLVu2MG7cOLp06RJOX7t2LePHj+f+++9n9erVHHXUUQwaNKhC3Zdffplt27YxY8YMevfuHT5++/btyz/+8Q9WrVrFli1buOOOOwCirv8+qepSQF2adKlfpHoLFizw0047zRs1auQ//vGPffDgwf6LX/zCS0tLvVWrVn7rrbf6rl27fPHixQ741Vdf7e7u48aN82OOOcazs7M9OTnZGzZs6G+88Ya7u19wwQVer149f/DBB3379u1+3XXXeUZGhj/44IPu7l5aWuqjRo3y/Px8T0tL84yMDAd89erVPnDgQB8/fry7u+fn5zvggUCgQt/KLVu2zHNycrxz584O+JYtW9zdvX379uHL/T/4wQ88Ly/PA4GAu7s//fTTe1zq//GPf+z169f3Zs2aeYcOHfyPf/yjH3XUUd6gQQN//vnnvWnTpl5cXBz1Un+/fv38jjvuqJCWmZnp8+bNq90ddYBEu6y9ceNGB/yJJ57w9evXO+ATJkzwE044wadMmeKBQMBTU1O9Q4cOftlll3kgEPCPPvrIp06dGr4N0KhRI//qq6/8f/7nfxzwzZs3e6dOnTwzM9M7d+7sOTk5fvHFF3sgEPB+/fp5QUGBJycne7du3fzss8/2P/3pTxUu9b/77rvepEkTf+211w7KNolUWloaXj93986dO/uwYcPC+d988014naPp3bt3ePxL+f/GkUce6Xl5eX7PPfeE/zdihS71i0h1OnfuzJw5c/j222+ZOXMmK1as4OSTT2bjxo2sWbOGESNGkJqaSuPGjYHgWRbAb37zG5YtW8YFF1zAOeecQ0lJCccddxwQHNGcmprKlVdeSUZGBjfddBM7duxg+vTpACQlJXHLLbdw5pln0q1bN4455hiysrLIy8tj1qxZjBw5ksaNG4cvj6alpTF06NBw3yB4mbhXr170798//KSBhy6RfvPNNzRp0oTrr7+eJUuW8N1331FaWkrTpk255pprwuv+yCOPAJCSkkJOTg5ffvklixcvpqysjGbNmtGoUSNOPvlkNmzYUOXI6o4dO7JgwYLw/IoVK9i9ezfHHnts7eygQ0BOTg5HHHFE+EkH+H5br1ixgjZt2nDxxRezePFimjdvTvPmzXnttdfo2LEjxcXFFBcXs3PnTgoLC1m8eDEATz75JCtXruTMM89kwYIFbNy4kTFjxlBaWsqwYcP44IMPSE9PZ+XKlcyaNYt7770XgFNOOYW//OUv9OvXj8cff5yzzjrr4GyUCGVlZeH1g+D/VPl2AvbYZpWVlJTw+eefA8H/jTFjxrBq1SrWrl1Lx44dycvLIy8vr1b6qsAvIixcuJBdu3axc+dO7rrrLtavX8+wYcP4/PPPOeKII3jooYf46quvGD58OE2aNKFLly7s2rWLRYsWsXPnTp599llWrVrFNddcQ05ODhB8c969ezf/+Mc/2L17N3fccQfJycmcdNJJfPrpp0yePJmLLrqIxYsXc8YZZ7Bw4UJGjBhBUlISn332GQsWLKBv377h+57PPvssX3zxBevXr6esrIwnn3ySnj17cv755/Puu+9SUlLC6aefTkZGBtu2bSMnJ4etW7eyadMmJk+ezPbt22ncuDELFy7k/fffJxAIAMHHqt58801mzpzJaaedRmlpKTfddBMPP/wwAOeffz7XXXcdJ5xwAunp6ZSVlVFSUsKuXbsoLS0FYPDgwbz00ku8+eab7Nixg1GjRjFw4EAaNGhwEPbmvotcr9LSUnbt2kVJSQnvvfceS5cuZdiwYdx7771cccUV9OjRg8cee4xzzjmH3NxcVq9ezYYNG3jhhRd46KGH2LRpE+np6bRp04ZjjjmGZ599loyMDD755BPmz5/P0Ucfza233srEiROZNWsWs2fPZv369fTr14/GjRvTunVriouLmT9/Pv369aNr167hx+Xuu+8+7rvvPh544AHOO++8g7JNXn31VT766CNKS0vZunUrv/vd78jJyeEHP/gBAJdddhnTpk0Ljy3585//HH4E8dNPP+WVV16hqOj/t3fv8VHVZ+LHP0/CBGYSSIjBBsJN/AEhERE25SIiRZHLikhBRQr+1J8uuq2sVEWhWkPZqlyqLtYWW/urlwW0qIhlYYXW4lIsoFBuCZeGRqgEFBEQwRESePaPczJMkpkwIZNMyDzv12temfme8/2e53zPZJ4553znHD+lpaXMnz+f1atXM3DgQAAOHz7M3//+d1SV7du388ADD/D4449XOJVVK+EOBTSmhx3qN6Z6Dz30kKalpWlycrIOGzYscCh14cKF2rp1a01ISFARZxCL1AAAGN5JREFU0aZNm+qIESP0s88+0yNHjmj37t21adOmmpCQoI888oiWlZUF2jx06JBee+212qRJEwXU4/HoyJEj9cSJE7p9+3bNzs4OHG4HtEmTJpqcnKzz589XVVW/36+pqanaqVMnBQIj8ouKivSOO+4I/BwvuL7P5wuM/K78aN26dWDUdKjpubm52rp1a/V6vZqVlaUZGRkK6EUXXaRjx47VMWPGVKnz0ksvBdZ3wYIF2q5dO/X5fDpy5Ej94osv6m8DRkmovsvPz9eFCxdqx44d1efzqc/nU4/HoxkZGTpp0iR99NFHq9RJTk7W2267Tbt27arJycnasmVL9fl8CmhCQoL26dNH27ZtG9jmIhKo26ZNG925c6feeuut2qJFC23RooXecsstgUPogI4ePVpFRJOTkwOPnJyceu2TRYsWBdYvIyNDhw8frlu2bKlQ95e//KW2adNG09LSdMSIEYFD9du3b9fevXtrSkqKpqamal5eni5evDhQb9euXdqlSxf1er3avn17ffrpp2scN9Uc6hcNc9ihMcnLy9MNGzbEOgxjjDGmXojIRlXNCzXNDvUbY4wxccQSvzHGGBNHLPEbY4wxcaRJrANobJZsKmH67ws56neuAJaclIgnMYEv/aW0SfMyZWhXRvWs+U8ylmwqYc6KXew/6g+0A/CTpYUc+dpZVprXw4gerVm18/PAfIOyW1V4XV6vclvnE9OFLlSf1qQfalu/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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from statsmodels.graphics.regressionplots import plot_leverage_resid2\n",
    "fig, ax = plt.subplots(figsize=(8,6))\n",
    "fig = plot_leverage_resid2(results, ax = ax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'average daily rate')"
      ]
     },
     "execution_count": 243,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "new=df[df['reservation_status']==1]\n",
    "\n",
    "new=df[df['adr']< 200]\n",
    "new=df[df['lead_time']<50]\n",
    "\n",
    "new_1=new.sample(200)\n",
    "x=new_1['lead_time']\n",
    "y=new_1['adr']\n",
    "plt.scatter(x,y)\n",
    "plt.xlabel(\"lead time\")\n",
    "plt.ylabel(\"average daily rate\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:                    adr   R-squared:                       0.045\n",
      "Model:                            OLS   Adj. R-squared:                  0.041\n",
      "Method:                 Least Squares   F-statistic:                     9.407\n",
      "Date:                Tue, 17 Nov 2020   Prob (F-statistic):            0.00246\n",
      "Time:                        22:14:04   Log-Likelihood:                -1033.4\n",
      "No. Observations:                 200   AIC:                             2071.\n",
      "Df Residuals:                     198   BIC:                             2077.\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "==============================================================================\n",
      "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
      "------------------------------------------------------------------------------\n",
      "Intercept     84.8371      4.549     18.650      0.000      75.866      93.808\n",
      "lead_time      0.2977      0.097      3.067      0.002       0.106       0.489\n",
      "==============================================================================\n",
      "Omnibus:                       27.870   Durbin-Watson:                   2.088\n",
      "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               36.218\n",
      "Skew:                           0.891   Prob(JB):                     1.37e-08\n",
      "Kurtosis:                       4.081   Cond. No.                         70.7\n",
      "==============================================================================\n",
      "\n",
      "Warnings:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "results = smf.ols('adr ~ lead_time', data=new_1).fit()\n",
    "print(results.summary())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-0.05674943 18.71211737  1.36123215  9.58469339  9.69153525  1.34874516]\n"
     ]
    }
   ],
   "source": [
    "regr = linear_model.LinearRegression()\n",
    "regr.fit(X, y)\n",
    "print(regr.coef_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"simpletable\">\n",
       "<caption>OLS Regression Results</caption>\n",
       "<tr>\n",
       "  <th>Dep. Variable:</th>           <td>adr</td>       <th>  R-squared (uncentered):</th>       <td>   0.366</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared (uncentered):</th>  <td>   0.366</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>           <td>6.882e+04</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Date:</th>             <td>Tue, 17 Nov 2020</td> <th>  Prob (F-statistic):</th>            <td>  0.00</td>   \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Time:</th>                 <td>09:42:52</td>     <th>  Log-Likelihood:    </th>          <td>-7.0736e+05</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>No. Observations:</th>      <td>119390</td>      <th>  AIC:               </th>           <td>1.415e+06</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Residuals:</th>          <td>119389</td>      <th>  BIC:               </th>           <td>1.415e+06</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>               <td> </td>     \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>               <td> </td>     \n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>lead_time</th> <td>    0.4610</td> <td>    0.002</td> <td>  262.327</td> <td> 0.000</td> <td>    0.458</td> <td>    0.464</td>\n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "  <th>Omnibus:</th>       <td>110045.093</td> <th>  Durbin-Watson:     </th>   <td>   0.612</td>   \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Prob(Omnibus):</th>   <td> 0.000</td>   <th>  Jarque-Bera (JB):  </th> <td>291143893.673</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Skew:</th>            <td> 3.134</td>   <th>  Prob(JB):          </th>   <td>    0.00</td>   \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Kurtosis:</th>        <td>244.841</td>  <th>  Cond. No.          </th>   <td>    1.00</td>   \n",
       "</tr>\n",
       "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
      ],
      "text/plain": [
       "<class 'statsmodels.iolib.summary.Summary'>\n",
       "\"\"\"\n",
       "                                 OLS Regression Results                                \n",
       "=======================================================================================\n",
       "Dep. Variable:                    adr   R-squared (uncentered):                   0.366\n",
       "Model:                            OLS   Adj. R-squared (uncentered):              0.366\n",
       "Method:                 Least Squares   F-statistic:                          6.882e+04\n",
       "Date:                Tue, 17 Nov 2020   Prob (F-statistic):                        0.00\n",
       "Time:                        09:42:52   Log-Likelihood:                     -7.0736e+05\n",
       "No. Observations:              119390   AIC:                                  1.415e+06\n",
       "Df Residuals:                  119389   BIC:                                  1.415e+06\n",
       "Df Model:                           1                                                  \n",
       "Covariance Type:            nonrobust                                                  \n",
       "==============================================================================\n",
       "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
       "------------------------------------------------------------------------------\n",
       "lead_time      0.4610      0.002    262.327      0.000       0.458       0.464\n",
       "==============================================================================\n",
       "Omnibus:                   110045.093   Durbin-Watson:                   0.612\n",
       "Prob(Omnibus):                  0.000   Jarque-Bera (JB):        291143893.673\n",
       "Skew:                           3.134   Prob(JB):                         0.00\n",
       "Kurtosis:                     244.841   Cond. No.                         1.00\n",
       "==============================================================================\n",
       "\n",
       "Warnings:\n",
       "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
       "\"\"\""
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#simple linear regression\n",
    "XE=sm.add_constant(x100)\n",
    "mod=sm.OLS(Y,x100)\n",
    "res=mod.fit()\n",
    "res.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"simpletable\">\n",
       "<caption>OLS Regression Results</caption>\n",
       "<tr>\n",
       "  <th>Dep. Variable:</th>    <td>reservation_status</td> <th>  R-squared (uncentered):</th>       <td>   0.855</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Model:</th>                    <td>OLS</td>        <th>  Adj. R-squared (uncentered):</th>  <td>   0.855</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Method:</th>              <td>Least Squares</td>   <th>  F-statistic:       </th>           <td>1.410e+05</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Date:</th>              <td>Tue, 17 Nov 2020</td>  <th>  Prob (F-statistic):</th>            <td>  0.00</td>   \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Time:</th>                  <td>07:47:35</td>      <th>  Log-Likelihood:    </th>          <td>-1.0009e+05</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>No. Observations:</th>       <td>119390</td>       <th>  AIC:               </th>           <td>2.002e+05</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Residuals:</th>           <td>119385</td>       <th>  BIC:               </th>           <td>2.002e+05</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Model:</th>               <td>     5</td>       <th>                     </th>               <td> </td>     \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Covariance Type:</th>       <td>nonrobust</td>     <th>                     </th>               <td> </td>     \n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "              <td></td>                 <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>lead_time</th>                 <td>    0.0015</td> <td> 1.55e-05</td> <td>   99.972</td> <td> 0.000</td> <td>    0.002</td> <td>    0.002</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>adults</th>                    <td>    0.3715</td> <td>    0.002</td> <td>  167.540</td> <td> 0.000</td> <td>    0.367</td> <td>    0.376</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>arrival_date_month</th>        <td>    0.0389</td> <td>    0.000</td> <td>   82.078</td> <td> 0.000</td> <td>    0.038</td> <td>    0.040</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>total_of_special_requests</th> <td>   -0.1250</td> <td>    0.002</td> <td>  -59.760</td> <td> 0.000</td> <td>   -0.129</td> <td>   -0.121</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>adr</th>                       <td>    0.0027</td> <td> 3.21e-05</td> <td>   83.737</td> <td> 0.000</td> <td>    0.003</td> <td>    0.003</td>\n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "  <th>Omnibus:</th>       <td>41051.909</td> <th>  Durbin-Watson:     </th>  <td>   0.655</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Prob(Omnibus):</th>  <td> 0.000</td>   <th>  Jarque-Bera (JB):  </th> <td>4785262.672</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Skew:</th>           <td>-0.643</td>   <th>  Prob(JB):          </th>  <td>    0.00</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Kurtosis:</th>       <td>33.989</td>   <th>  Cond. No.          </th>  <td>    246.</td>  \n",
       "</tr>\n",
       "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
      ],
      "text/plain": [
       "<class 'statsmodels.iolib.summary.Summary'>\n",
       "\"\"\"\n",
       "                                 OLS Regression Results                                \n",
       "=======================================================================================\n",
       "Dep. Variable:     reservation_status   R-squared (uncentered):                   0.855\n",
       "Model:                            OLS   Adj. R-squared (uncentered):              0.855\n",
       "Method:                 Least Squares   F-statistic:                          1.410e+05\n",
       "Date:                Tue, 17 Nov 2020   Prob (F-statistic):                        0.00\n",
       "Time:                        07:47:35   Log-Likelihood:                     -1.0009e+05\n",
       "No. Observations:              119390   AIC:                                  2.002e+05\n",
       "Df Residuals:                  119385   BIC:                                  2.002e+05\n",
       "Df Model:                           5                                                  \n",
       "Covariance Type:            nonrobust                                                  \n",
       "=============================================================================================\n",
       "                                coef    std err          t      P>|t|      [0.025      0.975]\n",
       "---------------------------------------------------------------------------------------------\n",
       "lead_time                     0.0015   1.55e-05     99.972      0.000       0.002       0.002\n",
       "adults                        0.3715      0.002    167.540      0.000       0.367       0.376\n",
       "arrival_date_month            0.0389      0.000     82.078      0.000       0.038       0.040\n",
       "total_of_special_requests    -0.1250      0.002    -59.760      0.000      -0.129      -0.121\n",
       "adr                           0.0027   3.21e-05     83.737      0.000       0.003       0.003\n",
       "==============================================================================\n",
       "Omnibus:                    41051.909   Durbin-Watson:                   0.655\n",
       "Prob(Omnibus):                  0.000   Jarque-Bera (JB):          4785262.672\n",
       "Skew:                          -0.643   Prob(JB):                         0.00\n",
       "Kurtosis:                      33.989   Cond. No.                         246.\n",
       "==============================================================================\n",
       "\n",
       "Warnings:\n",
       "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
       "\"\"\""
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "XA=df[['lead_time','adults','arrival_date_month','total_of_special_requests','adr']]\n",
    "YA=df['reservation_status']\n",
    "\n",
    "XMM=sm.add_constant(XA)\n",
    "\n",
    "Kmm=sm.OLS(YA,XA).fit()\n",
    "Kmm.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:     reservation_status   R-squared:                       0.062\n",
      "Model:                            OLS   Adj. R-squared:                  0.012\n",
      "Method:                 Least Squares   F-statistic:                     1.239\n",
      "Date:                Tue, 17 Nov 2020   Prob (F-statistic):              0.297\n",
      "Time:                        07:55:04   Log-Likelihood:                -68.884\n",
      "No. Observations:                 100   AIC:                             149.8\n",
      "Df Residuals:                      94   BIC:                             165.4\n",
      "Df Model:                           5                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "=============================================================================================\n",
      "                                coef    std err          t      P>|t|      [0.025      0.975]\n",
      "---------------------------------------------------------------------------------------------\n",
      "Intercept                     1.0447      0.223      4.685      0.000       0.602       1.487\n",
      "lead_time                     0.0010      0.001      1.638      0.105      -0.000       0.002\n",
      "adults                        0.1404      0.111      1.269      0.208      -0.079       0.360\n",
      "arrival_date_month           -0.0036      0.017     -0.212      0.833      -0.037       0.030\n",
      "total_of_special_requests     0.0291      0.064      0.456      0.649      -0.098       0.156\n",
      "adr                           0.0008      0.001      0.776      0.440      -0.001       0.003\n",
      "==============================================================================\n",
      "Omnibus:                     1364.449   Durbin-Watson:                   2.059\n",
      "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               12.884\n",
      "Skew:                           0.156   Prob(JB):                      0.00159\n",
      "Kurtosis:                       1.270   Cond. No.                         727.\n",
      "==============================================================================\n",
      "\n",
      "Warnings:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "df_2=df.sample(100)\n",
    "results = smf.ols('reservation_status ~ lead_time + adults + arrival_date_month + total_of_special_requests + adr', data=df_2).fit()\n",
    "print(results.summary())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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XkREJIIU4EVERCJIAV5ERCSCFOBFREQiSAFeREQkghTgRUREIkgBXkREJIIU4EVERCJIAV5ERCSCFOBFREQiSAFeREQkgtIa4M1sqJktN7MVZnZdnPmjzGxx+HrVzI5Odl0RERFJLG0B3szygDuBYUAf4EIz61NlsQ+AAe7eF5gATK7DuiIiIpJAOnPw/YEV7v6+u+8GpgFnxy7g7q+6++bw4zygW7LrioiISGLpDPBdgY9iPq8OpyUyFphV13XN7DIzKzaz4vXr19cjuSIiUl+ff/45Y8eO5eCDD6Z169b069ePWbOCn/Z58+bx9a9/nXbt2lFYWMg3v/lN1q1bV7HuH/7wBw455BDatGlDly5duOaaaygrKwPgww8/pFWrVpVeZsbtt9+eleNsCNIZ4C3ONI+7oNlAggD/87qu6+6T3b3I3YsKCwv3KaEiIpIaZWVlHHTQQcyZM4etW7cyYcIEzj//fFauXMnmzZu57LLLWLlyJatWraJ169aMGTOmYt0RI0bw3//+l23btrF06VLeeOMN/vjHPwLQvXt3duzYUfFasmQJTZo04dxzz83Woea8pmnc9mrgoJjP3YC1VRcys77AvcAwd99Yl3VFRCS3tGzZkvHjx1d8Hj58OD179mTBggXVgvGVV17JgAEDKj4feuihFe/dnSZNmrBixYq4+5kyZQqnnHIKPXr0SGn6oySdOfj5wOFm1tPM9gMuAGbELmBm3YFHgW+7+zt1WVdERHLfJ598wjvvvMORRx5Zbd7cuXOrTX/ooYdo06YN7du354033uD73/9+3O1OmTKFSy65JC1pjoq05eDdvczMrgRmA3nAfe7+ppldHs6/B7gJOBC4y8wAysLi9rjrpiutIiKSeqWlpYwaNYpLLrmE3r17V5q3ePFibr75Zh5//PFK0y+66CIuuugi3n33XaZMmULHjh2rbfell17ik08+4bzzzktr+hs6c49btd0gFRUVeXFxcbaTISLS6O3du5eLLrqIbdu28fjjj9OsWbOKeStWrGDAgAHcdtttfPvb3064jWnTpvH3v/+dRx99tNL07373u5SWlvLAAw+kLf0NhZktcPeiePPSWQcvIiKNkLszduxYPvnkE2bOnFkpuK9atYrTTz+dG2+8scbgDkGDvffee6/StJKSEv7xj38wffr0tKQ9StRVrYiIpNQVV1zBsmXLeOKJJ8jPz6+YvmbNGgYNGsQPf/hDLr/88mrr3XvvvXz66acAvPXWW9x6662cdtpplZaZPn06BQUFDBw4ML0HEQEqohcRkZRZtWoVPXr0oHnz5jRt+kUh8V/+8hdWrFjB+PHjadmyZaV1duzYAcCYMWOYOXMmO3bsqHhOfsKECbRo0aJi2SFDhtC/f38mTJiQmQPKcTUV0SvAi4iINFA1BXgV0YuIiESQAryIiEgEKcCLiIhEkB6TExGRrHps4Romzl7O2i0ldCnI59ohvRjZr6axySQZCvAiIpI1jy1cw/WPLqGkdA8Aa7aUcP2jSwAU5OtJRfQiIpI1E2cvrwju5UpK9zBx9vIspSg6FOBFRCRr1m4pqdN0SZ4CvIiIZE2Xgvw6TZfkKcCLiEjWXDukF/nN8ipNy2+Wx7VDemUpRdGhRnYiIpI15Q3p1Io+9RTgRUQkq0b266qAngYqohcREYkgBXgREZEIUoAXERGJIAV4kQZm2rRpfOlLX6Jly5YceuihvPTSS+zevZvzzjuPHj16YGa8+OKLldYZP348zZo1o1WrVhWv999/H4APP/yw0vRWrVphZtx+++3V9j1mzBjMjBUrVmTiUEWkHhTgRRqQZ599lp///Ofcf//9bN++nblz53LIIYcAcPLJJzN16lQ6deoUd91vfetb7Nixo+JVvl737t0rTV+yZAlNmjTh3HPPrbT+yy+/zHvvvZfeAxSRlFErepEG5Be/+AU33XQTX/nKVwDo2vWLlsdXX301AHl5eXHXTdaUKVM45ZRT6NGjR8W0srIyxo0bxwMPPMDRRx9dr+2LSGYoBy/SQOzZs4fi4mLWr1/PYYcdRrdu3bjyyispKUmuS88nnniCdu3aceSRR3L33XcnXG7KlClccskllabdcccdnHLKKfTt27dexyAimaMAL9JAfPLJJ5SWlvLPf/6Tl156iUWLFrFw4UJuueWWWtc9//zzWbZsGevXr+fOO+/kJz/5CYWFhbRu3Zp+/foxa9YsAF566SXWrFnDrbfeSuvWrenTpw/33nsvf/nLX7j55pvZsmULACeccAIdOnRg/PjxlfbTo0cP8vPzK+ryBw8eXDHvqaee4uSTT6agoIBOnTrxve99j+3bt6fuBIlIJQrwIg1Efn7QN/e4cePo3Lkz7du358c//jEzZ86sdd0+ffrQpUsX8vLyOP744znxxBM57rjj2Lp1KxMmTOD8889n5cqV3HXXXZSWlvKHP/yBbdu2MXHiRC6//HKuvvpq2rZtyzXXXAPAiy++yOuvv86DDz7I/fffX2lfTzzxREV9/jPPPFMxfevWrdxwww2sXbuWZcuWsXr1aq699toUniERiaUAL9JAHHDAAXTr1g0zq9d2WrZsyde//nX2339/mjRpwvDhw+nZsyevvfYaM2bMoE2bNgwbNgwz48wzz2Tv3r3cdNNNdOrUiQceeACAQYMG8eqrrzJ27Fjuu+++pPZ70UUXMXToUPbff38OOOAAvve97/HKK6/U61hEJDEFeJEGZMyYMfzpT3/i008/ZfPmzfzhD39g+PDhAHz++efs2rULgN27d7Nr1y7cHYDHH3+czZs34+68/vrr/PGPf+Tss88GgqL/d955hzVr1nDggQfSt29fZsyYwZ49e3jsscfo1KkTxcXFLFq0iIKCAiDIpX/jG9/A3Vm6dGmlNI4aNYrCwkIGDx7MG2+8kfBY5s6dy5FHHpnycyQiIXePzOu4445zkSjbvXu3X3HFFd62bVvv2LGjjxs3zktKStzd/eCDD3ag0uuDDz5wd/cLLrjA27Vr5y1btvRevXr5pEmTKrZ32mmn+WWXXeaDBw/2G264we+9915v2bKl5+XleX5+vj/55JMV+x81apQDvnDhQn/33Xf9kEMO8f32269i/ssvv+w7d+70zz77zH/96197x44dffPmzdWO45lnnvGCggJfvnx5Gs+WSPQBxZ4gJmY9KKfypQAvkrw9e/b4t771LR82bJjv3r3b3d2fffZZb9eunc+fP9/37Nnjr7/+unfq1MkXLlzo7u4bN270iy66yDt27Oh9+vTx//mf//FDDjkk4T569erlM2bMqDTttdde8/bt2/u///3v9B2cSCNRU4BXEb1II+TujB07lk8++YR//etfNGvWDIBFixZxyimnUFRURJMmTTj++OM54YQT+Pe//w1Au3bt+Nvf/sbHH3/Mm2++yd69e+nfv3/C/ZhZRTUBwMKFCznrrLO47777OO2009J7kCKNnAK8SCN0xRVXsGzZMp544omK1vkAxx9/fMUjeBAE5Jdeeqni+ff33nuPjRs3smfPHmbNmsXkyZO54YYbgKDL21deeaWi/n/ixIls2LCBk046CYClS5cydOhQ/vSnPzFixIgMH7FI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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from statsmodels.graphics.regressionplots import plot_leverage_resid2\n",
    "fig, ax = plt.subplots(figsize=(8,6))\n",
    "fig = plot_leverage_resid2(results, ax = ax)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
