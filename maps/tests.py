from django.test import TestCase
import external_models
from datetime import date, datetime, time

#from demo.maps.external_models import Datastreams

# Create your tests here.

today = date.today()
#queryset = Datastreams

"""
        # Plotting Openmeteo rain data
        df_rainfall = pd.read_csv("open-meteo-32.02N80.88W3m.csv")

        fig_rain = px.line(df_rainfall, 'time', 'rain (mm)')
        fig_rain_div = plot(fig_rain, output_type='div')
        context["rain_plot"] = fig_rain_div

        # Plotting Burton data
        df_burton = pd.read_csv('burton.csv')
        df_burton_tail1 = df_burton.tail(500)
        df_burton_tail2 = df_burton_tail1.copy()
        df_burton_tail3 = df_burton_tail1.copy()
        df_burton_tail4 = df_burton_tail1.copy()

        fig = px.line(df_burton_tail1, 'date', ' water_level')
        fig_div = plot(fig, output_type='div')
        context["burton_plot"] = fig_div

        # Apply spike smoothing: mean
        df_burton_spike_mean = spike_test(df_burton_tail1, 1, ' water_level', .007, False, 3)
        fig_mean = px.line(df_burton_spike_mean, 'date', 'fixed')

        fig_div_mean = plot(fig_mean, output_type='div')
        context["burton_spike_mean_naive"] = fig_div_mean

        # Apply spike smoothing: median
        df_burton_spike_median = spike_test(df_burton_tail2, 2, ' water_level', .007, False, 3)
        fig_median = px.line(df_burton_spike_median, 'date', 'fixed')

        fig_div_median = plot(fig_median, output_type='div')
        context["burton_spike_median_naive"] = fig_div_median

        # Running the standard deviation version

        # Apply spike smoothing: mean
        df_burton_spike_mean_std = spike_test(df_burton_tail3, 1, ' water_level', .007, True, 3)
        fig_mean_std = px.line(df_burton_spike_mean_std, 'date', 'fixed')

        fig_div_mean_std = plot(fig_mean_std, output_type='div')
        context["burton_spike_mean_std"] = fig_div_mean_std

        # Apply spike smoothing: median
        df_burton_spike_median_std = spike_test(df_burton_tail4, 2, ' water_level', .007, True, 3)
        fig_median_std = px.line(df_burton_spike_median_std, 'date', 'fixed')

        fig_div_median_std = plot(fig_median_std, output_type='div')
        context["burton_spike_median_std"] = fig_div_median_std

        # Plotting Catalina data
        df_catalina = pd.read_csv('catalina.csv')
        df_catalina_tail = df_catalina.tail(1000)

        fig = px.line(df_catalina_tail, 'date', ' water_level')
        fig_div = plot(fig, output_type='div')
        context["catalina_plot"] = fig_div

        # Plotting hwy80 data
        df_hwy80 = pd.read_csv('hwy80.csv')
        df_hwy80_tail = df_hwy80.tail(1000)

        fig = px.line(df_hwy80_tail, 'date', ' water_level')
        fig_div = plot(fig, output_type='div')
        context["hwy80_plot"] = fig_div

        # Plotting lazaretto data
        df_lazaretto = pd.read_csv('lazaretto.csv')
        df_lazaretto_tail = df_lazaretto.tail(1000)

        fig = px.line(df_lazaretto_tail, 'date', ' water_level')
        fig_div = plot(fig, output_type='div')
        context["lazaretto_plot"] = fig_div
"""

