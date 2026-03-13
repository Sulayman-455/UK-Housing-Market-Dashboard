import pandas as pd
from sqlalchemy import create_engine, text
from django.shortcuts import render

engine = create_engine('sqlite:///housing.db')

def overview(request):
    query = text("""
        SELECT 
            Date,
            AveragePrice,
            "12mPctChange"
        FROM housing_data
        WHERE RegionName = 'England'
        AND AveragePrice IS NOT NULL
        ORDER BY Date ASC
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    
    df['Date'] = pd.to_datetime(df['Date'])
    dates = df['Date'].dt.strftime('%Y-%m').tolist()
    prices = df['AveragePrice'].tolist()
    latest = df.iloc[-1]

    context = {
        'dates': dates,
        'prices': prices,
        'latest_price': f"£{latest['AveragePrice']:,.0f}",
        'latest_change': f"{latest['12mPctChange']:.1f}%",
    }
    return render(request, 'dashboard/overview.html', context)

def regional(request):
    query = text("""
        SELECT 
            RegionName,
            AveragePrice
        FROM housing_data
        WHERE Date = (SELECT MAX(Date) FROM housing_data)
        AND RegionName NOT IN ('England', 'United Kingdom', 'Wales', 'Scotland', 'Northern Ireland')
        AND AveragePrice IS NOT NULL
        ORDER BY AveragePrice DESC
        LIMIT 20
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)

    context = {
        'regions': df['RegionName'].tolist(),
        'prices': df['AveragePrice'].tolist(),
    }
    return render(request, 'dashboard/regional.html', context)

def property_types(request):
    query = text("""
        SELECT 
            Date,
            DetachedPrice,
            SemiDetachedPrice,
            TerracedPrice,
            FlatPrice
        FROM housing_data
        WHERE RegionName = 'England'
        AND DetachedPrice IS NOT NULL
        ORDER BY Date ASC
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)

    df['Date'] = pd.to_datetime(df['Date'])

    context = {
        'dates': df['Date'].dt.strftime('%Y-%m').tolist(),
        'detached': df['DetachedPrice'].tolist(),
        'semi': df['SemiDetachedPrice'].tolist(),
        'terraced': df['TerracedPrice'].tolist(),
        'flats': df['FlatPrice'].tolist(),
    }
    return render(request, 'dashboard/property_types.html', context)

def first_time_buyers(request):
    query = text("""
        SELECT 
            Date,
            FTBPrice,
            AveragePrice,
            FOOPrice
        FROM housing_data
        WHERE RegionName = 'England'
        AND FTBPrice IS NOT NULL
        ORDER BY Date ASC
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)

    df['Date'] = pd.to_datetime(df['Date'])
    latest = df.iloc[-1]

    context = {
        'dates': df['Date'].dt.strftime('%Y-%m').tolist(),
        'ftb': df['FTBPrice'].tolist(),
        'average': df['AveragePrice'].tolist(),
        'latest_ftb': f"£{latest['FTBPrice']:,.0f}",
        'latest_avg': f"£{latest['AveragePrice']:,.0f}",
    }
    return render(request, 'dashboard/ftb.html', context)