
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="PollInsights | Analytics Studio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "poll_responses.csv"

COLORS = [
    "#3977D5",
    "#13A89E",
    "#E9A23B",
    "#D95757",
    "#8067C7",
    "#48A6D9",
    "#E17AA5",
    "#7D9B76",
]

# =========================================================
# CUSTOM DESIGN
# =========================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #F4F7FB;
    }

    .block-container {
        padding-top: 1.7rem;
        padding-bottom: 2rem;
        max-width: 1600px;
    }

    /* LEFT NAVIGATION */
    [data-testid="stSidebar"] {
        background: #142B4A;
        border-right: 1px solid #284563;
    }

    [data-testid="stSidebar"] > div {
        padding-top: 1.1rem;
    }

    [data-testid="stSidebar"] * {
        color: #F2F6FC;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: #D4DFEE;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] > label {
        color: #91A9C5;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 9px;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] {
        gap: 7px;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] > label {
        background: #1B385B;
        border: 1px solid #29496D;
        border-radius: 10px;
        padding: 12px 10px;
        margin: 0;
        transition: background 0.2s ease;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
        background: #2B4E74;
        border-color: #6488B0;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] > label p {
        font-size: 13px;
        font-weight: 500;
    }

    [data-testid="stSidebar"] [data-testid="stExpander"] {
        border: 1px solid #34516F;
        border-radius: 10px;
        background: #1B385B;
    }

    [data-testid="stSidebar"] [data-testid="stExpander"] summary {
        font-size: 13px;
        font-weight: 600;
    }

    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] [data-baseweb="select"] {
        border-radius: 8px;
    }

    .brand-wrap {
        padding: 10px 2px 23px 2px;
    }

    .brand-row {
        display: flex;
        align-items: center;
        gap: 11px;
    }

    .brand-icon {
        width: 43px;
        height: 43px;
        border-radius: 12px;
        background: #3977D5;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 23px;
        font-weight: 800;
        flex-shrink: 0;
    }

    .brand-name {
        font-size: 20px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.7px;
    }

    .brand-subtitle {
        font-size: 9px;
        letter-spacing: 1.5px;
        color: #AFC3DC;
        margin-top: 4px;
    }

    .nav-label {
        font-size: 10px;
        color: #91A9C5;
        font-weight: 700;
        letter-spacing: 1.6px;
        margin: 7px 0 12px 3px;
    }

    .sidebar-divider {
        height: 1px;
        background: #34516F;
        margin: 20px 0;
    }

    .sidebar-note {
        margin-top: 22px;
        padding: 13px;
        border: 1px solid #34516F;
        background: #1B385B;
        border-radius: 11px;
    }

    .sidebar-note-title {
        color: white;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .sidebar-note-text {
        color: #B8CBE2;
        font-size: 11px;
        line-height: 1.7;
    }

    /* PAGE HEADER */
    .page-header {
        background: linear-gradient(115deg, #142B4A, #28578A);
        padding: 26px 28px;
        border-radius: 16px;
        color: white;
        margin-bottom: 22px;
        box-shadow: 0 7px 20px rgba(20, 43, 74, 0.08);
    }

    .page-header h1 {
        color: white;
        font-size: 28px;
        margin: 0 0 8px 0;
        font-weight: 800;
        letter-spacing: -0.8px;
    }

    .page-header p {
        color: #DCE8F6;
        font-size: 13px;
        margin: 0;
        line-height: 1.7;
    }

    .section-heading {
        font-size: 18px;
        font-weight: 700;
        color: #193453;
        margin: 22px 0 13px 0;
    }

    .section-caption {
        color: #7D8BA0;
        font-size: 12px;
        margin-top: -7px;
        margin-bottom: 14px;
    }

    /* KPI CARDS */
    .metric-card {
        background: white;
        padding: 19px;
        border-radius: 13px;
        border: 1px solid #E4EAF2;
        min-height: 116px;
        box-shadow: 0 3px 12px rgba(27, 52, 84, 0.035);
        overflow-wrap: anywhere;
    }

    .metric-label {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
        color: #758399;
        margin-bottom: 11px;
    }

    .metric-value {
        font-size: 26px;
        font-weight: 800;
        color: #193453;
        line-height: 1.25;
        overflow-wrap: anywhere;
    }

    .metric-note {
        font-size: 10px;
        color: #8793A5;
        margin-top: 8px;
        line-height: 1.5;
    }

    /* CHARTS AND TABLES */
    div[data-testid="stPlotlyChart"] {
        background: white;
        border: 1px solid #E4EAF2;
        border-radius: 13px;
        padding: 5px;
        margin-bottom: 12px;
        overflow: hidden;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #E4EAF2;
        border-radius: 10px;
        overflow: hidden;
    }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #E4EAF2;
        padding: 15px;
        border-radius: 12px;
    }

    .info-panel {
        background: white;
        border: 1px solid #E4EAF2;
        border-radius: 12px;
        padding: 16px;
        margin: 8px 0 16px 0;
    }

    .footer {
        text-align: center;
        color: #8290A3;
        font-size: 11px;
        padding: 28px 0 8px 0;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem 0.8rem;
        }

        .page-header {
            padding: 20px;
        }

        .page-header h1 {
            font-size: 23px;
        }

        .metric-card {
            padding: 14px;
        }

        .metric-value {
            font-size: 21px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data(file_path, modified_time):
    data = pd.read_csv(file_path)

    required_columns = [
        "Respondent ID",
        "Timestamp",
        "Question",
        "Option",
        "Region",
        "Age Group",
    ]

    missing = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            "Required columns missing: " + ", ".join(missing)
        )

    data["Timestamp"] = pd.to_datetime(
        data["Timestamp"], errors="coerce"
    )

    for column in ["Question", "Option", "Region", "Age Group"]:
        data[column] = (
            data[column]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .replace("", "Unknown")
        )

    data["Respondent ID"] = (
        data["Respondent ID"].fillna("Unknown").astype(str)
    )

    return data


if not DATA_PATH.exists():
    st.error(f"Poll dataset not found: {DATA_PATH}")
    st.info("Check that data/poll_responses.csv exists.")
    st.stop()

try:
    df = load_data(
        str(DATA_PATH),
        DATA_PATH.stat().st_mtime,
    )
except Exception as exc:
    st.error(f"Unable to load the poll data: {exc}")
    st.stop()

if df.empty:
    st.warning("The poll dataset is empty.")
    st.stop()

# =========================================================
# SIDEBAR: BRAND, NAVIGATION, FILTERS
# =========================================================
with st.sidebar:
    st.markdown(
        """
        <div class="brand-wrap">
            <div class="brand-row">
                <div class="brand-icon">◈</div>
                <div>
                    <div class="brand-name">PollInsights</div>
                    <div class="brand-subtitle">ANALYTICS STUDIO</div>
                </div>
            </div>
        </div>
        <div class="nav-label">MAIN MENU</div>
        """,
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Navigation",
        [
            "🏠  Overview",
            "📊  Poll Results",
            "🌍  Audience Insights",
            "📈  Trends",
            "🗃️  Raw Data",
        ],
        label_visibility="collapsed",
        key="page_navigation",
    )

    st.markdown(
        """
        <div class="sidebar-divider"></div>
        <div class="nav-label">CUSTOMIZE YOUR VIEW</div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("⚙️  Response filters", expanded=True):
        all_questions = sorted(df["Question"].unique().tolist())

        selected_questions = st.multiselect(
            "Poll questions",
            options=all_questions,
            default=all_questions,
            key="filter_questions",
        )

        option_source = df[
            df["Question"].isin(selected_questions)
        ]

        all_options = sorted(option_source["Option"].unique().tolist())

        selected_options = st.multiselect(
            "Answer options",
            options=all_options,
            default=all_options,
            key="filter_options",
        )

        all_regions = sorted(df["Region"].unique().tolist())

        selected_regions = st.multiselect(
            "Regions",
            options=all_regions,
            default=all_regions,
            key="filter_regions",
        )

        all_ages = sorted(df["Age Group"].unique().tolist())

        selected_ages = st.multiselect(
            "Age groups",
            options=all_ages,
            default=all_ages,
            key="filter_ages",
        )

        if df["Timestamp"].notna().any():
            min_date = df["Timestamp"].min().date()
            max_date = df["Timestamp"].max().date()

            date_range = st.date_input(
                "Response dates",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date,
                key="filter_dates",
            )
        else:
            date_range = None

        st.caption("Filters apply across all dashboard pages.")

        if st.button(
            "↻  Reset filters",
            use_container_width=True,
            key="reset_filters",
        ):
            for key in [
                "filter_questions",
                "filter_options",
                "filter_regions",
                "filter_ages",
                "filter_dates",
            ]:
                st.session_state.pop(key, None)

            st.rerun()

    st.markdown(
        """
        <div class="sidebar-note">
            <div class="sidebar-note-title">📊 Your workspace</div>
            <div class="sidebar-note-text">
                Analyze preferences, explore audiences,
                discover trends and export poll responses.
            </div>
        </div>
        <div style="
            color:#91A9C5;
            font-size:10px;
            text-align:center;
            padding:22px 0 5px 0;
        ">POLLINSIGHTS · V1.0</div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# FILTER DATA
# =========================================================
filtered = df[
    df["Question"].isin(selected_questions)
    & df["Option"].isin(selected_options)
    & df["Region"].isin(selected_regions)
    & df["Age Group"].isin(selected_ages)
].copy()

if date_range is not None:
    if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
        start_date, end_date = date_range

        valid_dates = filtered["Timestamp"].notna()

        filtered = filtered[
            ~valid_dates
            | filtered["Timestamp"].dt.date.between(
                start_date, end_date
            )
        ]

# =========================================================
# REUSABLE FUNCTIONS
# =========================================================
def render_header(title, subtitle):
    st.markdown(
        f"""
        <div class="page-header">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section(title, caption=None):
    st.markdown(
        f'<div class="section-heading">{title}</div>',
        unsafe_allow_html=True,
    )

    if caption:
        st.markdown(
            f'<div class="section-caption">{caption}</div>',
            unsafe_allow_html=True,
        )


def render_card(label, value, note):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def prepare_chart(fig, height=360):
    fig.update_layout(
        height=height,
        autosize=True,
        margin=dict(l=18, r=18, t=62, b=22),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(
            family="Inter, sans-serif",
            color="#34465E",
            size=12,
        ),
        title=dict(
            font=dict(size=15, color="#193453"),
            x=0.03,
            xanchor="left",
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        automargin=True,
        title_font=dict(size=11),
    )

    fig.update_yaxes(
        gridcolor="#EDF1F6",
        automargin=True,
        title_font=dict(size=11),
    )

    return fig


def get_option_counts(data):
    return (
        data.groupby("Option", as_index=False)
        .agg(Votes=("Respondent ID", "count"))
        .sort_values("Votes", ascending=False)
    )


def show_empty_state():
    st.warning(
        "No responses match your current filters. "
        "Adjust the filters in the left sidebar."
    )


def download_csv(data, filename="poll_responses.csv"):
    st.download_button(
        "⬇️  Download CSV",
        data=data.to_csv(index=False).encode("utf-8"),
        file_name=filename,
        mime="text/csv",
        use_container_width=True,
    )


def render_kpis(data):
    total = len(data)
    respondents = data["Respondent ID"].nunique()
    options = data["Option"].nunique()
    regions = data["Region"].nunique()

    c1, c2, c3, c4 = st.columns(4, gap="medium")

    with c1:
        render_card("TOTAL RESPONSES", f"{total:,}", "Filtered poll records")

    with c2:
        render_card("RESPONDENTS", f"{respondents:,}", "Distinct respondent IDs")

    with c3:
        render_card("ANSWER OPTIONS", f"{options:,}", "Options represented")

    with c4:
        render_card("REGIONS", f"{regions:,}", "Regions represented")


# =========================================================
# PAGE 1: OVERVIEW
# =========================================================
if page == "🏠  Overview":
    render_header(
        "Poll Analytics Overview",
        "Your central workspace for understanding poll preferences and response patterns.",
    )

    if filtered.empty:
        show_empty_state()
    else:
        render_kpis(filtered)

        render_section(
            "Response Overview",
            "Explore the most popular options and the distribution of responses.",
        )

        counts = get_option_counts(filtered)

        left, right = st.columns(2, gap="large")

        with left:
            fig = px.bar(
                counts,
                x="Option",
                y="Votes",
                color="Option",
                color_discrete_sequence=COLORS,
                text="Votes",
                title="Votes by Answer Option",
            )

            fig.update_layout(showlegend=False)
            fig.update_traces(
                textposition="outside",
                cliponaxis=False,
            )

            st.plotly_chart(
                prepare_chart(fig, 390),
                use_container_width=True,
            )

        with right:
            fig = px.pie(
                counts,
                names="Option",
                values="Votes",
                hole=0.55,
                color_discrete_sequence=COLORS,
                title="Response Share",
            )

            fig.update_traces(
                textposition="inside",
                textinfo="percent",
            )

            st.plotly_chart(
                prepare_chart(fig, 390),
                use_container_width=True,
            )

        render_section(
            "Audience Distribution",
            "Compare the number of responses across demographics.",
        )

        left, right = st.columns(2, gap="large")

        with left:
            regions = (
                filtered.groupby("Region", as_index=False)
                .agg(Responses=("Respondent ID", "count"))
                .sort_values("Responses", ascending=False)
            )

            fig = px.bar(
                regions,
                x="Region",
                y="Responses",
                color="Region",
                color_discrete_sequence=COLORS,
                text="Responses",
                title="Responses by Region",
            )

            fig.update_layout(showlegend=False)
            fig.update_traces(
                textposition="outside",
                cliponaxis=False,
            )

            st.plotly_chart(
                prepare_chart(fig, 350),
                use_container_width=True,
            )

        with right:
            ages = (
                filtered.groupby("Age Group", as_index=False)
                .agg(Responses=("Respondent ID", "count"))
                .sort_values("Responses", ascending=False)
            )

            fig = px.bar(
                ages,
                x="Age Group",
                y="Responses",
                color="Age Group",
                color_discrete_sequence=COLORS,
                text="Responses",
                title="Responses by Age Group",
            )

            fig.update_layout(showlegend=False)
            fig.update_traces(
                textposition="outside",
                cliponaxis=False,
            )

            st.plotly_chart(
                prepare_chart(fig, 350),
                use_container_width=True,
            )

        render_section("Recent Responses")

        recent = filtered.sort_values(
            "Timestamp",
            ascending=False,
            na_position="last",
        ).head(10)

        st.dataframe(
            recent,
            hide_index=True,
            use_container_width=True,
        )


# =========================================================
# PAGE 2: POLL RESULTS
# =========================================================
elif page == "📊  Poll Results":
    render_header(
        "Poll Results",
        "Compare answer choices and inspect the results of individual questions.",
    )

    if filtered.empty:
        show_empty_state()
    else:
        questions = sorted(filtered["Question"].unique().tolist())

        question = st.selectbox(
            "Select a poll question",
            questions,
            key="results_question",
        )

        question_data = filtered[
            filtered["Question"] == question
        ]

        counts = get_option_counts(question_data)

        if counts.empty:
            show_empty_state()
        else:
            total = int(counts["Votes"].sum())
            winner = counts.iloc[0]

            share = (
                float(winner["Votes"]) / total * 100
                if total else 0
            )

            c1, c2, c3 = st.columns(3, gap="medium")

            with c1:
                render_card(
                    "QUESTION RESPONSES",
                    f"{total:,}",
                    "Responses to this question",
                )

            with c2:
                render_card(
                    "TOP ANSWER",
                    str(winner["Option"]),
                    "Most selected option",
                )

            with c3:
                render_card(
                    "TOP ANSWER SHARE",
                    f"{share:.1f}%",
                    "Share of question responses",
                )

            render_section(
                "Vote Analysis",
                "Review answer counts and their percentage distribution.",
            )

            left, right = st.columns(2, gap="large")

            with left:
                fig = px.bar(
                    counts,
                    x="Option",
                    y="Votes",
                    color="Option",
                    color_discrete_sequence=COLORS,
                    text="Votes",
                    title="Vote Count by Option",
                )

                fig.update_layout(showlegend=False)
                fig.update_traces(
                    textposition="outside",
                    cliponaxis=False,
                )

                st.plotly_chart(
                    prepare_chart(fig, 400),
                    use_container_width=True,
                )

            with right:
                fig = px.pie(
                    counts,
                    names="Option",
                    values="Votes",
                    hole=0.5,
                    color_discrete_sequence=COLORS,
                    title="Share by Answer",
                )

                fig.update_traces(
                    textposition="inside",
                    textinfo="label+percent",
                )

                st.plotly_chart(
                    prepare_chart(fig, 400),
                    use_container_width=True,
                )

            render_section("Detailed Results")

            result_table = counts.copy()
            result_table["Share (%)"] = (
                result_table["Votes"] / total * 100
            ).round(2)

            st.dataframe(
                result_table,
                hide_index=True,
                use_container_width=True,
            )

            download_csv(
                question_data,
                "poll_question_results.csv",
            )


# =========================================================
# PAGE 3: AUDIENCE INSIGHTS
# =========================================================
elif page == "🌍  Audience Insights":
    render_header(
        "Audience Insights",
        "Understand how poll preferences differ across regions and age groups.",
    )

    if filtered.empty:
        show_empty_state()
    else:
        render_section(
            "Regional Preferences",
            "Compare answer options within each region.",
        )

        region_cross = pd.crosstab(
            filtered["Region"],
            filtered["Option"],
        ).reset_index()

        region_long = region_cross.melt(
            id_vars="Region",
            var_name="Option",
            value_name="Responses",
        )

        fig = px.bar(
            region_long,
            x="Region",
            y="Responses",
            color="Option",
            barmode="group",
            color_discrete_sequence=COLORS,
            title="Answer Preferences by Region",
        )

        st.plotly_chart(
            prepare_chart(fig, 430),
            use_container_width=True,
        )

        render_section(
            "Age Group Preferences",
            "See which answer options are selected across age groups.",
        )

        age_cross = pd.crosstab(
            filtered["Age Group"],
            filtered["Option"],
        ).reset_index()

        age_long = age_cross.melt(
            id_vars="Age Group",
            var_name="Option",
            value_name="Responses",
        )

        fig = px.bar(
            age_long,
            x="Age Group",
            y="Responses",
            color="Option",
            barmode="group",
            color_discrete_sequence=COLORS,
            title="Answer Preferences by Age Group",
        )

        st.plotly_chart(
            prepare_chart(fig, 430),
            use_container_width=True,
        )

        render_section("Audience Summary")

        left, right = st.columns(2, gap="large")

        with left:
            region_summary = (
                filtered.groupby("Region", as_index=False)
                .agg(Responses=("Respondent ID", "count"))
                .sort_values("Responses", ascending=False)
            )

            st.markdown("**Responses by region**")

            st.dataframe(
                region_summary,
                hide_index=True,
                use_container_width=True,
            )

        with right:
            age_summary = (
                filtered.groupby("Age Group", as_index=False)
                .agg(Responses=("Respondent ID", "count"))
                .sort_values("Responses", ascending=False)
            )

            st.markdown("**Responses by age group**")

            st.dataframe(
                age_summary,
                hide_index=True,
                use_container_width=True,
            )


# =========================================================
# PAGE 4: RESPONSE TRENDS
# =========================================================
elif page == "📈  Trends":
    render_header(
        "Response Trends",
        "Explore response activity over time and discover patterns in poll participation.",
    )

    dated = filtered.dropna(subset=["Timestamp"]).copy()

    if dated.empty:
        st.warning(
            "No valid timestamps match your current filters."
        )
    else:
        interval = st.selectbox(
            "Group responses by",
            ["Daily", "Weekly", "Monthly"],
            index=2,
        )

        period_map = {
            "Daily": "D",
            "Weekly": "W",
            "Monthly": "M",
        }

        dated["Period"] = (
            dated["Timestamp"]
            .dt.to_period(period_map[interval])
            .dt.start_time
        )

        trend = (
            dated.groupby("Period", as_index=False)
            .agg(Responses=("Respondent ID", "count"))
        )

        render_section("Response Volume")

        fig = px.line(
            trend,
            x="Period",
            y="Responses",
            markers=True,
            title=f"Responses Over Time — {interval}",
            color_discrete_sequence=[COLORS[0]],
        )

        fig.update_traces(
            line_width=3,
            marker_size=7,
        )

        st.plotly_chart(
            prepare_chart(fig, 430),
            use_container_width=True,
        )

        render_section("Response Trends by Answer")

        trend_options = (
            dated.groupby(["Period", "Option"], as_index=False)
            .agg(Responses=("Respondent ID", "count"))
        )

        fig = px.bar(
            trend_options,
            x="Period",
            y="Responses",
            color="Option",
            barmode="stack",
            color_discrete_sequence=COLORS,
            title="Response Volume by Answer Option",
        )

        st.plotly_chart(
            prepare_chart(fig, 430),
            use_container_width=True,
        )

        render_section("Time Series Data")

        st.dataframe(
            trend.sort_values(
                "Period",
                ascending=False,
            ),
            hide_index=True,
            use_container_width=True,
        )


# =========================================================
# PAGE 5: RAW DATA
# =========================================================
elif page == "🗃️  Raw Data":
    render_header(
        "Poll Data Explorer",
        "Search, inspect, and export the original poll response records.",
    )

    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        render_card(
            "SOURCE RECORDS",
            f"{len(df):,}",
            "Rows in the original dataset",
        )

    with c2:
        render_card(
            "FILTERED RECORDS",
            f"{len(filtered):,}",
            "Rows matching sidebar filters",
        )

    with c3:
        render_card(
            "DATA FIELDS",
            f"{len(df.columns):,}",
            "Available columns",
        )

    render_section(
        "Search and Explore",
        "Search within the filtered data, then download the matching records.",
    )

    search = st.text_input(
        "Search records",
        placeholder="Enter a respondent ID, option, question, region or age group...",
    )

    display_data = filtered.copy()

    if search.strip():
        match_mask = display_data.astype(str).apply(
            lambda column: column.str.contains(
                search.strip(),
                case=False,
                regex=False,
                na=False,
            )
        ).any(axis=1)

        display_data = display_data[match_mask]

    st.caption(f"{len(display_data):,} records displayed")

    st.dataframe(
        display_data,
        hide_index=True,
        use_container_width=True,
        height=460,
    )

    download_csv(
        display_data,
        "filtered_poll_responses.csv",
    )

    with st.expander("View data quality report"):
        quality = pd.DataFrame(
            {
                "Column": df.columns,
                "Data Type": [
                    str(df[column].dtype)
                    for column in df.columns
                ],
                "Missing Values": [
                    int(df[column].isna().sum())
                    for column in df.columns
                ],
                "Unique Values": [
                    int(df[column].nunique(dropna=True))
                    for column in df.columns
                ],
            }
        )

        st.dataframe(
            quality,
            hide_index=True,
            use_container_width=True,
        )

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        PollInsights · Poll Results Visualization · Built with Streamlit and Plotly
    </div>
    """,
    unsafe_allow_html=True,
)
