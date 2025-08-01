from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Event
from .external_models import Datastreams
#from leaflet.forms.widgets import LeafletWidget
from django.http import HttpResponse, HttpResponseRedirect
import pandas as pd
import plotly.express as px
from plotly.offline import plot
from .utils import spike_test
from .forms import DateForm
from datetime import date, datetime, time
from .external_models import Datastreams
from ioos_qc import qartod
from django.utils.datastructures import MultiValueDict

# Create your views here.

def GetDate(request):
    # if this is a POST request we need to process the form data
    form = DateForm()

    context = {"Burton4H": [32.006617, -80.851801], "Catalina": [32.006419, -80.866956],
               "HWY80": [32.01831, -80.850964], "Lazaretto": [32.014112, -80.884092]}

    context['form'] = form

    if request.method =='POST':
        start = request.POST['start']
        end = request.POST['end']
        location = request.POST['location']
        try:
            generate_qartod = request.POST['qartod_true']
        except:
            generate_qartod = 'off'
        try:
            generate_csv = request.POST['csv_true']
        except:
            generate_csv = 'off'

        context['location'] = location.capitalize()

        df = pd.read_csv(f'{location}.csv')
        df = df[(df['date'] >= start) & (df['date'] <= end)]

        if generate_qartod == 'on':
            #Gross Range Test
            gross_range_results = qartod.gross_range_test(df[' water_level'], suspect_span=[-3, -1], fail_span=[-5, 2])
            gross_range_failures = (gross_range_results == 4).sum()
            gross_range_warnings = (gross_range_results == 3).sum()
            context['gross_range_results'] = f"Gross Range Test: This dataset contains {gross_range_failures} failures and {gross_range_warnings} warnings."

            spike_test = qartod.spike_test(df[' water_level'])
            spike_failures = (spike_test == 4).sum()
            spike_warnings = (spike_test == 3).sum()

            context['spike_results'] = f"Spike Test: This dataset contains {spike_failures} failures and {spike_warnings} warnings."

            print(spike_test)

        if generate_csv == 'on':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data_export.csv"'
            df.to_csv(path_or_buf=response, index=False)
            return response


        fig = px.line(df, 'date', ' water_level')
        fig_div = plot(fig, output_type='div')
        context["plot"] = fig_div

        #filtered_df = df[(df['DateColumn'] >= start_date) & (df['DateColumn'] <= end_date)]

        return render(request, 'header.html', context)

    return render(request, "form.html", context)



def GenerateData(request):
    context = {"Burton4H": [32.006617, -80.851801], "Catalina": [32.006419, -80.866956],
               "HWY80": [32.01831, -80.850964], "Lazaretto": [32.014112, -80.884092]}

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

    return context


    return render(request, 'header.html')

class GenerateReport(ListView):
    model = Event
    template_name = "header.html"
    context_object_name = 'events'

    def get_context_data(self):
        context = {"Burton4H": [32.006617, -80.851801], "Catalina": [32.006419, -80.866956], "HWY80": [32.01831, -80.850964], "Lazaretto":[32.014112, -80.884092]}

        # Plotting Openmeteo rain data
        df_rainfall = pd.read_csv("open-meteo-32.02N80.88W3m.csv")

        fig_rain = px.line(df_rainfall, 'time','rain (mm)')
        fig_rain_div = plot(fig_rain, output_type='div')
        context["rain_plot"] = fig_rain_div

        # Plotting Burton data
        df_burton = pd.read_csv('burton.csv')
        df_burton_tail1 = df_burton.tail(500)
        df_burton_tail2 = df_burton_tail1.copy()
        df_burton_tail3 = df_burton_tail1.copy()
        df_burton_tail4 = df_burton_tail1.copy()

        fig = px.line(df_burton_tail1, 'date',' water_level')
        fig_div = plot(fig, output_type='div')
        context["burton_plot"] = fig_div

        #Apply spike smoothing: mean
        df_burton_spike_mean = spike_test(df_burton_tail1, 1, ' water_level', .007, False, 3)
        fig_mean = px.line(df_burton_spike_mean, 'date', 'fixed')

        fig_div_mean = plot(fig_mean, output_type='div')
        context["burton_spike_mean_naive"] = fig_div_mean

        #Apply spike smoothing: median
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

        fig = px.line(df_catalina_tail, 'date',' water_level')
        fig_div = plot(fig, output_type='div')
        context["catalina_plot"] = fig_div

        # Plotting hwy80 data
        df_hwy80 = pd.read_csv('hwy80.csv')
        df_hwy80_tail = df_hwy80.tail(1000)

        fig = px.line(df_hwy80_tail, 'date',' water_level')
        fig_div = plot(fig, output_type='div')
        context["hwy80_plot"] = fig_div

        # Plotting lazaretto data
        df_lazaretto = pd.read_csv('lazaretto.csv')
        df_lazaretto_tail = df_lazaretto.tail(1000)

        fig = px.line(df_lazaretto_tail, 'date',' water_level')
        fig_div = plot(fig, output_type='div')
        context["lazaretto_plot"] = fig_div

        return context



class EventDisplay(TemplateView):
    model = Datastreams
    template_name = "display.html"
    context_object_name = 'events'

    

    """
    TODO:
    
    Sensor latlong to context
    Sensor Result to context

    """

    def get_context_data(self, **kwargs):
        context = {}
        return context

