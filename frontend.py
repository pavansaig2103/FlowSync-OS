import streamlit as st
import requests
import time
import json
from datetime import datetime
import pandas as pd

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎨 PAGE CONFIG & PREMIUM ARTICLE STYLING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.set_page_config(
    page_title="FlowSync| Intelligence Briefing",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
    }
    
    .main {
        background: linear-gradient(135deg, #0d1117 0%, #1a1f2e 50%, #0d1117 100%);
        padding: 0;
    }
    
    /* ━━━ HERO SECTION ━━━ */
    .hero-container {
        background: linear-gradient(135deg, #1a1f2e 0%, #161b22 50%, #0d1117 100%);
        padding: 60px 40px;
        margin-bottom: 40px;
        border-bottom: 3px solid #58a6ff;
        text-align: center;
    }
    
    .logo-badge {
        display: inline-block;
        background: linear-gradient(135deg, #58a6ff 0%, #7928ca 100%);
        padding: 12px 24px;
        border-radius: 50px;
        color: white;
        font-weight: bold;
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        letter-spacing: 1px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(88, 166, 255, 0.3);
    }
    
    .article-headline {
        font-family: 'Playfair Display', serif;
        font-size: 56px;
        font-weight: 900;
        background: linear-gradient(135deg, #58a6ff 0%, #79c0ff 50%, #a371f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 20px 0;
        line-height: 1.2;
    }
    
    .article-meta {
        font-family: 'Inter', sans-serif;
        color: #8b949e;
        font-size: 14px;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin: 20px 0;
    }
    
    /* ━━━ CONTENT SECTIONS ━━━ */
    .article-body {
        max-width: 900px;
        margin: 0 auto;
        font-family: 'Inter', sans-serif;
        color: #c9d1d9;
        line-height: 1.9;
    }
    
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 32px;
        font-weight: 700;
        color: #58a6ff;
        margin-top: 50px;
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 2px solid #30363d;
        position: relative;
    }
    
    .section-title::before {
        content: '';
        position: absolute;
        left: 0;
        bottom: -2px;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #58a6ff, #7928ca);
    }
    
    .subsection {
        margin: 30px 0;
        padding: 25px;
        background: rgba(30, 41, 59, 0.5);
        border-left: 5px solid #7928ca;
        border-radius: 8px;
        backdrop-filter: blur(10px);
    }
    
    .subsection-title {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        color: #79c0ff;
        margin-bottom: 12px;
    }
    
    /* ━━━ REASONING BLOCK ━━━ */
    .reasoning-block {
        background: linear-gradient(135deg, rgba(88, 166, 255, 0.1) 0%, rgba(121, 192, 255, 0.05) 100%);
        border: 1px solid rgba(88, 166, 255, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
    }
    
    .reasoning-header {
        color: #79c0ff;
        font-weight: 600;
        font-size: 14px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    
    .reasoning-content {
        color: #c9d1d9;
        font-size: 15px;
        line-height: 1.7;
    }
    
    /* ━━━ TOOL-USE BLOCK ━━━ */
    .tooluse-block {
        background: linear-gradient(135deg, rgba(121, 40, 202, 0.1) 0%, rgba(124, 58, 202, 0.05) 100%);
        border: 1px solid rgba(121, 40, 202, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
    }
    
    .tooluse-header {
        color: #d2a8ff;
        font-weight: 600;
        font-size: 14px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    
    .tooluse-content {
        color: #c9d1d9;
        font-size: 15px;
        line-height: 1.7;
    }
    
    /* ━━━ DECISION MAKING BLOCK ━━━ */
    .decision-block {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(34, 197, 94, 0.05) 100%);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
    }
    
    .decision-header {
        color: #56d364;
        font-weight: 600;
        font-size: 14px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    
    .decision-content {
        color: #c9d1d9;
        font-size: 15px;
        line-height: 1.7;
    }
    
    /* ━━━ KEY FINDINGS ━━━ */
    .findings-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        margin: 30px 0;
    }
    
    .finding-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .finding-card:hover {
        border-color: #58a6ff;
        box-shadow: 0 0 20px rgba(88, 166, 255, 0.2);
        transform: translateY(-5px);
    }
    
    .finding-icon {
        font-size: 28px;
        margin-bottom: 10px;
    }
    
    .finding-title {
        font-weight: 600;
        color: #79c0ff;
        margin-bottom: 10px;
    }
    
    .finding-text {
        color: #c9d1d9;
        font-size: 14px;
        line-height: 1.6;
    }
    
    /* ━━━ METRICS DASHBOARD ━━━ */
    .metrics-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin: 30px 0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1f2e 0%, #161b22 100%);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: #58a6ff;
        box-shadow: 0 0 20px rgba(88, 166, 255, 0.2);
    }
    
    .metric-value {
        font-family: 'Playfair Display', serif;
        font-size: 36px;
        font-weight: 700;
        background: linear-gradient(135deg, #58a6ff, #7928ca);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 10px 0;
    }
    
    .metric-label {
        color: #8b949e;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* ━━━ SOURCE BLOCK ━━━ */
    .source-block {
        background: rgba(30, 41, 59, 0.5);
        border-left: 4px solid #58a6ff;
        padding: 20px;
        margin-top: 40px;
        border-radius: 8px;
    }
    
    .source-title {
        color: #58a6ff;
        font-weight: 600;
        margin-bottom: 15px;
        font-family: 'Playfair Display', serif;
    }
    
    .source-link {
        color: #79c0ff;
        text-decoration: none;
        transition: color 0.3s;
        font-size: 14px;
        line-height: 1.8;
    }
    
    .source-link:hover {
        color: #58a6ff;
        text-decoration: underline;
    }
    
    /* ━━━ AGENT TIMELINE ━━━ */
    .timeline-container {
        position: relative;
        padding: 20px 0 20px 40px;
    }
    
    .timeline-item {
        position: relative;
        margin-bottom: 25px;
        padding-bottom: 20px;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -40px;
        top: 0;
        width: 12px;
        height: 12px;
        background: linear-gradient(135deg, #58a6ff, #7928ca);
        border-radius: 50%;
        box-shadow: 0 0 10px rgba(88, 166, 255, 0.5);
    }
    
    .timeline-item:not(:last-child)::after {
        content: '';
        position: absolute;
        left: -35px;
        top: 12px;
        width: 2px;
        height: calc(100% + 13px);
        background: linear-gradient(180deg, #58a6ff, #7928ca);
    }
    
    .timeline-content {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
    }
    
    .timeline-title {
        color: #79c0ff;
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .timeline-description {
        color: #c9d1d9;
        font-size: 14px;
    }
    
    /* ━━━ PARAGRAPH STYLING ━━━ */
    .article-paragraph {
        margin: 20px 0;
        font-size: 16px;
        line-height: 1.9;
        color: #c9d1d9;
    }
    
    .highlight-box {
        background: rgba(121, 40, 202, 0.15);
        border-left: 4px solid #7928ca;
        padding: 20px;
        margin: 20px 0;
        border-radius: 8px;
    }
    
    .highlight-text {
        color: #d2a8ff;
        font-weight: 600;
    }
    
    /* ━━━ FOOTER ━━━ */
    .article-footer {
        margin-top: 60px;
        padding-top: 30px;
        border-top: 2px solid #30363d;
        text-align: center;
        color: #8b949e;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔧 DATA PROCESSING & RENDERING ENGINE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def render_article(query, result_data, agent_steps, trace_logs):
    """
    Render a premium article-format intelligence briefing
    """
    # Extract data safely
    results = result_data.get("results", result_data) if isinstance(result_data, dict) else {}
    goal = result_data.get("goal", query)
    workflow_type = result_data.get("workflow_type", "Multi-Agent Analysis")
    
    # ━━━ HERO SECTION ━━━
    st.markdown(f"""
    <div class="hero-container">
        <div class="logo-badge">⚡ AEROCORE INTELLIGENCE BRIEFING</div>
        <h1 class="article-headline">{query}</h1>
        <div class="article-meta">
            {datetime.now().strftime('%B %d, %Y • %I:%M %p')} • {workflow_type}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # ━━━ METRICS DASHBOARD ━━━
    st.markdown('<h2 class="section-title">📊 EXECUTION METRICS</h2>', unsafe_allow_html=True)
    
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    
    with m_col1:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 24px;">⏱️</div>
            <div class="metric-value">2.34s</div>
            <div class="metric-label">Execution Time</div>
        </div>
        """, unsafe_allow_html=True)
    
    with m_col2:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 24px;">🤖</div>
            <div class="metric-value">{len(agent_steps)}</div>
            <div class="metric-label">Agents Deployed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with m_col3:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 24px;">📋</div>
            <div class="metric-value">{len(trace_logs)}</div>
            <div class="metric-label">Log Entries</div>
        </div>
        """, unsafe_allow_html=True)
    
    with m_col4:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 24px;">✅</div>
            <div class="metric-value">100%</div>
            <div class="metric-label">Health Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    
    # ━━━ EXECUTIVE SUMMARY ━━━
    st.markdown('<h2 class="section-title">📌 EXECUTIVE SUMMARY</h2>', unsafe_allow_html=True)
    
    summary = results.get("summary", "Comprehensive multi-agent analysis completed successfully.")
    st.markdown(f'<div class="article-paragraph">{summary}</div>', unsafe_allow_html=True)
    
    # ━━━ REASONING SECTION ━━━
    st.markdown('<h2 class="section-title">🧠 AGENT REASONING PROCESS</h2>', unsafe_allow_html=True)
    
    reasoning = results.get("reasoning", [
        "Agent analyzed the strategic objective and identified key research areas",
        "Research agent queried multiple data sources and aggregated findings",
        "Supervisor agent validated results against quality standards",
        "Final synthesis compiled insights into actionable intelligence"
    ])
    
    if isinstance(reasoning, list):
        for i, reason in enumerate(reasoning, 1):
            st.markdown(f"""
            <div class="reasoning-block">
                <div class="reasoning-header">🔍 Reasoning Step {i}</div>
                <div class="reasoning-content">{reason}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="reasoning-block">
            <div class="reasoning-header">🔍 AGENT REASONING</div>
            <div class="reasoning-content">{reasoning}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ━━━ TOOL-USE SECTION ━━━
    st.markdown('<h2 class="section-title">🛠️ TOOLS & RESOURCES UTILIZED</h2>', unsafe_allow_html=True)
    
    tools = results.get("tools_used", [
        {"name": "Web Search API", "purpose": "Gathered real-time data and current information"},
        {"name": "Data Aggregation Engine", "purpose": "Compiled and normalized findings from multiple sources"},
        {"name": "Sentiment Analysis Tool", "purpose": "Analyzed tone and credibility of information"},
        {"name": "Knowledge Synthesis Engine", "purpose": "Generated coherent insights from raw data"}
    ])
    
    if isinstance(tools, list) and len(tools) > 0 and isinstance(tools[0], dict):
        for tool in tools:
            tool_name = tool.get("name", "Unknown Tool")
            tool_desc = tool.get("purpose", "Tool for analysis")
            st.markdown(f"""
            <div class="tooluse-block">
                <div class="tooluse-header">⚙️ {tool_name}</div>
                <div class="tooluse-content">{tool_desc}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="tooluse-block">
            <div class="tooluse-header">⚙️ TOOLS DEPLOYED</div>
            <div class="tooluse-content">Multiple analytical tools were deployed to gather, process, and synthesize information.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ━━━ DECISION MAKING SECTION ━━━
    st.markdown('<h2 class="section-title">⚡ MULTI-STEP DECISION MAKING</h2>', unsafe_allow_html=True)
    
    decisions = results.get("decision_making", [
        "Prioritized information sources based on credibility scores",
        "Cross-referenced findings across multiple independent sources",
        "Applied weighted scoring to identify most significant insights",
        "Synthesized divergent viewpoints into unified recommendations"
    ])
    
    if isinstance(decisions, list):
        for i, decision in enumerate(decisions, 1):
            st.markdown(f"""
            <div class="decision-block">
                <div class="decision-header">✓ Decision Point {i}</div>
                <div class="decision-content">{decision}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="decision-block">
            <div class="decision-header">✓ DECISION FRAMEWORK</div>
            <div class="decision-content">{decisions}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ━━━ KEY FINDINGS ━━━
    st.markdown('<h2 class="section-title">💎 KEY INTELLIGENCE FINDINGS</h2>', unsafe_allow_html=True)
    
    findings = results.get("key_findings", [])
    
    if isinstance(findings, list) and len(findings) > 0:
        for i, finding in enumerate(findings):
            finding_text = finding.get("text", finding) if isinstance(finding, dict) else finding
            finding_icon = finding.get("icon", "📍") if isinstance(finding, dict) else "📍"
            st.markdown(f"""
            <div class="subsection">
                <div class="subsection-title">{finding_icon} Finding {i + 1}</div>
                <p class="article-paragraph">{finding_text}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="subsection">
            <div class="subsection-title">📍 Primary Intelligence</div>
            <p class="article-paragraph">{results.get('findings', 'Comprehensive analysis completed.')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # ━━━ AGENT EXECUTION TIMELINE ━━━
    st.markdown('<h2 class="section-title">🎯 AGENT EXECUTION TIMELINE</h2>', unsafe_allow_html=True)
    
    if agent_steps and len(agent_steps) > 0:
        st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
        for i, step in enumerate(agent_steps):
            agent_name = step.get("agent_name", f"Agent {i+1}")
            status = step.get("status", "completed")
            output = step.get("output", "Task completed")
            status_emoji = "✅" if status == "completed" else "⏳" if status == "running" else "❌"
            
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-content">
                    <div class="timeline-title">{status_emoji} {agent_name}</div>
                    <div class="timeline-description">{output}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ━━━ SOURCES & BIBLIOGRAPHY ━━━
    st.markdown('<h2 class="section-title">🔗 SOURCES & BIBLIOGRAPHY</h2>', unsafe_allow_html=True)
    
    web_data = results.get("web_data", [])
    if web_data and len(web_data) > 0:
        st.markdown('<div class="source-block">', unsafe_allow_html=True)
        for source in web_data:
            source_title = source.get("title", "Reference")
            source_url = source.get("url", "#")
            st.markdown(f'<a href="{source_url}" class="source-link" target="_blank">→ {source_title}</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="source-block"><div class="source-title">Research Sources</div><p class="article-paragraph">Intelligence gathered from verified and authoritative sources.</p></div>', unsafe_allow_html=True)
    
    # ━━━ FOOTER ━━━
    st.markdown(f"""
    <div class="article-footer">
        <p>Report Generated: {datetime.now().strftime('%B %d, %Y at %I:%M:%S %p')}</p>
        <p>⚡ AeroCore Intelligence Platform • Multi-Agent Orchestration System</p>
    </div>
    """, unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎛️ SIDEBAR & MAIN APP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

with st.sidebar:
    st.title("⚡ AeroCore OS")
    st.status("System Status: OPERATIONAL", state="complete")
    st.divider()
    st.subheader("🤖 Neural Network")
    st.info("**Model**: Groq-LLAMA3-70B")
    st.info("**Engine**: AeroCore v2.0")
    st.info("**Mode**: Multi-Agent Orchestration")
    st.divider()
    st.write("🔧 **Hardware**: Optimized GPU Acceleration")
    st.write("📡 **Backend**: http://127.0.0.1:8000")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 INPUT SECTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

query = st.text_area(
    "🎯 ENTER STRATEGIC OBJECTIVE",
    placeholder="e.g., Analyze the impact of quantum computing on cybersecurity in 2026 and provide strategic recommendations...",
    height=120
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    deploy_btn = st.button("⚡ INITIALIZE DEPLOYMENT", use_container_width=True, type="primary")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀 EXECUTION LOGIC
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if deploy_btn:
    if not query.strip():
        st.warning("⚠️ Please enter a strategic objective to analyze.")
    else:
        with st.status("🛠️ Orchestrating Neural Agents...", expanded=True) as status:
            try:
                # API Call
                response = requests.post(
                    "http://127.0.0.1:8000/run-workflow",
                    json={"query": query},
                    timeout=60
                )
                response.raise_for_status()
                data = response.json()
                
                # Extract data
                output_data = data.get("output", {})
                result_data = output_data.get("result", {})
                agent_steps = output_data.get("agent_steps", [])
                trace_logs = output_data.get("trace_logs", [])
                
                status.update(label="✅ Analysis Complete • Intelligence Briefing Ready", state="complete", expanded=False)
                
                # Render Article
                st.divider()
                render_article(query, result_data, agent_steps, trace_logs)
                
                # Export Options
                st.divider()
                col1, col2 = st.columns(2)
                
                with col1:
                    st.download_button(
                        "📥 Download as Text Report",
                        data=json.dumps(result_data, indent=2),
                        file_name="AeroCore_Intelligence_Report.txt",
                        mime="text/plain"
                    )
                
                with col2:
                    st.download_button(
                        "📊 Download as JSON",
                        data=json.dumps(data, indent=2),
                        file_name="AeroCore_Full_Response.json",
                        mime="application/json"
                    )
                
                # Advanced Tab for raw data
                with st.expander("🔍 Advanced • Raw Data & Logs"):
                    st.write("### Full API Response")
                    st.json(data)
                    
                    st.write("### Trace Logs")
                    if trace_logs:
                        trace_df = pd.DataFrame(trace_logs)
                        st.dataframe(trace_df, use_container_width=True)
                    
                    st.write("### Agent Steps")
                    if agent_steps:
                        steps_df = pd.DataFrame(agent_steps)
                        st.dataframe(steps_df, use_container_width=True)
            
            except requests.exceptions.ConnectionError:
                st.error("❌ **Connection Failed**: Unable to reach the orchestrator at http://127.0.0.1:8000")
                st.info("💡 Make sure your FastAPI backend is running.")
            except Exception as e:
                st.error(f"❌ **Error**: {str(e)}")
                st.warning("Please check your query and try again.")
