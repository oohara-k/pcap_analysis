# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as pyplot
import numpy
import pandas as pd

df = pd.DataFrame({
    'date': pd.date_range('2016-06-02 00:00:00', periods=3, freq='d')
})

#np.whereでIPアドレスごとのものを取得
#それをnp.count_nonzero(a == value, axis=0)とか？
df['192.168.1.1'] = [5, 6, 7]
df['192.168.1.2'] = [7, 4, 7]
print df

df = df.set_index('date')
df.plot()

# Figure上に描画
pyplot.show()


