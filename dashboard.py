import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue': [45000, 52000, 48000, 61000, 55000, 67000,
                72000, 68000, 75000, 82000, 95000, 110000],
    'Orders': [320, 380, 350, 420, 390, 460,
               510, 480, 530, 580, 670, 780],
    'Customers': [280, 330, 300, 370, 340, 400,
                  450, 420, 470, 510, 590, 690],
    'Returns': [12, 15, 13, 18, 14, 20,
                22, 19, 24, 26, 30, 35]
}

df = pd.DataFrame(data)

categories = {
    'Category': ['Electronics', 'Fashion', 'Home & Living',
                 'Sports', 'Beauty', 'Books'],
    'Sales': [85000, 62000, 48000, 35000, 28000, 15000],
    'Profit': [25000, 18000, 14000, 10000, 8000, 4000]
}

cat_df = pd.DataFrame(categories)

# Create Dashboard
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        'Monthly Revenue Trend',
        'Orders vs Customers',
        'Sales by Category',
        'Profit by Category',
        'Monthly Returns',
        'Revenue vs Orders'
    ),
    specs=[
        [{"type": "scatter"}, {"type": "bar"}],
        [{"type": "pie"}, {"type": "bar"}],
        [{"type": "bar"}, {"type": "scatter"}]
    ]
)

# Chart 1: Revenue Trend
fig.add_trace(go.Scatter(
    x=df['Month'], y=df['Revenue'],
    mode='lines+markers',
    name='Revenue',
    line=dict(color='#00C9FF', width=3),
    fill='tozeroy'
), row=1, col=1)

# Chart 2: Orders vs Customers
fig.add_trace(go.Bar(
    x=df['Month'], y=df['Orders'],
    name='Orders', marker_color='#FF6B6B'
), row=1, col=2)
fig.add_trace(go.Bar(
    x=df['Month'], y=df['Customers'],
    name='Customers', marker_color='#4ECDC4'
), row=1, col=2)

# Chart 3: Sales Pie Chart
fig.add_trace(go.Pie(
    labels=cat_df['Category'],
    values=cat_df['Sales'],
    name='Sales'
), row=2, col=1)

# Chart 4: Profit by Category
fig.add_trace(go.Bar(
    x=cat_df['Category'],
    y=cat_df['Profit'],
    name='Profit',
    marker_color='#A8E6CF'
), row=2, col=2)

# Chart 5: Monthly Returns
fig.add_trace(go.Bar(
    x=df['Month'], y=df['Returns'],
    name='Returns', marker_color='#FF8B94'
), row=3, col=1)

# Chart 6: Revenue vs Orders
fig.add_trace(go.Scatter(
    x=df['Orders'], y=df['Revenue'],
    mode='markers+text',
    text=df['Month'],
    name='Rev vs Orders',
    marker=dict(size=10, color='#C3A6FF')
), row=3, col=2)

# Dashboard Layout
fig.update_layout(
    title=dict(
        text='🛒 E-Commerce Sales Dashboard 2024',
        font=dict(size=24, color='white')
    ),
    paper_bgcolor='#1a1a2e',
    plot_bgcolor='#16213e',
    font=dict(color='white'),
    height=900,
    showlegend=True
)

fig.write_html("ecommerce_dashboard.html")
print("Dashboard saved successfully!")