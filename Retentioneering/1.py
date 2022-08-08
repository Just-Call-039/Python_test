import retentioneering
import pandas as pd

data = pd.read_csv("Выгрузка цепочек 2.csv")
retentioneering.config.update({
    'user_col': 'id',
    'event_col':'event',
    'event_time_col':'call_date',
})

data.rete.plot_graph(norm_type='full',
                     weight_col='id',
                     thresh=0.06,
                     targets = {'payment_done':'green',
                                'lost':'red'})
